
#1. Create a Python program that prompts the user to enter their age. 
# If the age is less than 18, print "You are a minor." If the age is 
# between 18 and 60, print "You are an adult." For ages over 60, print 
# "You are a senior citizen." The program should continue until the user 
# inputs "stop."
   
while True:
    age = int(input("enter your age: "))

    if age < 18:
        print("you are a minor")
    elif 18 <= age <= 60:
        print("you are an adult")
    else: 
        print("you are a senior citizen")

    stop = input("do you want to stop? yes/no: ")
    if stop.lower() == "stop":
        break
    
#2. Write a Python program that simulates waiting for a 
# specific vehicle, such as a "bus". The program should 
# repeatedly prompt the user to input the name of a vehicle. 
# If the input is not "bus", the program should print 
# "waiting" and continue. Once the user inputs "bus", the 
# program should print "finally the wait is over" and terminate the loop.

while True:
    vec=input("enter the vehicle name: ")
    if vec.lower()!="bus":
        print("waiting")
    else:
        print("dinnaly  the wait is over")
        break
   
   
# 3. Write a Python program that continuously prompts the user 
# to input a fruit name. If the input is "apple," the program 
# should print "You got it!" and stop. Otherwise, it should 
# display "Try again" and continue. 

while True:
    fruit=input("enter fruit nanme")
    if fruit.lower()=="apple":
        print("you got it")
        break
    else:
        print("try again")
        
# 4. Create a Python program that asks the user to guess the password.
#  The program should keep asking until the user enters "open sesame."
#  For each incorrect guess, print "Wrong password, try again." 
# When the correct password is entered, print "Access granted!"

while True:
    password=input("enter a pass")
    if password.lower()!="open sesame":
        print("wrong pass try again")
    else:
        print("access granted")
        break        

# 5. Generate a frequency table for the ratings list which is initialized below.
# Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
#     a.	Start by creating an empty dictionary named content_ratings
#     b.	Loop through the ratings list. For each iteration, complete the following:
#         If the rating is already in content_ratings then increment the frequency of that rating by 1.
#         Else, initialize the rating with a value of 1 inside the content_ratings dictionary.

ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
content_ratings ={}
i = 0
# for rating in ratings:
#     if rating in content_ratings:
#         content_ratings[rating] += 1
#     else:
#         content_ratings[rating] = 1
# print(content_ratings) 

# while i < len(ratings):
#     rating = ratings[i]
#     if rating in content_ratings:
#         content_ratings[rating] += 1
#     else:
#         content_ratings[rating] = 1
#     i += 1
# print(content_ratings)

while True:
    if i>=len(ratings):
        break
    rating = ratings[i]
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
    i+=1
print(content_ratings)

# 6. Write a Python program that generates a random number 
# between 1 and 10 and prompts the user to guess the number. 
# The program should provide hints such as "guess higher" or 
# "guess lower" based on the user's input. Once the user guesses
# the correct number, the program should display the number of 
# attempts it took to guess the correct number.

import random
num=random.randint(1,10)
guess=None
attemps=0
while True:
  guess=int(input("guess a number between 1 and 10"))
      atemps=1+attemps

  if guess<num:
      print("guess higher")
  elif guess>num:
      print("guess lower")
  else:
    print(f"congratulations you guessed right {atemps} attempts")
    break

# 7. Write a Python program that simulates a login system. The program 
# should prompt the user to enter a username and password. If both are 
# correct (e.g., username is "admin" and password is "1234"), 
# print "Login successful" and exit(mean break use garne program enf garna ko lagi). If either is incorrect, 
# print "Invalid credentials, try again." Allow the user up to 
# 3 attempts before locking them out with the message "Too many failed attempts."

corrcet_username = "admin"
correct_paas="1234"
max_attemo=3
atempt=0
while True:
    username=input("enter a username:")
    password=input("enter a password: ")
    atempt=atempt+1
    if username==corrcet_username and password==correct_paas:
        print("login scuess")
        break 
    else:
        if atempt==max_attemo:
            print("too many failed attemps")
            break
        else:
            print(f"invalid credentails try again {max_attemo-atempt} attemps left")
            

# 8. Write a Python program that simulates a basic arithmetic quiz. 
# Generate two random numbers between 1 and 30 and ask the user to 
# provide the result of their multiplication. If the answer is correct, 
# print "Correct!" and generate a new question. If the answer is wrong, 
# print "Incorrect, try again." Allow the user to stop the quiz when the 
# user enters "exit"   

import random
while True:
    ques1 = random.randint(1, 30)
    ques2 = random.randint(1, 30)

    guess = input(f"{ques1} * {ques2} = ")

    if guess.lower() == "exit":
        print("Quiz ended.")
        break

    if int(guess) == ques1 * ques2:
        print("Correct!")
    else:
        print("Incorrect, try again.")


# 9. Write a Python program that prompts the user to enter a number. 
# The program should determine whether the number is prime or not. 
# If the number is prime, print "The number is prime." Otherwise, print
#  "The number is not prime." Continue prompting the user until they enter "exit."
 
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")  
    if user_input.lower() == "exit":
        print("Program terminated.")
        break 
    num = int(user_input) 
    if num < 2:
        print("The number is not prime.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("The number is not prime.")
                break
        else:  
            print("The number is prime.")

# 10. Write a Python program that asks the user to guess a pre-defined secret
#  word (e.g., "python"). Provide feedback like "Incorrect, try again" if the 
# guess is wrong. When the user guesses correctly, print "Congratulations, you
#  guessed the word!" Allow the user to exit the program by typing "quit."

sec_word="python"
attempts=0 
while True:
    guess=input("guess the secret word: ")
    attempts+=1
    if guess.lower()=="quit":
        print("program exicted")
        break
    if guess.lower()==sec_word:
        print(f"congratulations you guessed the word in {attempts} attempts")
        break
    else:
        print("incorrect try again")
        
# 11. Write a Python program that prompts the user to repeatedly enter a name. 
# If the user enters the phrase "good luck," the program keeps track of how many 
# times the phrase has been entered. When the phrase has been entered three times, 
# the program should display a message stating "You typed good luck three times." 
# For each entry of "good luck" before the third occurrence, display the message 
# "You typed the same word [count] times." Continue this process until the phrase 
# has been entered three times. 

count = 0
while True:
    name=input("Enter a name: ")
    if name.lower()=="good luck":
        count = count + 1
        if count < 3:
            print(f"You typed the same word {count} times.")
        else:
            print("You typed good luck three times.")
            break

# 12. Write a Python program that simulates a basic elevator system. The program should keep track of the elevator's current position and allow a user to travel to different floors until they choose to exit.
# Requirements
# a.	Starting State: The elevator should start on floor 1.
# b.	Continuous Loop: Use a while loop to repeatedly ask the user for a destination floor.
# c.	Input Handling: If the user enters 0, the program should print a goodbye message and terminate. If the user enters something that isn't a number, handle the error gracefully so the program doesn't crash.
# d.	Logic: If the target floor is higher than the current floor, print a â€˜Going upâ€™ message. If the target floor is lower than the current floor, print a â€˜Going downâ€™ message. If the user is already on the requested floor, inform them of that. 
# e.	State Update: After "moving," update the current floor to the target floor so the next movement starts from the new location.

current_floor = 1  
while True:
    user_input = input("Enter the floor you want to go (0 to exit): ")
    if not user_input.isdigit():  
        print("Invalid input! Please enter a number.")
        continue
    target_floor = int(user_input)
    if target_floor == 0:
        print("Goodbye!")
        break
    if target_floor > current_floor:
        print("Going up")
    elif target_floor < current_floor:
        print("Going down")
    else:
        print("You are already on this floor")
    current_floor = target_floor


        
        
        
