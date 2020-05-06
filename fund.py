f_amount=[]
f_donar=[]
# assuming 1 is comand dor data entry, 2 for retrive any data and '3' for exit the system.
print("enter '1' for data entry and '2' for retrive any data and '3' for exit ")
#Also at one time we can do only one transaction.
while(1):
    print("enter the command value")
    a=int(input())
    if(a==1):
        f_donar.append(input("enter the donar name :"))
        f_amount.append(int(input("amount donated :")))
        print("Unique ID is :",(len(f_amount)-1))
    elif(a==2):
        print("enter the Unque ID the retrive your transaction data:")
        b=int(input())
        if (b<len(f_amount)):
            print("NAME:",f_donar[b])
            print("AMOUNT:",f_amount[b])
        else:
            print("entered ID is does not exist")
    else:
        break
                

