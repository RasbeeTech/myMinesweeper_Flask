import random


class Minesweeper:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.mines = self.num_of_mines()
        self.flags = self.mines
        self.mine_locations = []

        self.revealed_tiles = []

        self.indicators = []
        self.ind_location = []
        self.ind_number = []

        self.start_tile = []
        self.game_over = False

    def num_of_mines(self):
        return {
            'easy': 8,
            'medium': 15,
            'hard': 30
        }[self.difficulty]

    def change_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty
        self.mines = self.num_of_mines()
        self.flags = self.mines
        self.mine_locations = []
        self.revealed_tiles = []
        self.indicators = []
        self.ind_location = []
        self.ind_number = []
        self.start_tile = []
        self.game_over = False

    def play_field(self):
        if self.difficulty == 'easy':
            return list(range(0, 6))
        if self.difficulty == 'medium':
            return list(range(0, 9))
        if self.difficulty == 'hard':
            return list(range(0, 11))

    def set_mines(self):
        num_of_mines = self.mines
        mine_tiles = []
        mines_planted = 0

        while mines_planted < num_of_mines:
            row = random.choice(self.play_field())
            col = random.choice(self.play_field())
            if [row, col] not in mine_tiles and [row, col] not in self.start_tile:
                mine_tiles.append([row, col])
                mines_planted += 1
        self.mine_locations = mine_tiles

    def reveal_tiles(self, row, column):
        if [row, column] not in self.revealed_tiles:
            if [row, column] in self.mine_locations:
                self.game_over = True
            elif [row, column] in self.ind_location:
                self.revealed_tiles.append([row, column])
            elif [row, column] not in self.mine_locations and [row, column] not in self.ind_location:
                self.revealed_tiles.append([row, column])
                self.check_adjacent(row, column, self.reveal_tiles)
        play_field = max(self.play_field())
        if (len(self.mine_locations)+len(self.revealed_tiles)) == (play_field*play_field):
            self.chicken_dinner()

    def chicken_dinner(self):
        return 'Winner Winner Chicken Dinner!'

    def start_game(self, row, column):
        self.start_tile = [row, column]
        self.set_mines()
        self.set_indicators()
        self.reveal_tiles(row, column)
        self.flags = self.mines

    def toggle_game_over(self):
        self.game_over = True

    def new_game(self):
        self.mine_locations = []
        self.revealed_tiles = []
        self.indicators = []
        self.ind_location = []
        self.ind_number = []
        self.start_tile = []
        self.game_over = False
        self.flags = self.mines

    def set_indicators(self):
        for mine in self.mine_locations:
            self.check_adjacent(mine[0], mine[1], self.get_indicators)
        self.indicator_numbers_and_location()

    def get_indicators(self, row, column):
        if [row, column] not in self.mine_locations:
            self.indicators.append([row, column])

    def indicator_numbers_and_location(self):
        ind = self.indicators

        ind_location = []
        ind_number = []
        for i in ind:
            if i not in ind_location:
                ind_location.append(i)
                ind_number.append(ind.count(i))
        self.ind_location = ind_location
        self.ind_number = ind_number

    def check_adjacent(self, row, column, func):
        r = row
        c = column
        max_value = max(self.play_field())
        if r == 0 and c == 0:
            func(r, c + 1)
            func(r + 1, c)
            func(r + 1, c + 1)
        elif r == max_value and c == max_value:
            func(r - 1, c)
            func(r - 1, c - 1)
            func(r, c - 1)
        elif r == 0 and c == max_value:
            func(r, c - 1)
            func(r + 1, c - 1)
            func(r + 1, c)
        elif r == max_value and c == 0:
            func(r - 1, c)
            func(r - 1, c + 1)
            func(r, c + 1)
        elif r == 0:
            func(r, c - 1)
            func(r, c + 1)
            func(r + 1, c - 1)
            func(r + 1, c)
            func(r + 1, c + 1)
        elif r == max_value:
            func(r - 1, c)
            func(r - 1, c - 1)
            func(r - 1, c + 1)
            func(r, c - 1)
            func(r, c + 1)
        elif c == 0:
            func(r - 1, c)
            func(r - 1, c + 1)
            func(r, c + 1)
            func(r + 1, c)
            func(r + 1, c + 1)
        elif c == max_value:
            func(r - 1, c)
            func(r - 1, c - 1)
            func(r, c - 1)
            func(r + 1, c - 1)
            func(r + 1, c)
        else:
            func(r - 1, c)
            func(r - 1, c - 1)
            func(r - 1, c + 1)
            func(r, c - 1)
            func(r, c + 1)
            func(r + 1, c - 1)
            func(r + 1, c)
            func(r + 1, c + 1)


if __name__ == '__main__':
    print('Minesweeper')
    game = Minesweeper('medium')
    print(game.num_of_mines())
    print(game.play_field())
    print(game.mine_locations)
    game.change_difficulty('easy')
    print(game.mine_locations)
    game.set_indicators()
    print(game.indicators)

    print("length:", len(game.ind_location), ":", game.ind_location)
    print("length:", len(game.ind_number), ":", game.ind_number)

    game.reveal_tiles(4, 4)
    print(game.revealed_tiles)

    print("mines: ", game.mine_locations)
