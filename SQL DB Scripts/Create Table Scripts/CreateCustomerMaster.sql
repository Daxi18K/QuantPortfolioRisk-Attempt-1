USE [QuantPortfolioRisk]
GO

/****** Object:  Table [Customer].[CustomerMaster]    Script Date: 14/04/2023 10:15:35 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Customer].[CustomerMaster](
	[Record_ID] [numeric](18, 0) NOT NULL,
	[Customer_ID] [numeric](18, 0) NOT NULL,
	[Date_of_Birth] [date] NULL,
	[State] [varchar](5) NULL,
	[Occupation] [varchar](20) NULL,
	[Investment_Exp] [varchar](20) NULL,
	[Date_Updated] [datetime] DEFAULT current_timestamp,
	PRIMARY KEY (Record_ID)
) ON [PRIMARY]
GO


