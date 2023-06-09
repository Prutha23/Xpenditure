USE Xpenditure
GO

CREATE TABLE  USERS (
  ID INT IDENTITY PRIMARY KEY,
  USERNAME NVARCHAR(50) NOT NULL UNIQUE,
  PASSWORD NVARCHAR(30) NOT NULL ,
  ROLE INT,
  IS_ACTIVE INT, 
  CREATED_DATE DATE DEFAULT getdate(),
  UPDATED_DATE DATE DEFAULT getdate()
);


CREATE TABLE  USERS_DETAILS (
  ID INT IDENTITY PRIMARY KEY,
  U_ID INT NOT NULL  ,
  FNAME VARCHAR(30) NOT NULL,
  LNAME  VARCHAR(30),
  EMAILID NVARCHAR(40) NOT NULL,
  PHONENO BIGINT NOT NULL,
  ADDRESSLINE1 NVARCHAR(40),
  STREET NVARCHAR(40),
  PROVINCE NVARCHAR(30),
  ZIPCODE NVARCHAR(20),
  COUNTRY VARCHAR(40),
  IS_PREMIUM INT,
  CREATED_DATE DATE DEFAULT getdate(),
  UPDATED_DATE DATE DEFAULT getdate(),
  UPDATED_BY INT
    
	CONSTRAINT fk_USERS_DETAILS_USERS
		FOREIGN KEY (U_ID)
		REFERENCES USERS (ID),
	CONSTRAINT fk_USERS_DETAILS_UPDATEUSER
		FOREIGN KEY (UPDATED_BY)
		REFERENCES USERS (ID)
);


CREATE TABLE  ROLES (
  ID INT IDENTITY PRIMARY KEY,
  ROLESNAME VARCHAR(20) NOT NULL ,
  ROLESDESC VARCHAR(20),
  CREATED_DATE DATE DEFAULT getdate()
);

	ALTER TABLE USERS ADD CONSTRAINT fk_ROLES_USERS FOREIGN KEY (ROLE) REFERENCES ROLES (ID);

CREATE TABLE  CATEGORY (
  ID INT IDENTITY PRIMARY KEY,
  NAME VARCHAR(20) UNIQUE NOT NULL ,
  CREATED_BY INT,
  CREATED_DATE DATE DEFAULT getdate(),
  UPDATED_BY INT,
  UPDATED_DATE DATE DEFAULT getdate(),
  REMARKS NVARCHAR(50)

	CONSTRAINT fk_CATEGORY_CREATEUSER
		FOREIGN KEY (CREATED_BY)
		REFERENCES USERS (ID),
	CONSTRAINT fk_CATEGORY_UPDATEUSER
		FOREIGN KEY (UPDATED_BY)
		REFERENCES USERS (ID)
);

CREATE TABLE EXPENSE(
 ID INT IDENTITY PRIMARY KEY,
 CAT_ID INT NOT NULL,
 AMOUNT DECIMAL(7,2) NOT NULL,
 PAYEMNT_METHOD NVARCHAR(20) NOT NULL DEFAULT 'CASH',
 EXPENSE_DATE DATE NOT NULL DEFAULT GETDATE(),
 CREATED_BY INT,
 DESCRIPTION NVARCHAR(250),
  CREATED_DATE DATE DEFAULT getdate(),
  UPDATED_BY INT,
  UPDATED_DATE DATE DEFAULT getdate(),

  CONSTRAINT fk_EXPENSE_CREATEUSER
    FOREIGN KEY (CREATED_BY)
    REFERENCES USERS (ID),
	 CONSTRAINT fk_EXPENSE_UPDATEUSER
    FOREIGN KEY (UPDATED_BY)
    REFERENCES USERS (ID),
	CONSTRAINT fk_EXPENSE_CATEGORY
    FOREIGN KEY (CAT_ID)
    REFERENCES CATEGORY (ID),
);

CREATE TABLE PREMIUM_USERS (
  ID INT IDENTITY PRIMARY KEY,
  USERID INT NOT NULL UNIQUE ,
  START_DATE DATE DEFAULT getdate(),
  END_DATE DATE,
  CREATED_DATE DATE DEFAULT getdate(),
  UPDATED_BY INT,
  UPDATED_DATE DATE DEFAULT getdate(),
  
	CONSTRAINT fk_PREMIUM_USERS_USERS
    FOREIGN KEY (USERID)
    REFERENCES USERS (ID),
	CONSTRAINT fk_PREMIUM_USERS_UPDATEUSER
    FOREIGN KEY (UPDATED_BY)
    REFERENCES USERS (ID)
);


CREATE TABLE PAYMENT (
	ID INT IDENTITY PRIMARY KEY,
	USERID INT,
	PAYMENT_METHOD VARCHAR(10) NOT NULL,
	SUBSRIPTION_DATE DATE DEFAULT getdate(),
	AMOUNT INT,
	CARD_HOLDER_NAME VARCHAR(30) NOT NULL,
	CARD_NO VARCHAR(30) NOT NULL,
	PAYMENT_STATUS CHAR(1),
	UPDATED_BY INT,
	UPDATED_DATE DATE DEFAULT getdate(),
	CONSTRAINT fk_PAYMENT_PREMIUM_USERS
    FOREIGN KEY (USERID)
    REFERENCES PREMIUM_USERS (ID)
);


CREATE TABLE NOTIFICATION (
    ID INT IDENTITY,
	U_ID INT NOT NULL,
    EMAIL VARCHAR(255) NOT NULL,
    DUE_DATE DATE NOT NULL,
    DESCRIPTION VARCHAR(MAX),
	CREATED_BY INT,
	CREATED_DATE DATE DEFAULT getdate(),
	UPDATED_BY INT,
	UPDATED_DATE DATE DEFAULT getdate(),
  
    CONSTRAINT PK_NOTIFICATION PRIMARY KEY (ID), 
	CONSTRAINT fk_NOTIFICATION_USERS
    FOREIGN KEY (U_ID)
    REFERENCES USERS (ID),
	  CONSTRAINT fk_NOTIFICATION_CREATEUSER
    FOREIGN KEY (CREATED_BY)
    REFERENCES USERS (ID),
	 CONSTRAINT fk_NOTIFICATION_UPDATEUSER
    FOREIGN KEY (UPDATED_BY)
    REFERENCES USERS (ID),
);

-- insert statement for ROLE table 

INSERT INTO ROLES(ROLESNAME, ROLESDESC) VALUES('USER', 'normal user'); 
INSERT INTO ROLES(ROLESNAME, ROLESDESC) VALUES('ADMIN', 'admin user'); 

-- procedure to approve payment 

CREATE PROCEDURE [dbo].[APPROVE_PAYMENT]
    @id INT,
	@uid INT,
    @start_date date,
	@end_date date
AS
BEGIN
    IF EXISTS (SELECT ID FROM PREMIUM_USERS WHERE USERID = @id)
    BEGIN
        UPDATE PREMIUM_USERS
        SET START_DATE = @start_date,
            END_DATE = @end_date,
			UPDATED_DATE = getdate(),
			UPDATED_BY = @uid
        WHERE USERID = @id
    END
    ELSE
    BEGIN
        INSERT INTO PREMIUM_USERS(USERID, START_DATE, END_DATE)
        VALUES (@id, @start_date, @end_date)
    END
END

-- Procedure to send email notification for reminders

-- first enabled access to database mail xps
sp_configure 'show advanced options', 1;  
GO  
RECONFIGURE; 
GO
sp_configure 'Database Mail XPs', 1;  
GO  
RECONFIGURE  
GO

-- this procedure will be called everynight using [XpenditureEmailJob]

CREATE PROCEDURE SendDueDateNotifications
AS
BEGIN
    DECLARE @CurrentDate DATETIME = GETDATE();
    
    DECLARE @Body NVARCHAR(MAX);
    DECLARE @Subject NVARCHAR(255);
    DECLARE @Recipients NVARCHAR(MAX);
	 DECLARE @Email NVARCHAR(MAX); 
	  DECLARE @Description NVARCHAR(MAX); 

    -- Declare and initialize the cursor
    DECLARE cur CURSOR FOR
    SELECT
        EMAIL,
        DESCRIPTION
    FROM NOTIFICATION
    WHERE DUE_DATE BETWEEN @CurrentDate AND DATEADD(HOUR, 24, @CurrentDate);
    
    OPEN cur;
    
    -- Iterate through the results and send emails using sp_send_dbmail
    FETCH NEXT FROM cur INTO @Email, @Description;
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @Body = 'Dear user,<br><br>This is reminder regarding ' + @Description;
        SET @Subject = 'Xpenditure - Notification for Due Date';
        SET @Recipients = @Email;
        
        EXEC msdb.dbo.sp_send_dbmail
            @profile_name = 'XpenditureProfile',
            @recipients = @Recipients,
            @subject = @Subject,
            @body = @Body,
            @body_format = 'HTML';
        
        FETCH NEXT FROM cur INTO @Email, @Description;
    END
    
    CLOSE cur;
    DEALLOCATE cur;
END 

-- function to hash password

CREATE FUNCTION [dbo].[HashPassword]
    (@password NVARCHAR(20))
    RETURNS VARBINARY(20)
    AS
BEGIN
    RETURN HASHBYTES('SHA1', RTRIM(RTRIM(@password)));
END
