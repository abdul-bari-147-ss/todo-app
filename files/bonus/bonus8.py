date =input("Enter todays date:")
mood = input("how do you rate your mood today from 1 to 10?")
Thoughts = input("let you thoughts flow:\n")

with open(f"files/journal/{date}.txt",'w') as file:
    file.write(mood)
    file.write(Thoughts)