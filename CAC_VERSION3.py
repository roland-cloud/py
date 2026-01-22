
def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0 or x !=0:
        return x / y
    else:
        return "Error: We can not divide by Zero."

def main():
    print("""
        WELCOME TO THE CALCULATOR V.3
          """)
    while True:
        print("""
                Select operation:
                1. Add
                2. Subtract
                3. Multiply
                4. Divide
                """)
        choice = input("Enter choice: (1/2/3/4) ")
        
        if  choice in ("1", "2", "3", "4"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            
            if choice == "1":
                print("The sum of", num1, "+", num2, "is", add(num1, num2))
                
            elif choice == "2":
                print("The difference of", num1, "-", num2, "is", subtract(num1, num2))
                
            elif choice == "3":
                print("The product of", num1, "x", num2, "is", multiply(num1, num2))
                
            elif choice == "4":
                print("The division of", num1, "/", num2, "is", divide(num1, num2))
                
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != "yes":
                break

print(main())
                        
                        
                        
                    


