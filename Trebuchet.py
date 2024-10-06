sum = 0

with open("TrebuchetInput.txt") as f:
    for line in f:
        numbers = []
        for c in line:
            if c.isnumeric():
                numbers.append(c)
        sum += int(numbers[0] + numbers[-1])
        print("string: " + line + " value: " + numbers[0] + numbers[-1])
print(sum)