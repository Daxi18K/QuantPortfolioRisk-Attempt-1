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


class StateDetails(Base):
        
    def __init__(self,
                 Id: int,
                 state: str
                 ):
                
        self.Id = Id
        self.state = state
    
    __tablename__ = "DimStateDetails"
    __table_args__ = {"schema":"Customer","extend_existing": True}

    Id = Column('State_ID',Integer, primary_key=True)
    state = Column("State",String)
    #stateRelationship = relationship('Registration', backref='DimStateDetails')
    stateRelationship = relationship('Registration', backref='author')
    
    

class FreqofInvestmentDetails(Base):
        
    def __init__(self,
                 Id: int,
                 freqOfInvestment: str
                 ):
                
        self.Id = Id
        self.freqOfInvestment = freqOfInvestment
    
    __tablename__ = "DimInvestmentFreqDetails"
    __table_args__ = {"schema":"Customer","extend_existing": True}

    Id = Column('Frequency_of_Investment_ID',Integer, primary_key=True)
    freqOfInvestment = Column("Frequency_of_Investment",String)
    #stateRelationship = relationship('Registration', backref='DimStateDetails')
    freqOfInvestRelationship = relationship('Registration', backref='author')
 
          
class OccupationDetails(Base):
        
    def __init__(self,
                 Id: int,
                 Occupation: str
                 ):
                
        self.Id = Id
        self.Occupation = Occupation
    
    __tablename__ = "DimOccupationDetails"
    

    Id = Column('Occupation_ID',Integer, primary_key=True)
    Occupation = Column("Occupation",String)
    occupationRelationship = relationship('Registration', backref='DimOccupationDetails')
    
    __table_args__ = {"schema":"Customer","extend_existing": True}       

    
class ReturnProfileDetails(Base):
        
    def __init__(self,
                 Id: int,
                 returnProfile: str
                 ):
                
        self.Id = Id
        self.returnProfile = returnProfile
    
    __tablename__ = "DimReturnProfileDetails"
    

    Id = Column('Return_Profile_ID',Integer, primary_key=True)
    returnProfile = Column("Return_Profile",String)
    returnProfileRelationship = relationship('Registration', backref='DimReturnProfileDetails')
    
    __table_args__ = {"schema":"Customer","extend_existing": True} 


class RiskProfileDetails(Base):
        
    def __init__(self,
                 Id: int,
                 riskProfile: str
                 ):
                
        self.Id = Id
        self.riskProfile = riskProfile
    
    __tablename__ = "DimRiskProfileDetails"
    

    Id = Column('Risk_Profile_ID',Integer, primary_key=True)
    riskProfile = Column("Risk_Profile",String)
    riskProfileRelationship = relationship('Registration', backref='DimRiskProfileDetails')
    
    __table_args__ = {"schema":"Customer","extend_existing": True} 
    
 
 
class StrategyDetails(Base):
        
    def __init__(self,
                 Id: int,
                 strategyDescription: str
                 ):
                
        self.Id = Id
        self.strategyDescription = strategyDescription
    
    __tablename__ = "DimStrategyDetails"
    

    Id = Column('Strategy_ID',Integer, primary_key=True)
    strategyDescription = Column("Strategy_Description",String)
    strategyRelationship = relationship('Registration', backref='DimStrategyDetails')
    
    __table_args__ = {"schema":"Customer","extend_existing": True}        
        

class Registration(StrategyDetails, RiskProfileDetails, ReturnProfileDetails, OccupationDetails, FreqofInvestmentDetails,StateDetails):
        
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 dob: Date,
                 State_ID: int,
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
        assert State_ID >= 0
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
        self.State_ID = State_ID
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
    __table_args__ = {"schema":"Customer","extend_existing": True}
    
        
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    dob = Column("Date_of_Birth", Date)
    State_ID = Column(Integer, ForeignKey('DimStateDetails.State_ID'))
    #stateRelationship = relationship('StateDetails', backref='FactCustomerDetails')
    occupationId = Column(Integer, ForeignKey('DimOccupationDetails.Occupation_ID'))
    #occupationRelationship = relationship('OccupationDetails', backref = 'FactCustomerDetails')
    investmentExperience = Column("Investment_Exp",Integer)
    expectedFundSize = Column("Expected_Fund_Size", Numeric)
    investmentProportion = Column("Residual_Proportion", Numeric)
    frequencyOfInvestmentId = Column(Integer, ForeignKey('DimInvestmentFreqDetails.Frequency_of_Investment_ID'))
    #frequencyOfInvestment = relationship('DimInvestmentFreqDetails', backref='freq_of_investment')
    portfolioDriver = Column("Portfolio_Driver", String)
    riskProfileId = Column(Integer, ForeignKey('DimRiskProfileDetails.Risk_Profile_ID'))
    #riskProfileRelationship = relationship('RiskProfileDetails', backref='FactCustomerDetails')
    returnProfileId = Column(Integer, ForeignKey('DimReturnProfileDetails.Return_Profile_ID'))
    #returnProfileRelationship = relationship('ReturnProfileDetails', backref='FactCustomerDetails')
    strategyId = Column(Integer, ForeignKey('DimStrategyDetails.Strategy_ID'))
    #strategyRelationship = relationship('StrategyDetails', backref='FactCustomerDetails')
    dateUpdated = Column("Date_Updated", DateTime)
    
