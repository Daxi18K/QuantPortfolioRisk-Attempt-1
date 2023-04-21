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

cust2 = Registration(112233,123123, date(1992,3,18),'NSW','Consultant',4, date_time)
cust1 = Registration(123123,123456, date(1992,3,18),'NSW','Consultant',4, date_time)
print(cust1.customeId)
session.add(cust1)
session.commit()

session.rollback()

#try:
#    session.commit()
#    print('Session Commit Tested')
#except:
#    session.rollback()
#    print('Session rolled Back due to error')
    




