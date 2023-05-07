# This file will call all the class variables and will run the basics of the code
# Commiting in hopes that this file will be seen on the server


  
# Insert the path of modules folder 



from Utility.Utility import conn, sessionmaker
from Customer_Registration.Customer import (Registration)
import sys
from datetime import datetime
import pandas as pd


Session = sessionmaker(bind = conn, expire_on_commit=False)
session = Session()
print("Session Created")

date_time = datetime.now()
print(date_time)

sys.path.insert(0, r'C:\Users\dashrimali\Quant Risk Management Course\QuantPortfolioRisk-Attempt-1')

bulkDataset = pd.read_csv(r'C:\Users\dashrimali\Quant Risk Management Course\QuantPortfolioRisk-Attempt-1\Bulk_Input_Data\Bulk_Input_File.csv')

#Converting relevant columns to datetime
bulkDataset['dob'] = pd.to_datetime(bulkDataset['dob'])


for index, row in bulkDataset.iterrows():
    print(f'Running loop for index - {index}')
    
    cust1 = Registration(recordId=row['Record_ID'],
                         customerId=row['Customer_ID'],
                         dob=row['dob'],
                         State_ID=row['State_ID'],
                         occupationId=row['Occupation_ID'],
                         investmentExperience=row['Investment_Exp'],
                         expectedFundSize=row['Expected_Fund_Size'],
                         investmentProportion=row['Residual_Proportion'],
                         frequencyOfInvestmentId=row['Freq_of_Investment_ID'],
                         portfolioDriver=row['Portfolio_Driver'],
                         riskProfileId=row['Risk_Profile_ID'],
                         returnProfileId=row['Return_Profile_ID'],
                         strategyId=row['Stretegy_ID'],
                         dateUpdated=date_time)
    session.add(cust1)
    try:
        session.commit()
        session.flush()
    except:
        print("Commit Error Encountered for Registration")
        session.rollback()
        pass
    
session.close()

   




