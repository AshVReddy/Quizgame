print("Welcome to my computer quiz!")

playing = input("Enter your Name: ")
print("Hi", playing)

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Thank you for confirming! See you again :)")
    quit()

print("Okay Let's play :)")
score = 0

answer = input("How do you say Good Morning in German? ")
if answer.lower() == "Guten Morgen".lower():
    print("Correct! You can proceed with the second Question")
    score += 1
else:
    print("Incorrect!")

answer = input("How do you say Good Night in German? ")
if answer.lower() == "Gute Nacht".lower():
    print("Correct! You can proceed with the third Question")
    score += 1
else:
    print("Incorrect!")

answer = input("How do you say Good Evening in German? ")
if answer.lower() == "Guten Abend".lower():
    print("Correct! You can proceed with the fourth Question")
    score += 1
else:
    print("Incorrect!")

answer = input("How do you say cold in German? ").lower()
if answer.lower() == "Kalt".lower():
    print("Correct! You can proceed with the fifth Question")
    score += 1
else:
    print("Incorrect!")

answer = input("How do you say hot in German? ").lower()
if answer.lower() == "Heiß".lower():
    print("Correct! Thank you for participating in this Quiz game :)")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
