# WAP to find the sum of first n natural numbers

n = int(input("Enter the value for n:"))

sum = 0
for i in range(1,n+1):
    sum += i

print(sum)
