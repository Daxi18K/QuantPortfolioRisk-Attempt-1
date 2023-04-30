USE [QuantPortfolioRisk]
GO

/****** Object:  Table [Customer].[FactCustomerDetails]    Script Date: 30/04/2023 8:45:09 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Customer].[FactCustomerDetails](
	[Record_ID] [numeric](18, 0) NOT NULL,
	[Customer_ID] [numeric](18, 0) NOT NULL,
	[Date_of_Birth] [date] NULL,
	[State_ID] [int] NOT NULL FOREIGN KEY REFERENCES [Customer].[DimStateDetails](State_ID),
	[Occupation_ID] [int] NOT NULL FOREIGN KEY REFERENCES [Customer].[DimOccupationDetails](Occupation_ID),
	[Investment_Exp] [varchar](20) NULL,
	[Expected_Fund_Size] [numeric](18, 2) NULL,
	[Residual_Proportion] [float] NULL,
	[Frequency_of_investment_ID] [int] NOT NULL FOREIGN KEY REFERENCES [Customer].[DimInvestmentFreqDetails](Frequency_of_Investment_ID),
	[Portfolio_Driver] [varchar](10) NULL,
	[Risk_Profile_ID] [int] NOT NULL FOREIGN KEY REFERENCES [Customer].[DimRiskProfileDetails](Risk_Profile_ID),
	[Return_Profile_ID] [int] NOT NULL FOREIGN KEY REFERENCES [Customer].[DimReturnProfileDetails](Return_Profile_ID),
	[Strategy_ID] [int] NOT NULL FOREIGN KEY REFERENCES [Customer].[DimStrategyDetails](Strategy_ID),
	[Date_Updated] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[Record_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [Customer].[DimInvestmentFreqDetails](
	[Frequency_of_Investment_ID] [int] NOT NULL,
	[Frequency_of_Investment] [varchar](500) NULL,
PRIMARY KEY CLUSTERED 
(
	[Frequency_of_Investment_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


CREATE TABLE [Customer].[DimOccupationDetails](
	[Occupation_ID] [int] NOT NULL,
	[Occupation] [varchar](500) NULL,
PRIMARY KEY CLUSTERED 
(
	[Occupation_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [Customer].[DimReturnProfileDetails](
	[Return_Profile_ID] [int] NOT NULL,
	[Return_Profile] [varchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[Return_Profile_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [Customer].[DimRiskProfileDetails](
	[Risk_Profile_ID] [int] NOT NULL,
	[Risk_Profile] [varchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[Risk_Profile_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [Customer].[DimStateDetails](
	[State_ID] [int] NOT NULL,
	[State] [varchar](5) NULL,
PRIMARY KEY CLUSTERED 
(
	[State_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


CREATE TABLE [Customer].[DimStrategyDetails](
	[Strategy_ID] [int] NOT NULL,
	[Strategy_Description] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[Strategy_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


