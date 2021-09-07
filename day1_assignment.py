# Excersize #1
print("Excersize #1")

x = 1
while x**3 < 1000:
    cubed_num = x**3
    print(cubed_num)
    x += 1

print("")

# Excersize #2
print("Excersize #2")

for num in range(1,101,1):  
    for i in range(2,num):  
        if (num % i) == 0:  
            break  
    else:  
        print(num)  

print("")

# Excersize #3
print("Excersize #3")

age = int(input("Enter your age:"))
if age < 18:
    print("You are just a kid.")
elif age <= 65:
    print("You're an adult.")
else:
    print("You're a senior, cool.")