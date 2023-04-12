SELECT * FROM [dbo].[CATEGORY]


SELECT * from users


SELECT * from USERS_DETAILS

SELECT * FROM ROLES r


SELECT * FROM [dbo].[EXPENSE]

---1 insert in user table through procedure
=---2 data fect from user
--THEN CREATE USER details FILE AND premium USER file
--- NOTIFICATION TABLE--- FOR MAIL SCHEDULE

-- USERID,USERNAME=MAILID,DUE_DATE, DESCRIPTION ''
---- DUE_DATE BEFORE 24 HRS
---SCHEDULE

ALTER TABLE [dbo].[EXPENSE]
	ADD  payment_mehtod NVARCHAR(20) NOT NULL
DEFAULT 'CASH' ;



ALTER TABLE [dbo].[EXPENSE]
	ADD  DESCRIPTION NVARCHAR(MAX)  NULL;


CREATE PROCEDURE SendDueDateNotifications
AS
BEGIN
    DECLARE @CurrentDate DATETIME = GETDATE();
    
    DECLARE @Body NVARCHAR(MAX);
    DECLARE @Subject NVARCHAR(255);
    DECLARE @Recipients NVARCHAR(MAX);
	 DECLARE @UserName NVARCHAR(MAX); 
	  DECLARE @Description NVARCHAR(MAX); 

    -- Declare and initialize the cursor
    DECLARE cur CURSOR FOR
    SELECT
        USERNAME,
        DESCRIPTION
    FROM notification
    WHERE DUE_DATE BETWEEN @CurrentDate AND DATEADD(HOUR, 24, @CurrentDate);
    
    OPEN cur;
    
    -- Iterate through the results and send emails using sp_send_dbmail
    FETCH NEXT FROM cur INTO @UserName, @Description;
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @Body = 'Dear ' + @UserName + ',<br><br>' + @Description;
        SET @Subject = 'Notification for Due Date';
        SET @Recipients = @UserName + '@example.com';
        
        EXEC msdb.dbo.sp_send_dbmail
            @profile_name = 'YourDatabaseMailProfile',
            @recipients = @Recipients,
            @subject = @Subject,
            @body = @Body,
            @body_format = 'HTML';
        
        FETCH NEXT FROM cur INTO @UserName, @Description;
    END
    
    CLOSE cur;
    DEALLOCATE cur;
END 



CREATE TABLE notification (
    ID INT NOT NULL,
	U_ID INT NOT NULL,
    USERNAME VARCHAR(50) NOT NULL,
    MAILID VARCHAR(255) NOT NULL,
    DUE_DATE DATE NOT NULL,
    DESCRIPTION VARCHAR(MAX) NOT NULL,
    CONSTRAINT PK_notification PRIMARY KEY (ID),

	 
	CONSTRAINT fk_NOTIFICATION_USERS
    FOREIGN KEY (U_ID)
    REFERENCES USERS (USERID)
);