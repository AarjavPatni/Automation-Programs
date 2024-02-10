import random, time, math
from os import system, name

def game():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(100, 1000)
    d = random.randint(100, 1000)
    choice = input("\nEnter the number corresponding to the question you want:\n1. 2 x 2 digits\n2. 3 x 3 digits\n3. 2 x 3 digits\n4. 3 x 2 digits\n5. square roots\n6. cube roots\n7. squares\n8. cubes\n")
    choice = int(choice)
    clear()
    if choice == 1:
        start = time.time()
        print(f"\n{a} x {b} ? (Press enter to see the answer)", end = "")
        input(" ")
        end = time.time()
        elapsed = end - start
        round(elapsed, 2)
        print("Answer: ", a * b, ". That took you ", elapsed, " seconds.", sep = "", end = "\n\n")
    elif choice == 2:
        start = time.time()
        print(f"\n{c} x {d} ? (Press enter to see the answer)", end = "")
        input(" ")
        end = time.time()
        elapsed = end - start
        round(elapsed, 2)
        print("Answer: ", c * d, ". That took you ", elapsed, " seconds.", sep = "", end = "\n\n")
    elif choice == 3:
        start = time.time()
        print(f"\n{a} x {c} ? (Press enter to see the answer)", end = "")
        input(" ")
        end = time.time()
        elapsed = end - start
        round(elapsed, 2)
        print("Answer: ", a * c, ". That took you ", elapsed, " seconds.", sep = "", end = "\n\n")
    elif choice == 4:
        start = time.time()
        print(f"\n{d} x {b} ? (Press enter to see the answer)", end = "")
        input(" ")
        end = time.time()
        elapsed = end - start
        round(elapsed, 2)
        print("Answer: ", d * b, ". That took you ", elapsed, " seconds.", sep = "", end = "\n\n")
    elif choice == 5:
        while True:
            start = time.time()
            ques = random.randint(1, 10000)
            print(ques)
            ans = float(input("Enter the square root: "))
            end = time.time()
            elapsed = end - start
            if ans == math.sqrt(ques):
                print(f"Correct! That took you {elapsed} seconds.", end = "\n\n")
            else:
                print(f"Incorrect! The correct answer is {math.sqrt(ques)}", end = "\n\n")
    elif choice == 6:
        while True:
            start = time.time()
            ques = random.randint(1, 1000000)
            print(ques)
            ans = float(input("Enter the cube root: "))
            end = time.time()
            elapsed = end - start
            if ans == (round(ques ** (1/3), 2)):
                print(f"Correct! That took you {elapsed} seconds.", end = "\n\n")
            else:
                print(f"Incorrect! The correct answer is {round(ques ** (1/3))}", end = "\n\n")
    elif choice == 7:
        while True:
            start = time.time()
            ques = random.randint(1, 100)
            print(ques)
            ans = float(input("Enter the square: "))
            end = time.time()
            elapsed = end - start
            if ans == (ques ** 2):
                print(f"Correct! That took you {elapsed} seconds.", end = "\n\n")
            else:
                print(f"Incorrect! The correct answer is {ques ** 2}", end = "\n\n")
    elif choice == 8:
        while True:
            start = time.time()
            ques = random.randint(1, 100)
            print(ques)
            ans = float(input("Enter the cube: "))
            end = time.time()
            elapsed = end - start
            if ans == (ques ** 3):
                print(f"Correct! That took you {elapsed} seconds.", end = "\n\n")
            else:
                print(f"Incorrect! The correct answer is {ques ** 3}", end = "\n\n")
    else:
        print("Wrong choice!")

def clear():
    if name == 'nt':
        _ = system('cls')

try_again = "Y"
while(try_again == "y" or try_again == "Y"):
    try:
        game()
    except KeyboardInterrupt:
        try_again = input("\n\nDo you want to try again? (Y/N) ")