import sys
  
# Insert the path of modules folder 
sys.path.insert(0, r'C:\Users\dashrimali\Quant Risk Management Course\QuantPortfolioRisk-Attempt-1')

from Utility.Utility import (Base,
                            PrimaryKeyConstraint,
                            ForeignKey,
                            Column,
                            String,
                            Integer,
                            CHAR,
                            Numeric,
                            Float,
                            Date,
                            DateTime,
                            relationship                            
)

class Registration(Base):
        
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 dob: Date,
                 stateId: int,
                 occupationId: int,
                 investmentExperience: int,
                 expectedFundSize: Numeric,
                 investmentProportion: float,
                 frequencyOfInvestmentId: int,
                 portfolioDriver: String,
                 riskProfileId: int,
                 returnProfileId: int,
                 strategyId: int,
                 dateUpdated: DateTime
                 ):
        
        assert recordId >= 0.0
        assert customerId >= 0.0
        assert dob != ''
        assert stateId >= 0
        assert occupationId >= 0
        assert investmentExperience >= 0
        assert expectedFundSize >= 0
        assert investmentProportion >= 0
        assert frequencyOfInvestmentId >= 0
        assert portfolioDriver != ''
        assert riskProfileId >= 0
        assert returnProfileId >= 0
        assert strategyId >= 0
        assert dateUpdated != ''
        
        self.recordId = recordId
        self.customeId = customerId
        self.dob = dob
        self.stateId = stateId
        self.occupationId = occupationId
        self.investmentExperience = investmentExperience
        self.expectedFundSize = expectedFundSize
        self.investmentProportion = investmentProportion
        self.frequencyOfInvestmentId = frequencyOfInvestmentId
        self.portfolioDriver = portfolioDriver
        self.riskProfileId = riskProfileId
        self.returnProfileId = returnProfileId
        self.strategyId = strategyId
        self.dateUpdated = dateUpdated
    
    
    __tablename__ = "FactCustomerDetails"
    
        
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    dob = Column("Date_of_Birth", Date)
    stateId = Column(Integer, ForeignKey('DimStateDetails.State_ID'))
    stateRelationship = relationship('DimStateDetails', backref='stateRelationship')
    occupationId = Column(Integer, ForeignKey('DimOccupationDetails.Occupation_ID'))
    occupation = relationship('DimOccupationDetails', backref = 'occupation_name')
    investmentExperience = Column("Investment_Exp",Integer)
    expectedFundSize = Column("Expected_Fund_Size", Numeric)
    investmentProportion = Column("Residual_Proportion", Numeric)
    frequencyOfInvestmentId = Column(Integer, ForeignKey('DimInvestmentFreqDetails.Frequency_of_Investment_ID'))
    frequencyOfInvestment = relationship('DimInvestmentFreqDetails', backref='freq_of_investment')
    portfolioDriver = Column("Portfolio_Driver", String)
    riskProfileId = Column(Integer, ForeignKey('DimRiskProfileDetails.Risk_Profile_ID'))
    riskProfile = relationship('DimRiskProfileDetails', backref='risk_profile')
    returnProfileId = Column(Integer, ForeignKey('DimReturnProfileDetails.Return_Profile_ID'))
    returnProfile = relationship('DimReturnProfileDetails', backref='return_profile')
    strategyId = Column(Integer, ForeignKey('DimStrategyDetails.Strategy_ID'))
    strategy = relationship('DimStrategyDetails', backref='strategy_name')
    dateUpdated = Column("Date_Updated", DateTime)
    
    __table_args__ = {"schema":"Customer","extend_existing": True}

        


class StateDetails(Base):
        
    def __init__(self,
                 stateId: int,
                 state: str
                 ):
                
        self.stateId = stateId
        self.state = state
    
    __tablename__ = "DimStateDetails"
    

    stateId = Column(Integer, ForeignKey('DimStateDetails.State_ID'))
    state = Column("State",String)
    stateRelationship = relationship('FactCustomerDetails', backref='stateRelationship')
    
    __table_args__ = {"schema":"Customer","extend_existing": True}

          
        

    

    

        
        
## Ideas for the input required for customer registration
## Customer ID (auto-generated)
## 