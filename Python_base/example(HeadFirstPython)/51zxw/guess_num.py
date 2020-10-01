import random
answer = random.randint(1, 100)
n = int(input("Please input num(1-100):"))
while n != answer:
      if n > answer:
            n = int(input("Num is more, Please continue input num:"))
      if n < answer:
            n = int(input("Num is less, Please continue input num:"))
print("You win the game.")
      
