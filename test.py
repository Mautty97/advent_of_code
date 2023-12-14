example = "eightonetwothree"

dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for i in range(len(example)):
    for num in dic:
        if example[i:i+len(num)] == num:
            print(num, i)