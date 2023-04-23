# This file will call all the class variables and will run the basics of the code
# Commiting in hopes that this file will be seen on the server


  
# Insert the path of modules folder 



from Utility.Utility import conn
from sqlalchemy.orm import sessionmaker
from Customer_Registration.Customer import Registration, customerFinancials, customerPortfolioPreference, customerStrategyPreference
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
    
    cust1 = Registration(recordId=row['Record_ID'],customerId=row['Customer_ID'], dob=row['dob'],state=row['State'],occupation=row['Occupation'],investmentExperience=row['Investment_Exp'],dateUpdated=date_time)
    session.add(cust1)
    try:
        session.commit()
        session.flush()
    except:
        print("Commit Error Encountered for Registration")
        session.rollback()
        pass
    
    fin1 = customerFinancials(recordId=row['Record_ID'],customerId=row['Customer_ID'],expectedFundSize=row['Expected_Fund_Size'],investmentProportion=row['Residual Proportion'],frequencyOfInvestment=row['Freq_of_Investment'],dateUpdated=date_time)
    session.add(fin1)
    try:
        session.commit()
        session.flush()
    except:
        print("Commit Error Encountered for Customer Financials")
        session.rollback()
        pass
    
    portPref1 = customerPortfolioPreference(recordId=row['Record_ID'],customerId=row['Customer_ID'],portfolioDriver=row['Portfolio_Driver'],riskProfile=row['Risk_Profile'],returnProfile=row['Return_Profile'],dateUpdated=date_time)
    session.add(portPref1)
    try:
        session.commit()
        session.flush()
    except:
        print("Commit Error Encountered for Customer Portfolio Preference")
        session.rollback()
        pass
    
    custStrgy1 = customerStrategyPreference(recordId=row['Record_ID'],customerId=row['Customer_ID'],strategyId=row['Stretegy_ID'],dateUpdated=date_time)
    session.add(custStrgy1) 
    try:
        session.commit()
        session.flush()
    except:
        print("Commit Error Encountered for Customer Stretegy")
        session.rollback()
        pass
    
session.close()

#try:
#    session.commit()
#    print('Session Commit Tested')
#except:
#    session.rollback()
#    print('Session rolled Back due to error')
    




