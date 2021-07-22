#Mood
#mood = input("What mood are you in today?")
#if mood == "happy":
 #   print("It is great to see you happy!")
#elif mood == "nervous":
 #   print("Take a deep breath 3 times")
#elif mood == "sad":
 #   print("It's going to be okay!")
#elif mood == "excited":
 #   print("What are you excited about?")
#elif mood == "relaxed":
 #   print("Zen :) ")
#else:
 #   print("I don't recognize this mood")

#Calculator
#num1 = int(input("Write the first number "))
#num2 = int(input("Write the second number "))
#operation = input("Which operation do you want to use? You can choose between +, -, * and /: ")

#if operation == "+":
 #   print(num1 + num2)
#elif operation == "-":
 #   print(num1 - num2)
#elif operation == "*":
 #   print(num1 * num2)
#else:
 #   print(num1 / num2)


#Guess the secret number - While loop
#secret = 49
#guess = 0
#while True:
 #   guess = int(input("Guess the secret number between 1 and 50: "))

  #  if guess == secret:
   #     print("You guessed the correct number - 49!")
    #    break
    #elif guess > secret:
     #   print("Your guess is incorrect, try something smaller")
    #elif guess < secret:
     #   print("Your guess is incorrect, try something bigger")

#Guess my age - For loop
#myAge = 21

#for x in range(5):
 #   attempt = int(input("Guess my age: "))

  #  if attempt == myAge:
   #     print("You've guessed my age - 21.")
    #    break
#else:
 #   print("Sorry, this is not my age.")

#Using a random number
import random
import json
import datetime

number = random.randint(1, 10)
attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date " + score_dict.get("date"))

while True:
    my_guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if my_guess == number:
        score_list.append({"attempts": attempts}, "date": str(datetime.datetime.now())})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it, it's number " + str(number))
        print("Attempts needed: " + str(attempts))
        break
    elif my_guess > number:
        print("Sorry, try something smaller")
    elif my_guess < number:
        print("Sorry, try something bigger")
