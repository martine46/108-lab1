def say_hello():
    print("Hello from method")

def sum(op1, op2):
    x = op1 + op2
    return x

def dif(op1, op2):
    x = op1 - op2
    return x

def mul(op1, op2):
    x = op1 * op2
    return x

def div(op1, op2):
    x = op1 // op2
    return x

def menu():
    print("       Menu ")
    print("[1] -  Add")
    print("[2] -  Subtract")
    print("[3] -  Multiply")
    print("[4] -  Divide")
    print("[x]  -  EXIT")

print('-' * 25)
print('Welcome to PyCalc')
print("-" * 25)


opc = ""
while (opc != "x"):
    menu()
    opc = input("Select an option:" )
    if(opc == "x"):
        break

    num1 = float(input("First No. : "))
    num2 = float(input("Second No. : "))

    if(opc == '1'):
        sum_res = sum(num1, num2)
        print("Sum = " + str(sum_res))

    if(opc == "2"):
        dif_res = dif(num1, num2)
        print("Difference = " + str(dif_res))

    if(opc == "3"):
        mul_res = mul(num1, num2)
        print("Multiplication = " + str(mul_res))

    if(opc == '4'):
        div_res = div(num1, num2)
        print("Quotient " + str(div_res))

    input("Press Enter to go back")