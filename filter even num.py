
#List of numbers:

number = []
for i in range(1, 101):
    number.append(i)

# for printing Even numbers:
# All even numbers form 1 to 100:

print("All Even numbers from 1 to 100:")

for i in number:
    if i%2 ==0:
        print(f"{i}", end = "   ")
        
    if i % 10 == 0:
        print("")
    


