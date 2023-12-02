from pathlib import Path
import pandas as pd
import re

def find_game(games_input:list,  game_limit:dict):
    df = pd.DataFrame()
    for i, games in enumerate(games_input):
        games = games.split(':')[1].split(';')
        for j, game in enumerate(games):
            game_list = []
            for cubes in game.split(','):
                if cubes:
                    game_list.append(re.findall(r'(\d{0,2}) red|(\d{0,2}) green|(\d{0,2}) blue', cubes)[0])
            df_game = pd.DataFrame(game_list, columns = ['red', 'green', 'blue']).replace('', 0).astype(int)
            df_game['game_id'] = i + 1
            df = pd.concat([df, df_game], ignore_index=True)
    bad_games = df[(df['red'] > game_limit['red']) | (df['green'] > game_limit['green']) | (df['blue'] > game_limit['blue'])]['game_id'].unique().tolist()
    
    # Part 2
    game_power = []
    for game_id in df['game_id'].unique():
        game_power.append(df[df['game_id'] == game_id][['red', 'green', 'blue']].max(axis=0).prod())

    return df[df['game_id'].isin(bad_games) == False]['game_id'].unique().sum(), sum(game_power)


game_limit = {'red':12, 'green': 13, 'blue': 14}

test_set = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# find_game(games_input = test_set.split('\n'), game_limit = game_limit)

with open (Path(__file__).parent / 'data/input.txt', 'r') as f:
    print(find_game(games_input = f.readlines(), game_limit = game_limit))