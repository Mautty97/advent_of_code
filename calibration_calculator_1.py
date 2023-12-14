file =  open('calibration.txt', 'r')

total_cal_value = 0

for line in file:
    for digit in line:
        if digit.isdigit():
            val1 = digit
            print(val1, "break")
            break
    for digit in reversed(line):
        if digit.isdigit():
            val2 = digit
            print(val2, "break")
            break
    val_str = val1 + val2
    total_cal_value += int(val_str)
    print(total_cal_value)
print(total_cal_value)