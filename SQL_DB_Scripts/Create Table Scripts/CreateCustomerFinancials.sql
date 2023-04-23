USE [QuantPortfolioRisk]
GO

/****** Object:  Table [Customer].[CustomerMaster]    Script Date: 14/04/2023 10:15:35 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Customer].[CustomerFinancials](
	[Customer ID] [numeric](18, 0) NOT NULL,
	[Expected_Fund_Size] [numeric](18, 0) NULL,
    [Investment_Prop] FLOAT NULL,
    [Frequency_of_Investment] VARCHAR(5) NULL,
    [Date_Updated] [date] NULL
) ON [PRIMARY]
GO


