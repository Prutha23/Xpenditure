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
  PHONENO INT NOT NULL,
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
  NAME VARCHAR(20) NOT NULL ,
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
 DESCRIPTION NVARCHAR(250),
  CREATED_DATE DATE DEFAULT getdate(),
  UPDATED_BY INT,
  UPDATED_DATE DATE DEFAULT getdate(),
    FOREIGN KEY (CREATED_BY)
    REFERENCES USERS (ID),
	 CONSTRAINT fk_EXPENSE_UPDATEUSER
    FOREIGN KEY (UPDATED_BY)
    REFERENCES USERS (ID),
    FOREIGN KEY (CAT_ID)
    REFERENCES CATEGORY (ID),
  ID INT IDENTITY PRIMARY KEY,
  USERID INT NOT NULL UNIQUE ,
  PASSWORD NVARCHAR(30) NOT NULL ,
  ROLES INT,
  SUBSCRIPTION_DATE DATE DEFAULT getdate(),
  START_DATE DATE,
  END_DATE DATE,
  IS_REPEAT CHAR(3),
  CREATED_DATE DATE DEFAULT getdate()

  CONSTRAINT fk_PREMIUM_USERS_USERS
    FOREIGN KEY (USERID)
    REFERENCES USERS (ID)

    );
    FOREIGN KEY (USERID)
    REFERENCES PREMIUM_USERS (ID)



		 
		 