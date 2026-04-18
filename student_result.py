# student result system

name = input("Enter Your Name: ")

mark1 = int(input("Enter marks of Subject: 1 "))
mark2 = int(input("Enter Marks of Subject: 2 "))
mark3 = int(input("Enter marks of Subject: 3 "))
mark4 = int(input("Enter marks of Subject: 4 "))

total = mark1+mark2+mark3+mark4
percentage = total / 4
print("\nStudent Name: ", name)
print("Total :", total)
print("Percentage :", percentage)

if percentage >= 80:
    print("Grade A+")
elif percentage >= 70:
    print("Grade B ")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
elif percentage >= 20:
    print("Grade E You Failed")
