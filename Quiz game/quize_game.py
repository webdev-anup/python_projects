print("Welcome to the quiz game!")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :")

# Score counter initialize karein
score = 0

# Question 1
answer = input("What is the Financial capital of India? ")
if answer.lower() == "mumbai":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# print Score 
print("\n--- Game Over ---")
print("You got " + str(score) + " questions correct!")
print("You scored " + str((score / 4) * 100) + "%.")