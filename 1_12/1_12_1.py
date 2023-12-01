file = open("input.txt", "r", encoding="UTF-8")
finalSum = 0
for line in file:
    numbers = []
    for char in line:
        if char.isnumeric():
            numbers.append(char)
    finalSum += int(str(numbers[0])+str(numbers[-1]))
print(finalSum)