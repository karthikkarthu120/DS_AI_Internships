while(1):
    print("Simple Calculator")
    a = int(input("First Number: "))
    print("First Number :",a)
    b = int(input("Second Number: "))
    print("Second Number :",b)

    print("Addition :+ \n subtraction :- \n Division :/ \n Multiplication :* \n Modulus :% ")
    ch = input("Enter the Operation :")
    if ch=='+':
        print("Addition: ",a + b)
        
    elif ch=='-':
        print("Subtraction: ",a - b)
        
    elif ch=='/':
        print("Division: ",a / b)
        
    elif ch=='*':
        print("Multiplication: ",a * b)
        
    elif ch=='%':
         print("Modulus: ",a % b)
    else:
        print("Invalid choice")
        break
    
    
    
    
   
