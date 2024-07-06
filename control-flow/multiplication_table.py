#Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

#Generate and Print the multiplication table
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")