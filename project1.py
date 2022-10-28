a=int(input("Enter year."))
if a % 4==0 or a % 400==0 and a % 100!=0:
    print("This is leap year.")
else:
    print("This is not leap year.")