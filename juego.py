import random;

print ("Guess a number bewteen 1 and 10")
RandomNum = random.randint(1,10)
UserNumber = 0
while UserNumber != RandomNum:
 UserNumber = int(input("Guess the number\n"))
 print("You tipe",UserNumber)
 if(RandomNum < UserNumber):
  print("The number is minor")
 if(RandomNum > UserNumber):
  print("The number is bigger")
 elif(UserNumber == RandomNum):
  print("You guess the number xd")
