import random
a = int(input("enter your move(rock,paperor sissor):"))
print("your trun")
if a == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif a == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print(a)

print("computers trun")
b = random.randint(1, 3)
if b == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif b == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print(b)

while (True):
    if a == 1 and b == 1:
        print("try again. Its a draw")
        break
    elif a == 2 and b == 2:
        print("try again. Its a draw")
        break
    elif a == 3 and b == 3:
        print("try again. Its a draw")
        break
    elif a < b:
        print("try again you won")
        break
    else:
        print("Player A you won!!!")
        break
