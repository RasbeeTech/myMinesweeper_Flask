import random


class Minesweeper:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.mines = self.num_of_mines()
        self.mine_locations = self.set_mines()

    def num_of_mines(self):
        return {
            'easy': 5,
            'medium': 10,
            'hard': 20
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
        num_of_bombs = self.mines
        bomb_tiles = []
        bombs_planted = 0

        while bombs_planted < num_of_bombs:
            row = random.choice(self.play_field())
            col = random.choice(self.play_field())
            if [row, col] not in bomb_tiles:
                bomb_tiles.append([row, col])
                bombs_planted += 1
        return bomb_tiles


if __name__ == '__main__':
    print('Minesweeper')
    game = Minesweeper('medium')
    print(game.num_of_mines())
    print(game.play_field())
    print(game.mine_locations)
    print(game.set_mines())
    print(game.mine_locations)
