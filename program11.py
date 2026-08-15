grade = input("Enter grade (A, B, C, D, F): ").upper()

if grade == 'A':
    print("Excellent")
elif grade == 'B':
    print("Good")
elif grade == 'C':
    print("Average")
elif grade == 'D':
    print("Pass")
elif grade == 'F':
    print("Fail")
else:
    print("Invalid Grade")
