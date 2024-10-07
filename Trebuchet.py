def convertToNumber(number):
    if number.isnumeric():
        return int(number)
    match number:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9

sum = 0
numbersToFind = ["1", "one", "2", "two", "3", "three", "4", "four", "5", "five", "6",
                 "six", "7", "seven", "8", "eight", "9", "nine"]

with open("TrebuchetInput.txt", "r", encoding="utf-8") as f:
    for line in f:
        numbers = []
        for s in numbersToFind:
            foundLowestIndex = line.find(s)
            foundHighestIndex = line.rfind(s)
            if foundLowestIndex != -1:
                numbers.append((foundLowestIndex, s))
            if foundHighestIndex != -1:
                numbers.append((foundHighestIndex, s))
        sorted_list = sorted(numbers)
        numberToAdd = convertToNumber(sorted_list[0][1]) * 10 + convertToNumber(sorted_list[-1][1])
        sum += numberToAdd
    print(sum)

