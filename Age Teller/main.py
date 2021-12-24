import time
while True:
    print("Welcome to Maahir Age teller!")
    time.sleep(5)
    age = input("What is your age? ")
    final = 2021 - int(age)
    print(f"You were born in {final}")