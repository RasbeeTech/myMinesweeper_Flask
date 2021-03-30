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

    # Sets number of mines in accordance to chosen difficulty
    def num_of_mines(self):
        return {
            'easy': 5,
            'medium': 10,
            'hard': 20
        }[self.difficulty]

    # When the game difficulty is changed, reset game parameters
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

    # Set the size of playing field relative to the game difficulty
    def play_field(self):
        # Returns row/column numbers in the form of a list
        if self.difficulty == 'easy':
            return list(range(0, 6))
        if self.difficulty == 'medium':
            return list(range(0, 9))
        if self.difficulty == 'hard':
            return list(range(0, 11))

    def set_mines(self):
        num_of_mines = self.mines
        # mine_tiles variable holds the mine locations
        mine_tiles = []
        # mines_planted keeps track of mines set
        mines_planted = 0

        while mines_planted < num_of_mines:
            # generate random row and column locations within the game's play field
            row = random.choice(self.play_field())
            col = random.choice(self.play_field())
            # if statement ensures that only one mine is placed per location
            # also ensures the mine is not location on the first clicked tile(start_tile)
            if [row, col] not in mine_tiles and [row, col] != self.start_tile:
                mine_tiles.append([row, col])
                mines_planted += 1
        self.mine_locations = mine_tiles

    # function to reveal tiles
    def reveal_tiles(self, row, column):
        # the following If statement ensures that user is not
        if [row, column] not in self.revealed_tiles:
            # If statement to store indicator locations if the location has an indicator...
            if [row, column] in self.ind_location:
                self.revealed_tiles.append([row, column])
            # ...Otherwise, add location to the revealed tiles
            elif [row, column] not in self.mine_locations and [row, column] not in self.ind_location:
                self.revealed_tiles.append([row, column])
                # Creates a recursion to reveal all empty tiles adjacent to the location
                self.check_adjacent(row, column, self.reveal_tiles)

    # function to get indicators for tiles that have been revealed
    def get_revealed_indicators(self):
        revealed = self.revealed_tiles
        ind_locations = self.ind_location
        ind_numbers = self.ind_number

        revealed_ind_locations = []
        revealed_ind_numbers = []
        for tile in revealed:
            if tile in ind_locations:
                revealed_ind_locations.append(tile)
                revealed_ind_numbers.append(ind_numbers[ind_locations.index(tile)])
        return revealed_ind_locations, revealed_ind_numbers

    # function to start the game
    # to avoid revealing a mine on first reveal/click, sets mines in locations after first click
    def start_game(self, row, column):
        self.start_tile = [row, column]
        self.set_mines()
        self.set_indicators()
        self.reveal_tiles(row, column)
        self.flags = self.mines

    # reset minesweeper game parameters to start a new game
    def new_game(self):
        self.mine_locations = []
        self.revealed_tiles = []
        self.indicators = []
        self.ind_location = []
        self.ind_number = []
        self.start_tile = []
        self.flags = self.mines

    # function to set indicators: places indicators on open tiles that are adjacent to mine locations
    def set_indicators(self):
        for mine in self.mine_locations:
            self.check_adjacent(mine[0], mine[1], self.get_indicators)
        self.indicator_numbers_and_location()

    def get_indicators(self, row, column):
        if [row, column] not in self.mine_locations:
            self.indicators.append([row, column])

    # gets the correct indicator numbers
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

    # function to check adjacent tile locations and can apply a function to adjacent tile locations
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

    # function to check game status (win or lose)
    def chicken_dinner(self):
        play_field = len(self.play_field())
        if (len(self.mine_locations) + len(self.revealed_tiles)) == (play_field * play_field):
            return "Winner Winner"