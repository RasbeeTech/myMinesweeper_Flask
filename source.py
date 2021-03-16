from random import randrange


class Minesweeper:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.mines = self.num_of_mines()

    def num_of_mines(self):
        return {
            'easy': 5,
            'medium': 10,
            'hard': 20
        }[self.difficulty]

    def change_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty
        self.mines = self.num_of_mines()


if __name__ == '__main__':
    print('Minesweeper')
    game = Minesweeper('medium')
    print(game.num_of_mines())
