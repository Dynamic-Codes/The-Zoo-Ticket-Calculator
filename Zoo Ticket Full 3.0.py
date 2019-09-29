#Delay Instructions
import time

#Price Variable
tic1price=25.00
tic2price=15.00
tic3price=0.50
tic4price=0.00
tic5price=10.00

#discount Variable
discount=0.00

#Admin Console Usage
ConsoleStatus='Console Not Used'
SCLtext=''


print("Welcome to the Zoo Ticket calculator")
print("")
time.sleep(1)
print("Here are the prices:")
print("--------------------")
print("Adult:    £25.00")  #tic1
print("Child:    £15.00")  #tic2
print("Under 3:  £0.50")   #tic3
print("")
print("---SPECIAL PASS---")
print("Staff:    £0.00")   #tic4
print("Disabled: £10.00")  #tic5 
print("--------------------")
print("")
time.sleep(3)
tic1=int(input("How many Adults:     "))
tic2=int(input("How many Children:   "))
tic3=int(input("How many Under 3s:   "))
tic4=int(input("How many Staff:      "))
tic5=int(input("How many Disabled:   "))
currentprice=tic1*tic1price+tic2*tic2price+tic3*tic3price+tic4*tic4price+tic5*tic5price
print("Your current price is £",currentprice)
dis=input("Enter Discount Code: ")
if dis=='5Animals':
    print("Code Accepted!")
    discount=-5.00
elif dis=='Halloween19':
    print("Code Accepted!")
    discount=-9.00
elif dis=='School2019' and tic2>30:
    print("Code Accepted!")
    discount=-500.00
elif dis=='School2019' and tic2<30:
    print("Error: Requires 30+ Childern to use!")
    if tic2>10:
        time.sleep(1)
        print("Added mini school trip discount!")
        discount=-250.00
    else:
        print("No Code found!")
elif dis=='Python2Code':
    print("")
    print("          --||Admin Console||--")
    print("")
    print("*Sensitive Area! Only to be used by professionals.")
    print("")
    discount=int(input("Price Changer: "))
    SCLtext=input("Type in Special Text: ")
    ConsoleStatus='Admin Console has been used!'
else:
    print("No Code found!")
print("")
print("Please wait while we calculate your total.")
time.sleep(2)
totalprice=tic1*tic1price+tic2*tic2price+tic3*tic3price+tic4*tic4price+tic5*tic5price+discount
if totalprice==0.00 and tic4>0:
    print("You Have a free entry as you are a Staff Member")
elif totalprice>0.50:
    print("Your total price is £",totalprice)
elif tic3>0.49 and tic1==0 and tic2==0 and tic4==0 and tic5==0:
    print("Your Under 3 Must be accompanied by an Adult!")#No staff with under 3
elif tic3>0 and tic4>0 and tic1==0 and tic2==0 and tic5==0:
    print("Your Under 3 has been selected to be accompanied by a Staff Memeber.")#Under 3 with staff
else:
    print("There was an error while processing your total...")
print("")
print("Console Zone")
print("------------")
print(SCLtext)
print(ConsoleStatus)

