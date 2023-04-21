import sys
  
# Insert the path of modules folder 
sys.path.insert(0, r'C:\Users\dashrimali\Quant Risk Management Course\QuantPortfolioRisk-Attempt-1')

from Utility.Utility import Base, create_engine, PrimaryKeyConstraint, ForeignKey, Column, String, Integer, CHAR, Numeric, Float, Date, DateTime

class Registration(Base):
        
    def __init__(self,
                 recordId: int,
                 customerId: int,
                 dob: str,
                 state: str,
                 occupation: str,
                 investmentExperience: int,
                 dateUpdated
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
    __table_args__ = {'extend_existing': True}
    
    recordId = Column("Record_ID", Numeric, primary_key=True)
    customeId = Column("Customer_ID", Numeric)
    dob = Column("Date_of_Birth", Date)
    state = Column("State", String)
    occupation = Column("Occupation", String)
    investmentExperience = Column("Investment_Exp",String)
    dateUpdated = Column("Date_Updated", DateTime)

        # Get a number from the sequence and retain it for the registration purpose.
        # But this number should only go for new registration.
        # Any modification to existing customer or their respective details will be done via calling individual child class.
        
        
        
        
## Ideas for the input required for customer registration
## Customer ID (auto-generated)
## 