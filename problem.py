# Control Statements:
# Conditional Statements:
#  -if, else, elif, nested if,
#  loops, pass, continue,
#  break, assert, return

# lets learn about control statements in python which help in decision making and controlling the flow of a program.
# if statement: used to execute a block of code if a specified condition is true

# Understanding with code of example:

# # we use input function to take input from user
Age = int(input("Enter your age: "))

if Age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#  if you enter age 18 or above it wil print if statement otherwise else statement will be printed.

# else statement: used to execute a block of code if the condition in the if statement is false.

# elif statement: short for "else if", used to check multiple conditions in sequence.
2

# nested if statement: an if statement inside another if statement. 
# In this code we use two if statements one inside another.

nm_1 = int(input("Enter number 1:"))
nm_2  = int(input("Enter number 2:"))

choice = input("Enter your choice +, -, *, / :")

if choice == '+':
    print("Addition:", nm_1 + nm_2)

elif choice == "-":
    print("Subtraction:", nm_1 - nm_2)

elif choice == "*":
    print("Multiplication:", nm_1 * nm_2)

elif choice == "/":
    print("Division:", nm_1 / nm_2)

else:
    print("Invalid choice!")

# # In this code we take two numbers and an operator as input from the user.
# # Based on the operator entered, the corresponding arithmetic operation is performed using if, elif, and else statements.


# # Hera are a mini conditional statement project :
# # Roadmap Provider project.
print("Welcome to the Career Path Advisor!")

#Get and normalize inputs
experience = input("Are you a fresher or experienced professional? (fresher/experienced): ").strip().lower()
interest = input("What area are you interested in? (e.g., web development, app development, data science, AI, cloud, front-end): ").strip().lower()

 # Normalize experience
if experience in ["fresher", "fresh", "new", "beginner"]:
        experience = "fresher"
elif experience in ["experienced", "exp", "professional"]:
     experience = "experienced"
else:
     print("Sorry, experience level not recognized. Please type 'fresher' or 'experienced'.")
     exit()

# Normalize interest with more flexible matching
interests_fresher = {
    "web dev": "web development",
    "web development": "web development",
    "app dev": "app development",
    "mobile": "app development",
    "android": "app development",
    "ios": "app development",
    "ds/ml/ai": "data science/ai",
    "data science": "data science/ai",
    "machine learning": "data science/ai",
    "ai": "data science/ai",
    "ml": "data science/ai"
}

interests_experienced = {
    "data analytics": "data analytics",
    "analytics": "data analytics",
    "cloud computing": "cloud computing",
    "cloud": "cloud computing",
    "devops": "cloud computing",
    "front-end": "front-end",
    "frontend": "front-end",
    "react": "front-end"
}

# Recommendations
if experience == "fresher":
    matched = None
    for key in interests_fresher:
        if key in interest:
            matched = interests_fresher[key]
            break
    
    if matched == "web development":
        print("Recommended path: Learn HTML, CSS, JavaScript, then Python + Django or React for full-stack.")
    elif matched == "app development":
        print("Recommended path: Learn Java/Kotlin (Android) or Swift (iOS), practice DSA, and build projects.")
    elif matched == "data science/ai":
        print("Recommended path: Master Python, Mathematics (Stats & Linear Algebra), Pandas, Scikit-learn, TensorFlow/PyTorch.")
    else:
        print("Interest not fully supported yet for freshers. Try: web development, app development, or data science/AI.")

elif experience == "experienced":
    matched = None
    for key in interests_experienced:
        if key in interest:
            matched = interests_experienced[key]
            break
    
    if matched == "data analytics":
        print("Recommended path: Master Python (Pandas, NumPy), SQL, Excel, Power BI or Tableau.")
    elif matched == "cloud computing":
        print("Recommended path: Learn AWS/Azure/GCP, DevOps tools (Docker, Kubernetes), Terraform, and Python automation.")
    elif matched == "front-end":
        print("Recommended path: Deepen React/Vue/Angular, TypeScript, performance optimization, and modern tooling.")
    else:
        print("Interest not fully supported yet for experienced professionals.")



# Certificate Eligibility Checker
print("\nCertificate Eligibility Checker")

# Get attendance
attendance = input("Did you attend 'All Day' or was there a 'Day Gap'? ").strip().lower()

if attendance in ["all day", "all", "full", "no gap"]:
    # Only ask for activity if full attendance
    activity = input("Which activity did you participate in? (e.g., Assignment, LIVE Class, Camera On): ").strip().lower()

    # Define what makes someone eligible
    eligible_keywords = ["assignment", "live class", "live"]
    ineligible_keyword = "camera on"

    # Check if any eligible activity is mentioned
    has_eligible = any(keyword in activity for keyword in eligible_keywords)
    has_only_camera = "camera on" in activity and not has_eligible

    if has_eligible:
        print("Congratulations! You are eligible for a certificate.")
    elif has_only_camera:
        print("Sorry, 'Camera On' alone does not qualify. You are NOT eligible for a certificate.")
    else:
        print("Activity not recognized. Please choose from: Assignment, LIVE Class, or Camera On.")

elif attendance in ["day gap", "gap", "daygap"]:
    print("Sorry, having a day gap means you are NOT eligible for a certificate.")

else:
    print("Invalid input. Please type 'All Day' or 'Day Gap' for attendance.")



# # Next topic will be covered in next file.
# # Loops in python:
# # used to execute a block of code repeatedly until a certain condition is met

# # for loop, while loop, nested loop

# # Here we will learn about different types of Loops in python.

# # for loop: used to iterate over a sequence (like a list, tuple, string, dictionary) or other iterable objec

#,, for loop
# [1,2,3,4,5]
# 5 times
# --ex
for i in range(5):
    print("Iteration:", i)
# # ,,#

# # while loop: used to execute a block of code as long as a specified condition is true
print("=== Countdown Timer ===\n")

n = int(input("Enter a number to start countdown from: "))

while n > 0:
    print(n)
    n -= 1

print("🎉 Time's Up! Boom!")


# nested loop: a loop inside another loop
# Here is an example of nasted or while true loops ,
print("=== Multiplication Table ===\n")

while True:
    n = int(input("Enter a number (or 0 to exit): "))
    
    if n == 0:
        print("Goodbye! 👋")
        break
    
    print(f"\nTable of {n}:")
    i = 1
    while i <= 10:          # Nested while loop
        print(f"{n} x {i} = {n * i}")
        i += 1
    print()                 # Blank line after table


# # Lets know about range functiion:
# # range(start, stop, step)
# # start: starting value (inclusive) 
# # stop: ending value (exclusive)
# # step: increment value (default is 1) otherwise you can specify any value
# # for num in range(1, 10, 2):
# #     print(num)
# # This will print odd numbers from 1 to 9


# # Now we will write a  mini project using for loops for logical thinking and building problem solving skills.

print("=== Student Mark Sheet & Grade Calculator ===\n")

# Get number of subjects
while True:
    try:
        num_subjects = int(input("How many subjects do you have? "))
        if num_subjects <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

# Initialize variables
total_marks = 0
marks_list = []

print("\nEnter marks for each subject (out of 100):")

# Use for loop to take marks for each subject
for i in range(1, num_subjects + 1):
    while True:
        try:
            mark = float(input(f"Subject {i} marks: "))
            if 0 <= mark <= 100:
                marks_list.append(mark)
                total_marks += mark
                break
            else:
                print("Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Calculate percentage
percentage = (total_marks / (num_subjects * 100)) * 100

# Display individual marks
print("\n" + "="*40)
print("         MARK SHEET")
print("="*40)
for i in range(num_subjects):
    print(f"Subject {i+1}: {marks_list[i]} / 100")

print("-"*40)
print(f"Total Marks : {total_marks} / {num_subjects * 100}")
print(f"Percentage  : {percentage:.2f}%")

# Determine grade using if-elif
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

print(f"Grade       : {grade}")
print("="*40)

# Bonus: Motivational message using for loop!
print("\nKeep up the great work!" if percentage >= 50 else "\nDon't give up! You can do better next time!")

# Fun star rating based on percentage
print("\nYour Performance:")
stars = int(percentage // 10)  # 95% → 9 stars
for _ in range(stars):
    print("⭐", end="")
print()
