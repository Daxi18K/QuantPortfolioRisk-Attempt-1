import sys
  
# Insert the path of modules folder 
sys.path.insert(0, r'C:\Users\dashrimali\Quant Risk Management Course\QuantPortfolioRisk-Attempt-1')

from Utility.Utility import Base, create_engine, PrimaryKeyConstraint, ForeignKey, Column, String, Integer, CHAR, Numeric, Float, Date, DateTime

class Registration(Base):
        
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 dob: Date,
                 state: str,
                 occupation: str,
                 investmentExperience: int,
                 dateUpdated: DateTime
                 ):
        
        assert recordId >= 0.0
        assert customerId >= 0.0
        assert dob != ''
        assert state != ''
        assert occupation != ''
        assert investmentExperience >= 0
        assert dateUpdated != ''
        
        self.recordId = recordId
        self.customeId = customerId
        self.dob = dob
        self.state = state
        self.occupation = occupation
        self.investmentExperience = investmentExperience
        self.dateUpdated = dateUpdated
    
    
    __tablename__ = "CustomerMaster"
    
        
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    dob = Column("Date_of_Birth", Date)
    state = Column("State", String)
    occupation = Column("Occupation", String)
    investmentExperience = Column("Investment_Exp",String)
    dateUpdated = Column("Date_Updated", DateTime)
    
    __table_args__ = {"schema":"Customer","extend_existing": True}

        
        
        
class customerFinancials:
    
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 expectedFundSize: float,
                 investmentProportion: float,
                 frequencyOfInvestment: str,
                 dateUpdated: DateTime
                 ):
        
        assert recordId >= 0.0
        assert customerId >= 0.0
        assert expectedFundSize >= 0
        assert investmentProportion >= 0.0
        assert frequencyOfInvestment != ''
        assert dateUpdated != ''
        
        self.recordID = recordId
        self.customerId = customerId
        self.expectedFundSize = expectedFundSize
        self.investmentProportion = investmentProportion
        self.frequencyOfInvestment = frequencyOfInvestment
        self.dateUpdated = dateUpdated
        
    __tablename__ = "CustomerFinancials"
        
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    expectedFundSize = Column("Expected_Fund_Size", Numeric)
    investmentProportion = Column("Investment_Prop",Float)
    frequencyOfInvestment = Column("Frequency_of_Investment", String)
    dateUpdated = Column("Date_Updated",DateTime)
        
    __table_args__ = {"schema":"Customer","extend_existing": True}
    

    
class customerPortfolioPreference:
    
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 portfolioDriver: String,
                 riskProfile: String,
                 returnProfile: String,
                 dateUpdated: DateTime
                 ):
        
        assert recordId >= 0.0
        assert customerId >= 0.0
        assert portfolioDriver != ''
        assert riskProfile != ''
        assert returnProfile != ''
        assert dateUpdated != ''
        
        self.recordId = recordId
        self.customerId = customerId
        self.portfolioDriver = portfolioDriver
        self.riskProfile = riskProfile
        self.returnProfile = returnProfile
        self.dateUpdated = dateUpdated
        
    __tablename__ = "CustomerPortfolioPreference"
    
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    portfolioDriver = Column("Portfolio_Driver", String)
    riskProfile = Column("Risk_Profile",String)
    returnProfile = Column("Return_Profile", String)
    dateUpdated = Column("Date_Updated",DateTime)
    
    __table_args__ = {"schema":"Customer","extend_existing": True}
    
class customerStrategyPreference:
    
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 strategyId: int,
                 dateUpdated: DateTime
                 ):
        
        assert recordId >= 0.0
        assert customerId >= 0.0
        assert strategyId >= 0
        assert dateUpdated != ''
        
        self.recordId = recordId
        self.customerId = customerId
        self.strategyId = strategyId
        self.dateUpdated = dateUpdated
        
    __tablename__ = "CustomerStrategyPreference"
    
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    strategyId = Column("Strategy_ID", Integer)
    dateUpdated = Column("Date_Updated",DateTime)
    
    __table_args__ = {"schema":"Customer","extend_existing": True}
    

class customerStockPreference:
    
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 etfName: String,
                 portfolioCategory: String,
                 dateUpdated: DateTime
                 ):
        
        assert recordId >= 0.0
        assert customerId >= 0.0
        assert etfName != ''
        assert portfolioCategory != ''
        assert dateUpdated != ''
        
    __tablename__ = 'CustomerStockPreference'
    
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    etfName = Column("ETF_Name",String)
    portfolioCategory = Column("Portfolio_Category", String)
    dateUpdated = Column("Date_Updated",DateTime)
        
    __table_args__ = {"schema":"Customer","extend_existing": True}
        
        
## Ideas for the input required for customer registration
## Customer ID (auto-generated)
## 