print("----- Student Grade Calculator -----")

# Getting marks from the user
m1 = float(input("Enter Mark 1: "))
m2 = float(input("Enter Mark 2: "))
m3 = float(input("Enter Mark 3: "))
m4 = float(input("Enter Mark 4: "))
m5 = float(input("Enter Mark 5: "))

# Calculating total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100   # since 5 subjects, each out of 100

# Finding Grade
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Final Output
print("\n------ RESULT ------")
print(f"Total Marks   : {total}")
print(f"Percentage    : {percentage:.2f}%")
print(f"Grade         : {grade}")