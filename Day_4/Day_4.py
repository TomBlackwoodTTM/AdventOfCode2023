from pathlib import Path

def win_check(vals:list) -> int:
    total_score = 0
    win_mult = 1
    for game in vals:
        game = game.split(':')
        card_vals = game[1].split('|')
        win_vals = [int(w) for w in card_vals[0].split()]
        win_nums = [int(p) for p in card_vals[1].split() if int(p) in win_vals]
        if win_nums:
            if len(win_nums) >= 2:
                win_mult += 1
            total_score += 2 ** (len(win_nums) - 1)

    return total_score

test_set = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# print(win_check(test_set.split('\n')))

with open(Path(__file__).parent/'data/input.txt') as f:
    print(win_check(f.readlines()))