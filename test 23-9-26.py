## BINARY PROGRAM
numbers = input().split(",")
result = []

for i in numbers:
    num = int(i,2)
    if num%5==0:
        result.append(i)
print(",".join(result))

## LETTER AND DIGIT PROGRAM

sentence = input()

l = 0
d = 0
for i in sentence:
    if i.isalpha():
        l+=1
    elif i.isdigit():
        d+=1
print("Letters: ",l)
print("Digit: ",d)

## FACTORIAL PROGRAM
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factorial: ",fact)
