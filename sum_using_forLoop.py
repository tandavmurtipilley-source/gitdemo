#Task 2: Sum of Integers from 1 to 50 Using a Loop

num = int(input("Enter a number for that you need sum of all number using python: "))
count = 0
for i in range(1, num + 1):
    count += i

print(f"{num} and its all number is {count}")