file = open('calibration.txt', 'r')

total_cal_value = 0

word_to_num = {
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

#find first digit in string
for line in file:  
    found_first = False   
    for i in range(len(line)):
        if found_first == True:
            break 
        #check if there is a word num at i
        for (word, num) in word_to_num.items():
            if line[i:i+len(word)] == word:
                num_1 = num
                print(num)
                found_first = True
                break
        if found_first == True:
            break 
        #check if there is a digit at i
        elif line[i].isdigit():
            num_1 = line[i]
            print(num_1)
            found_first = True
            break
    print("reverse")
    found_last = False
    for i in range(len(line)-1, -1, -1):
        if found_last == True:
            print("found")
            break 
        #check if there is a word num at i
        for (word, num) in word_to_num.items():
            if line[i:i+len(word)] == word:
                num_2 = num
                print(num)
                found_last = True
                break
        if found_last == True:
            break 
        #check if there is a digit at i
        elif line[i].isdigit():
            num_2 = line[i]
            print(num_2)
            found_last = True
            break
    val = str(num_1) + str(num_2)
    total_cal_value += int(val)
print(total_cal_value)