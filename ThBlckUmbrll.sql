USE master
GO

IF EXISTS(select * from sys.databases where name='ThBlkUmbrll')
DROP DATABASE ThBlkUmbrll

CREATE DATABASE ThBlkUmbrll;
GO

USE ThBlkUmbrll;
GO

CREATE TABLE [dbo].[Users](
	[UserID] [int] IDENTITY(1,1) NOT NULL,
	[Username] [varchar](120) NOT NULL,
	[FirstName] [varchar] (120) NOT NULL,
	[LastName] [varchar] (120) NOT NULL,
	[Email] [varchar](50) NOT NULL,
    [Password] [varchar](130) NOT NULL,
	[LastLogin] [datetime] DEFAULT GETDATE(),
	
);