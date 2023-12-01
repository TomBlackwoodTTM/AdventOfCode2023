import re

def calibrated_val_sum(vals) -> int:
    sum_vals = 0
    for val in vals.split('\n'):
        if val:
            digits = re.findall(r'\d', val)
            sum_vals += int(digits[0] + digits[-1])
    # return sum(sum_vals) 
    return sum_vals

print(calibrated_val_sum("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""))