import re
from pathlib import Path

def calibrated_val_sum(vals) -> int:
    sum_vals = 0
    for val in vals:
        if val:
            digits = re.findall(r'\d', val)
            sum_vals += int(digits[0] + digits[-1])
    # return sum(sum_vals) 
    return sum_vals

def calibrated_val_sum_2(vals:list) -> int:
    digit_dict={
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    re_digit = re.compile(rf'\d|{"|".join(digit_dict.keys())}')
    sum_vals = 0
    for val in vals:
        if val:
            digits = []
            pos = 0
            while True:
                digits_s = re_digit.search(val.lower(), pos=pos)
                if digits_s is None:
                    break
                digits.append(val[digits_s.start():digits_s.end()])
                pos = digits_s.start() + 1
            if digits:
                for i, digit in enumerate(digits):
                    if digit in digit_dict.keys():
                        digits[i] = digit_dict[digit]
                sum_vals += int(digits[0] + digits[-1])
    return sum_vals

with open (Path(__file__).parent / 'data/input.txt', 'r') as f:
    print(f"Result 1: {calibrated_val_sum(f.readlines())}")

with open (Path(__file__).parent / 'data/input.txt', 'r') as f:
    print(f"Result 2: {calibrated_val_sum_2(f.readlines())}")