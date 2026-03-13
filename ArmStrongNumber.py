num = int(input())

n = num

# Number has no length thats why I convert number into string
power = len(str(num))

total = 0

while n > 0:
    digit = n % 10
    total = total + (digit ** power)
    n = n // 10


if (total == num):
    print("Armstrong number")
else:
    print("Not Armstrong number")

# print(power)