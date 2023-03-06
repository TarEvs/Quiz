print("Welcome to my computer quiz")
name = input("what is your name? ").capitalize()
playing = input("Do you want to play " + (name) + "? ")

if playing.lower() != "yes":
    quit()

print("ok, lets play :)")

score = 0
answer = input("What is my fav colour ? ")

if answer.lower() == "pink":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer")

answer = input("What colour is my computer? ")

if answer.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer")

answer = input("What make is my computer? ")

if answer.lower() == "lenovo":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer")

answer = input("what day is it? ")

if answer.lower() == "monday":
    print("Correct!")
    score += 1
else:
    print("Sorry, wrong answer")

if score <= 2:
    print("You got " + str(score) + " questions correct!!")
else:
    print("You got " + str(score) + " questions correct! Well Done! " + (name))
