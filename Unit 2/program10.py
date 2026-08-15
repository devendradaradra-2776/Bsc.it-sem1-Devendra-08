sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
print("Total Marks:", total)

if total >= 90:
    print("Grade A+")
elif 80 <= total <= 89:
    print("Grade A")
elif 70 <= total <= 79:
    print("Grade A-")
elif 60 <= total <= 69:
    print("Grade B+")
elif 50 <= total <= 59:
    print("Grade B")
elif 40 <= total <= 49:
    print("Grade C")
else:
    print("Fail")
