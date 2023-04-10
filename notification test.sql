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
    
    -- Get the list of users to notify
    SELECT
        USERNAME,
        DESCRIPTION
    FROM notification
    WHERE DUE_DATE BETWEEN @CurrentDate AND DATEADD(HOUR, 24, @CurrentDate)
    
    -- Iterate through the results and send emails using sp_send_dbmail
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @Body = 'Dear ' + USERNAME + ',<br><br>' + DESCRIPTION;
        SET @Subject = 'Notification for Due Date';
        SET @Recipients = USERNAME + '@example.com';
        
        EXEC msdb.dbo.sp_send_dbmail
            @profile_name = 'YourDatabaseMailProfile',
            @recipients = @Recipients,
            @subject = @Subject,
            @body = @Body,
            @body_format = 'HTML';
        
        FETCH NEXT FROM cursor INTO USERNAME, DESCRIPTION;
    END
    
    CLOSE cursor;
    DEALLOCATE cursor;
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