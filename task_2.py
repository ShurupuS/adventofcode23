from utils import Utils

class ColorCount:
    def __init__(self, color, count):
        self.color = color
        self.count = count

class Round:
    def __init__(self):
        self.color_counts = []

class Game:
    def __init__(self, game_number):
        self.game_number = game_number
        self.rounds = []

    # 12 red cubes, 13 green cubes, and 14 blue
    def is_correct_day(self):
        for round in self.rounds:
            for color_count in round.color_counts:
                if color_count.color == 'red':
                    if color_count.count > 12:
                        return False

                if color_count.color == 'green':
                    if color_count.count > 13:
                        return False

                if color_count.color == 'blue':
                    if color_count.count > 14:
                        return False

        return True

class Day_2:
    def execute(self):
        print("Day 2")
        data = Utils.read_file('day2.txt')
        games = []
        for game_string in data:
            game = Day_2.parse_game_string(game_string)
            games.append(game)
        print(games)
        correct_games = [game for game in games if game.is_correct_day()]
        game_ids = [Day_2.extract_game_id(game) for game in correct_games]
        sum_value = sum(int(i) for i in game_ids)
        print(sum_value)

    def extract_game_id(game):
        return game.game_number

    def parse_game_string(game_string):
        # Split the string by ': ' to get the game number and the rounds string
        game_number_string, rounds_string = game_string.split(': ')

        # Convert the game number string to an integer
        game_number = int(game_number_string.split(' ')[1])

        # Create a Game object
        game = Game(game_number)

        # Split the rounds string by '; ' to get the rounds
        rounds_strings = rounds_string.split('; ')

        for round_string in rounds_strings:
            # Create a Round object
            round = Round()

            # Split the round string by ', ' to get the color counts
            color_count_strings = round_string.split(', ')

            for color_count_string in color_count_strings:
                # Split the color count string by ' ' to get the count and the color
                count_string, color = color_count_string.split(' ')

                # Convert the count string to an integer
                count = int(count_string)

                # Create a ColorCount object
                color_count = ColorCount(color, count)

                # Add the ColorCount object to the Round object
                round.color_counts.append(color_count)

            # Add the Round object to the Game object
            game.rounds.append(round)

        return game