y = 1
print("Please guess a number between 1 and 10")
while {y<=9}:
   i = int(input("Your guess is: "))
   if i==10:
       print("Congrats, You won! You chose the right answer")
       break

   if i<10:
       print("The number is bigger than this Try again")

   if i>9:
       print("The number is smaller than this Try again")

