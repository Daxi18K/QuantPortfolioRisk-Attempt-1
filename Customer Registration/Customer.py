class Customer:
    
    def __init__(self, DOB: str,
                 State: str,
                 Occupation: str,
                 investmentExp: int,
                 expectedFundSize: float,
                 residualProportion: float,
                 freqOfInvestment: str,
                 portfolioDriver: str,
                 riskProfile: str,
                 returnProfile: str,):
        assert State != ''                                  # State should not blank
        assert Occupation != ''
        assert investmentExp >= 0
        assert expectedFundSize > 0
        assert residualProportion > 0.0
        assert freqOfInvestment != ''
        assert portfolioDriver != ''
        assert riskProfile != ''
        assert returnProfile != ''
        
        #assign to self objects
        self.State = State
        self.Occupation = Occupation
        self.investmentExp = investmentExp
        self.expectedFundSize = expectedFundSize
        self.residualProportion = residualProportion
        self.freqOfInvestment = freqOfInvestment
        self.portfolioDriver = portfolioDriver
        self.riskProfile = riskProfile
        self.returnProfile = returnProfile
        
        # Get a number from the sequence and retain it for the registration purpose.
        # But this number should only go for new registration.
        # Any modification to existing customer or their respective details will be done via calling individual child class.
        
        
        
        
## Ideas for the input required for customer registration
## Customer ID (auto-generated)
## 