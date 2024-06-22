# Solution - 1
total = 0
for num in range(1, 101):
    if num % 2 == 0:
        total += num

print(total)


# solution - 2

total1 = 0
for number in range(2, 101, 2):
    total1 += number
print(total1)
