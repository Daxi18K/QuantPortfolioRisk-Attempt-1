USE [QuantPortfolioRisk]
GO

/****** Object:  Table [Customer].[CustomerMaster]    Script Date: 14/04/2023 10:15:35 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Customer].[CustomerPortfolioPreference](
	[Customer ID] [numeric](18, 0) NOT NULL,
	[Portfolio_Driver] [VARCHAR](10) NULL,
    [Risk_Profile] [VARCHAR](10) NULL,
    [Return_Profile] [VARCHAR](10) NULL,
    [Date_Updated] [date] NULL
) ON [PRIMARY]
GO
