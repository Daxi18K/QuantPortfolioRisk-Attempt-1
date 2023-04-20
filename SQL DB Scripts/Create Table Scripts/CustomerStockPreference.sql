USE [QuantPortfolioRisk]
GO

/****** Object:  Table [Customer].[CustomerMaster]    Script Date: 14/04/2023 10:15:35 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Customer].[CustomerStockPreference](
	[Customer ID] [numeric](18, 0) NOT NULL,
	[ETF_Name] [VARCHAR](10) NULL,
    [Portfolio_Category] [VARCHAR](50) NULL,
	[Date_Updated] [date] NULL
) ON [PRIMARY]
GO
