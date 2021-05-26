#Loops and conditionals
#Task 1 - Fibonacci sequence

Terms = 14
n1 = 0
n2 = 1
x = 0
print("Fibonacci sequence:")
while x < Terms:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    x += 1

