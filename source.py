import random


class Minesweeper:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.mines = self.num_of_mines()
        self.mine_locations = self.set_mines()
        self.revealed_tiles = []
        self.indicators = []

    def num_of_mines(self):
        return {
            'easy': 8,
            'medium': 15,
            'hard': 30
        }[self.difficulty]

    def change_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty
        self.mines = self.num_of_mines()
        self.mine_locations = self.set_mines()

    def play_field(self):
        if self.difficulty == 'easy':
            return list(range(0, 6))
        if self.difficulty == 'medium':
            return list(range(0, 9))
        if self.difficulty == 'hard':
            return list(range(0, 12))

    def set_mines(self):
        num_of_mines = self.mines
        mine_tiles = []
        mines_planted = 0

        while mines_planted < num_of_mines:
            row = random.choice(self.play_field())
            col = random.choice(self.play_field())
            if [row, col] not in mine_tiles:
                mine_tiles.append([row, col])
                mines_planted += 1
        return mine_tiles

    def reveal_tiles(self, row, column):
        if [row,column] not in self.revealed_tiles:
            x = 10

    def set_indicators(self):
        for mine in self.mine_locations:
            self.check_adjacent(mine[0], mine[1], self.get_indicators)

    def get_indicators(self, row, column):
        if [row, column] not in self.mine_locations:
            self.indicators.append([row, column])

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
    game.change_difficulty('hard')
    print(game.mine_locations)
    game.set_indicators()
    print(game.indicators)

    # TODO: make a dictionary of tiles and the respective number indicator
    ind = game.indicators
    indi = {}
    for i in ind:
        if i[0] in indi:
            indi[i[0]].append(i[1])
        elif i[1] in ind[i[0]]:
            x = 10
        else:
            indi[i[0]] = [(i[1])]
        #print(i[0], i[1])

    print(indi)