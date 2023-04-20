# This file will call all the class variables and will run the basics of the code
# Commiting in hopes that this file will be seen on the server

import sys
  
# Insert the path of modules folder 
sys.path.insert(0, r'C:\Users\dashrimali\Quant Risk Management Course\QuantPortfolioRisk-Attempt-1')


from Utility.Utility import Base, session
from Customer_Registration.Customer import Registration

cust1 = Registration(123123,123456, '1992-03-18','NSW','Consultant',4, '')
print(cust1.customeId)
session.add(cust1)
try:
    session.commit()
except:
    session.rollback()



