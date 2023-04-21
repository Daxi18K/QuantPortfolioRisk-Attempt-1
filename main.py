# This file will call all the class variables and will run the basics of the code
# Commiting in hopes that this file will be seen on the server


  
# Insert the path of modules folder 



from Utility.Utility import Base, session
from Customer_Registration.Customer import Registration
import sys
from datetime import date

date_time = date.today()
print(date_time)

sys.path.insert(0, r'C:\Users\dashrimali\Quant Risk Management Course\QuantPortfolioRisk-Attempt-1')

cust1 = Registration(recordId=112233,customerId=123123, dob=date(1992,3,18),state='NSW',occupation='Consultant',investmentExperience=4,dateUpdated=date_time)
session.add(cust1)

cust2 = Registration(recordId=223344,customerId=123123, dob=date(1994,4,18),state='QLD',occupation='Engineer',investmentExperience=1,dateUpdated=date_time)
session.add(cust2)

cust3 = Registration(recordId=334455,customerId=123123, dob=date(1993,1,22),state='SA',occupation='Financial Advisor',investmentExperience=10,dateUpdated=date_time)
session.add(cust3)

try:
    session.commit()
except:
    print("Commit Error Encountered")
    session.rollback()


session.close()

#try:
#    session.commit()
#    print('Session Commit Tested')
#except:
#    session.rollback()
#    print('Session rolled Back due to error')
    




