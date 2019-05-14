#WAP to illustrate simple reflex agent
#problem to solve to give the loan to the bank customer
import sys

loan=int(input("Enter customer's loan amount"))
income=int(input("Enter the monthly income of the user"))
papers=(input("Is there any house or property papers(yes/no)").lower())
if(loan>500000):
    input("Reject Loan")
    sys.exit()
    
elif(income<15000):
    input("Reject Loan")
    sys.exit()
    
elif(papers!='yes'):
    input("Reject Loan")
    sys.exit()
    
else:
    print("Accept Loan")
