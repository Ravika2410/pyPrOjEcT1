a=int(input("Enter year."))
if a % 4==0 or a % 400==0 and a % 100!=0:
    print("This is leap year.")
else:
    print("This is not leap year.")
    
    b=int(input("Enter the height in centimeter."))
inches=0.394 
print(("The length in inches :",round(b*inches,2),"inches"))


c=int(input("Enter the height in centimeter."))
feet=0.0328 
print(("The length in feet :",round(c*feet,2),"feet"))
