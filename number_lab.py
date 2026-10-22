
def positiveNegativeCheck(num):
      if num < 0:
            print(f"{num} is a negative number")
            print("\n")
      elif num > 0:
            print(f"{num} is a positive number")
            print("\n")
      else:
            print(f"{num} is zero number")

def positiveNegativeHub():
      while True:
            print("\n")
            print("Welcome to Negative and Positive number checker! ")
            i = input("Input any number or type Exit to exit : ")
            if i == "Exit":
                  break
            elif i != "Exit":
                num = int(i)
                positiveNegativeCheck(num)
                  

#OddEvenChecker
def oddEvenCheck(num):
      if num % 2 == 0:
            print(f"{num} is an even number")
            print("\n")
            return
      else:
            print(f"{num} is an odd number")
            print("\n")
            return

def oddEvenHub():
      while True:
            print("\n")
            print("Welcome to Odd & Even Checker")
            i = int(input("Input any number or 0 to exit : "))
            if i:
                  oddEvenCheck(i)
            elif i == 0:
                  break;
                  

def main():
      while True:
            print("Number Lab")
            print("\n")
            print("1. Odd or even ")
            print("2. Positive or negative ")
            print("0. Exit")
            i = int(input("Input the number of option : "))
            if i == 0:
                  break
            elif i == 1:
                  oddEvenHub()
            elif i == 2:
                  positiveNegativeHub()

main()