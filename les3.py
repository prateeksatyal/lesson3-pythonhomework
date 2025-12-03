#1. Take 3 numbers and print the largest number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("The largest number is:", largest)


#2. Take a month number and print the month name
month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number")
    

#3.Write a program to swap two variables  
    
x = input("Enter first value: ")
y = input("Enter second value: ")
print("Before swapping: x =", x, "y =", y)
x, y = y, x
print("After swapping: x =", x, "y =", y)
    

#   4. You are developing a simple ticket booking system for a movie theatre. The ticket
# price depends on the age of the person and whether they have a membership card. If
# the person is under 12, the ticket is free. If the person is between 12 and 60: if they
# have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs 200. If the
# person is above 60, they get a senior citizen discount, and then ticket costs Rs 100.
# Write a python program using nested if-else to calculate and print the ticket price
# based on the users age and membership status.   

age = int(input("Enter your age: "))
has_membership = input("Do you have a membership card? (yes/no): ").lower()

if age < 12:
    print("Ticket is Free")  # or print(0)
elif 12 <= age <= 60:
    if has_membership == "yes":
        print("Ticket price is Rs. 150")
    else:
        print("Ticket price is Rs. 200")
else:
    print("Ticket price is Rs. 100")


# 5. A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
#  Next units: Rs 8
# If usage is > 300 units:
#  First 100: Rs 5
#  Next 200: Rs 8
#  Remaining: Rs 10

usage = int(input("Enter electricity usage in units: "))

if usage < 100:
    print("Total cost: Rs", usage * 5)
elif usage <= 300:
    first_100 = 100 * 5
    remaining = usage - 100
    print("Total cost: Rs", first_100 + remaining * 8)
else:
    first_100 = 100 * 5
    next_200 = 200 * 8
    remaining = usage - 300
    print("Total cost: Rs", first_100 + next_200 + remaining * 10)
    
# 6. Write a complete Python program that:
#  Asks Player 1 to enter their move ( input: rock, paper, or scissors)
#  Asks Player 2 to enter their move ( input: rock, paper, or scissors)
#  Uses only nested if and else statements
#  Prints who wins or if it's a tie

p1 = input("Player 1 move (rock/paper/scissors): ").lower()
p2 = input("Player 2 move (rock/paper/scissors): ").lower()

if p1 == p2:
    print("It's a tie")
elif p1 == "rock" and p2 == "scissors":
    print("Player 1 wins")
elif p1 == "paper" and p2 == "rock":
    print("Player 1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("Player 1 wins")
else:
    print("Player 2 wins")
    

#  7. A school decided to replace the desks in three classrooms. Each desk sits two
# students. Given the number of students in each class, print the smallest possible
# number of desks that can be purchased. The program should read three integers: the
# number of students in each of the three classes, a, b and c respectively.
# Hint: In the first test there are three groups. The first group has 20 students and thus
# needs 10 desks. The second group has 21 students, so they can get by with no fewer
# than 11 desks. 11 desks are also enough for the third group of 22 students. So, we
# need 32 desks in total.   

# Class haru ma student ko number halne
a = int(input("Class 1 ma students kati cha?: "))
b = int(input("Class 2 ma students kati cha?: "))
c = int(input("Class 3 ma students kati cha?: "))

# Harek class ka lagi desk haru calculate garne
# 2 ma divide garera odd cha vane 1 add garera round up garne
desks_a = (a + 1) // 2  # class 1 ko desk
desks_b = (b + 1) // 2  # class 2 ko desk
desks_c = (c + 1) // 2  # class 3 ko desk

# Sabai desks add garera total
total_desks = desks_a + desks_b + desks_c

# Result yoo
print("Minimum desks needed:", total_desks)


# 8. In a smart building lift system, the lift is currently at floor 5. A person presses
# floor 3. Write a program to decide and display whether the lift should go up, go
# down, or stay at current floor.

# Lift ahile kati floor ma cha bhanera
current_floor = 5

# User le kun floor press garxa bhanera input
pressed_floor = int(input("Tapaiko kun floor chahiyo?: "))

# Lift k garne decide garnu
if pressed_floor > current_floor:
    print("Lift upar janey cha")  # Up janey
elif pressed_floor < current_floor:
    print("Lift tala janey cha")  # Down janey
else:
    print("Lift ahile yo floor ma cha")  # Already yahi cha


# 9. Write a Python program that takes a number as input, first checks if it is positive
# if yes then check whether it is even or odd

num = int(input("Enter a number: "))

# Check positive ho ki hoina
if num > 0:
    # Number positive bhaye
    if num % 2 == 0:
        print("The number is even")   # even ho ki hoina check garne
    else:
        print("The number is odd")    # odd ho bhane
else:
    print("The number is not positive")   # positive chaina bhane
    

# 10. Take two numbers and find the greater of the two. If they are equal, check if the
# number is positive, negative, or zero.    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compare garne
if num1 > num2:
    print("The greater number is", num1)   # num1 greater bhaye p
elif num2 > num1:
    print("The greater number is", num2)   # num2 greater bhaye p
else:
    # Duita number equal cha bhane
    print("Both numbers are equal")
    if num1 > 0:
        print("The number is positive")   # positive check
    elif num1 < 0:
        print("The number is negative")   # negative check
    else:
        print("The number is zero")       # zero bhaye
        

# 11. Accept input from user If given number is a multiple of both 3 and 5 prints "Fizz
# Buzz" instead of number If given number is a multiple of 3 but not 5 prints "Fizz"
# instead of number If given number is a multiple of 5 but not 3 prints "Buzz"instead
# of number If given number is not multiple of 3 or 5 prints value as usual.
  
num = int(input("Enter a number: "))

# Check multiple of 3 and 5
 if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")   # 3 ra 5 le divide garxa bhane
 elif num % 3 == 0:
    print("Fizz")       # 3 le divide garxa bhane
 elif num % 5 == 0:
    print("Buzz")       # 5 le divide garxa bhane
 else:
    print(num)          # Kunai ni divide gardaina bhane number print garne      
    

# 12. Snapple is a famous tea drink brand from Queens, New York. Each bottle cap
# comes with a silly fun fact.
# Use the random module to create a number from 0 to 5. Then use
# an if/elif/else statement to print out one of these six random Snapple facts:
# 0 - 'Flamingos turn pink from eating shrimp.'
# 1 - 'The only food that doesn't spoil is honey.'
# 2 - 'Shrimp can only swim backwards.'
# 3 - 'A taste bud's life span is about 10 days.'
# 4 - 'It is impossible to sneeze while sleeping.'
# 5 - 'It is illegal to sing off-key in North Carolina.'

import random  # random module import garne

# Random number 0 dekhi 5 samma generate garxa
num = random.randint(0, 5)

# Check number ra corresponding Snapple fact print garxa
if num == 0:
    print("Flamingos turn pink from eating shrimp.")
elif num == 1:
    print("The only food that doesn't spoil is honey.")
elif num == 2:
    print("Shrimp can only swim backwards.")
elif num == 3:
    print("A taste bud's life span is about 10 days.")
elif num == 4:
    print("It is impossible to sneeze while sleeping.")
else:
    print("It is illegal to sing off-key in North Carolina.")
    

# 13. A store gives a 20% discount if the total purchase is above RS 1000 AND the
# customer is a member, or a 10% discount if the purchase is above RS 1000 but the
# customer is not a member. Write a program that takes total_amount and
# is_member (True/False) as input and prints the final amount after applying the
# correct discount (or no discount).
    
# User le total purchase amount halne
total_amount = float(input("Enter total purchase amount: "))

# User le member ho ki hoina halne (True/False)
is_member = input("Are you a member? (True/False): ").title() == "True"

# Check discount
if total_amount > 1000 and is_member:
    # Purchase >1000 ra member ho bhane 20% discount
    final_amount = total_amount * 0.8
elif total_amount > 1000 and not is_member:
    # Purchase >1000 ra member hoina bhane 10% discount
    final_amount = total_amount * 0.9
else:
    # Discount lagdaina
    final_amount = total_amount

# Print final amount
print("Final amount to pay:", final_amount)


#14: Weight conversion to other planet

# User le Earth weight halne
earth_weight = float(input("Enter your Earth weight (kg): "))

# User le planet number halne
planet = int(input("Enter planet number (1-7): "))

# Calculate weight based on planet
if planet == 1:
    weight = earth_weight * 0.38   # Mercury
elif planet == 2:
    weight = earth_weight * 0.91   # Venus
elif planet == 3:
    weight = earth_weight * 0.38   # Mars
elif planet == 4:
    weight = earth_weight * 2.53   # Jupiter
elif planet == 5:
    weight = earth_weight * 1.07   # Saturn
elif planet == 6:
    weight = earth_weight * 0.89   # Uranus
elif planet == 7:
    weight = earth_weight * 1.14   # Neptune
else:
    weight = None                   # Invalid planet

# Print result
if weight is not None:
    print("Your weight on planet", planet, "is:", weight)
else:
    print("Invalid planet number")
     

#15. WAP which accepts marks of four subjects and display total marks, percentage and
# grade. Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –>
# pass, less than 40 –> fail  

  
# User le char subject ko marks halne
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))

# Total marks calculate garnu
total = sub1 + sub2 + sub3 + sub4

# Percentage calculate garnu (assuming each subject max 100)
percentage = (total / 400) * 100

# Grade determine garnu
if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

# Print results
print("Total marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)  

# 16. Write a program to accept the cost price of a bike and display the road tax to be
# paid according to the following criteria:
# Cost price (in Rs) Tax
# >100000 15%
# >50000 and <=100000 10%
# <=50000 5%

# User le bike ko cost price halne
cost_price = float(input("Enter the cost price of the bike (Rs): "))

# Road tax calculate garnu
if cost_price > 100000:
    tax = cost_price * 0.15   # 15% tax
elif cost_price > 50000:
    tax = cost_price * 0.10   # 10% tax
else:
    tax = cost_price * 0.05   # 5% tax

# Print result
print("Road tax to be paid: Rs", tax)


# 17. A company decided to give bonus to employee according to following criteria:
# Time period of service Bonus
# More than 10 years 10%
# >=6 and <=10 8%
# Less than 6 years 5%

# User le service period halne (years)
service_years = float(input("Enter your years of service: "))

# Bonus calculate garnu
if service_years > 10:
    bonus = 0.10   # 10% bonus
elif service_years >= 6:
    bonus = 0.08   # 8% bonus
else:
    bonus = 0.05   # 5% bonus

# Print result
print("Your bonus percentage is:", bonus * 100, "%")


# 18. Ask the user for a subject score. If it's above 90, congratulate him. If it's between
# 50 and 90, suggest improvement. Otherwise, advise on retaking the course.

# User le subject score halne
score = float(input("Enter your subject score: "))

# Check score and give advice
if score > 90:
    print("Congratulations! Excellent score.")  # 90+ bhaye
elif score >= 50:
    print("Good effort, but you should improve.")  # 50–90 bhaye
else:
    print("You should retake the course.")  # <50 bhaye
    

# 19. Write a program to determine if a candidate is eligible for a job: If the candidate's
# age is >= 18, check if they have a degree. If they have a degree, check their work
# experience: More than 3 years: Display "Highly Eligible." 1-3 years: Display
# "Eligible." Less than 1 year: Display "Under Review."

# User le candidate ko age halne
age = int(input("Enter candidate's age: "))

# User le degree cha ki chaina halne (Yes/No)
has_degree = input("Do you have a degree? (Yes/No): ").title() == "Yes"

# User le work experience halne (years)
experience = float(input("Enter work experience in years: "))

# Eligibility check
if age >= 18:
    if has_degree:
        if experience > 3:
            print("Highly Eligible")   # 3+ years experience
        elif experience >= 1:
            print("Eligible")          # 1–3 years experience
        else:
            print("Under Review")      # <1 year experience
    else:
        print("Not Eligible")           # degree chaina
else:
    print("Not Eligible")               # age <18
    
    
# 20. Accept the age, gender ('M', 'F'), number of days and display the wages
# accordingly.
# Age Gender Wage/day
# >=18 and <30 M 700
# F 750
# >=30 and <=40 M 800
# F 850   


# User le age, gender, number of days halne
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days worked: "))

# Wage per day determine garnu
if age >= 18 and age < 30:
    if gender == "M":
        wage_per_day = 700
    else:  # gender F
        wage_per_day = 750
elif age >= 30 and age <= 40:
    if gender == "M":
        wage_per_day = 800
    else:  # gender F
        wage_per_day = 850
else:
    wage_per_day = 0  # age criteria match nagare

# Total wages calculate garnu
total_wages = wage_per_day * days

# Print result
if wage_per_day > 0:
    print("Total wages to pay: Rs", total_wages)
else:
    print("No wages, age not in valid range") 

#    21. Write a Python program to simulate a simple ATM with the following
# specifications:
#  Assume the card is valid (is_valid = True)
#  Initial account balance is 50000
#  Correct PIN is 123
#  After entering correct PIN, display the menu:
# 1. Withdraw
# 2. Check Balance
# 3. Exit
#  If user selects 1 then ask amount and deduct from balance
#  If user selects 2 then show current balance
#  If user selects 3 then print “Thank you for visiting”
#  Show proper messages for wrong PIN and invalid option Use nested if-else
# statements only     


# Card valid cha bhane
is_valid = True

# Initial account balance
balance = 50000

# Correct PIN
correct_pin = 123

# User le PIN halne
if is_valid:
    pin = int(input("Enter your ATM PIN: "))
    
    if pin == correct_pin:
        # PIN correct, menu display
        print("ATM Menu:")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        
        option = int(input("Select option (1-3): "))
        
        if option == 1:
            # Withdraw
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful. Remaining balance: Rs", balance)
            else:
                print("Insufficient balance")
        elif option == 2:
            # Check balance
            print("Your current balance is: Rs", balance)
        elif option == 3:
            # Exit
            print("Thank you for visiting")
        else:
            print("Invalid option selected")
    else:
        print("Wrong PIN")
else:
    print("Card not valid")
    

# 22. Create a Python program that greets the user with the message "Welcome to the
# Magic Forest". Then, ask the user whether they want to go "north" or "south". If
# they choose "south", print "Game Over". If they choose "north", ask if they want to
# "cross the river" or "follow the path". If they choose "cross the river", print "Game
# Over". If they choose "follow the path", ask them to choose between "fairy","ogre",
# or "elf". If they choose "ogre" or "fairy", print "Game Over". If they choose "elf",
# print "You Win".    

# Welcome message
print("Welcome to the Magic Forest")

# First choice: north or south
choice1 = input("Do you want to go 'north' or 'south'? ").lower()

if choice1 == "south":
    print("Game Over")  # south choose gare game over
elif choice1 == "north":
    # Second choice: cross river or follow path
    choice2 = input("Do you want to 'cross the river' or 'follow the path'? ").lower()
    
    if choice2 == "cross the river":
        print("Game Over")  # river cross gare game over
    elif choice2 == "follow the path":
        # Third choice: fairy, ogre, elf
        choice3 = input("Choose 'fairy', 'ogre', or 'elf': ").lower()
        
        if choice3 == "ogre" or choice3 == "fairy":
            print("Game Over")  # ogre or fairy choose gare game over
        elif choice3 == "elf":
            print("You Win")    # elf choose gare win
        else:
            print("Invalid choice, Game Over")
    else:
        print("Invalid choice, Game Over")
else:
    print("Invalid choice, Game Over")
    
    
#   23. Create a Python program that greets the user with the message "Welcome to the
# Haunted House". Then, ask the user whether they want to go "upstairs" or
# "downstairs". If they choose "downstairs", print "Game Over". If they choose
# "upstairs", ask if they want to "enter the room" or "stay outside". If they choose
# "enter the room", print "Game Over". If they choose "stay outside", ask them to
# choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
# "vampire", print "Game Over". If they choose "werewolf", print "You Win"  

# Welcome message
print("Welcome to the Haunted House")

# First choice: upstairs or downstairs
choice1 = input("Do you want to go 'upstairs' or 'downstairs'? ").lower()

if choice1 == "downstairs":
    print("Game Over")  # downstairs choose gare game over
elif choice1 == "upstairs":
    # Second choice: enter room or stay outside
    choice2 = input("Do you want to 'enter the room' or 'stay outside'? ").lower()
    
    if choice2 == "enter the room":
        print("Game Over")  # enter room gare game over
    elif choice2 == "stay outside":
        # Third choice: ghost, vampire, werewolf
        choice3 = input("Choose 'ghost', 'vampire', or 'werewolf': ").lower()
        
        if choice3 == "ghost" or choice3 == "vampire":
            print("Game Over")  # ghost or vampire choose gare game over
        elif choice3 == "werewolf":
            print("You Win")    # werewolf choose gare win
        else:
            print("Invalid choice, Game Over")
    else:
        print("Invalid choice, Game Over")
else:
    print("Invalid choice, Game Over")
