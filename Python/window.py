
import arcade
import os


class TikTakToe(arcade.Window):
    """Main Application class."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.width = width
        self.height = height

        self.__init_variables()
        self.__init_board()
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self) -> None:
        self.game_board = arcade.Sprite(
            self.__getResourcePath('GameBoard.png'), 1.0)
        self.game_board.set_position(self.width / 2, self.height / 2)

    def on_draw(self) -> None:
        arcade.start_render()
        self.game_board.draw()
        self.xo_sprite_list.draw()

    def on_mouse_press(self, x: float, y: float,
                       button: int, modifiers: int) -> None:
        if self.winner is not None:
            self.__init_variables()
            self.__init_board()
            return

        self.__evaluate_turn(x, y)

    def update(self, delta_time: float):
        if self.__is_game_finished():
            print(f"{self.winner} is the winner!!!")

    def __evaluate_turn(self, x: float, y: float) -> None:
        x_index = int(x / (self.width / self.GRID_SIZE_X))
        y_index = int(y / (self.height / self.GRID_SIZE_Y))

        if self.board[x_index][y_index] is not None:
            return

        if self.x_turn:
            sprite = self.__load_and_position_sprite(
                self.X_FILENAME, x, y, x_index, y_index)
            self.board[x_index][y_index] = 'X'
        else:
            sprite = self.__load_and_position_sprite(
                self.O_FILENAME, x, y, x_index, y_index)
            self.board[x_index][y_index] = 'O'

        self.xo_sprite_list.append(sprite)
        self.x_turn = not self.x_turn

    def __getResourcePath(self, resource: str) -> str:
        return os.path.join(os.path.dirname(__file__), '..', 'Res', resource)

    def __load_sprite(self, filename: str) -> arcade.Sprite:
        return arcade.Sprite(self.__getResourcePath(filename),
                             self.SYMBOL_SPRITE_SIZE)

    def __load_and_position_sprite(self, filename: str,
                                   mouse_x: float, mouse_y: float,
                                   x_index: int, y_index: int)-> arcade.Sprite:
        x_position = ((self.width / self.GRID_SIZE_X) * x_index) + \
            (self.width / self.GRID_SIZE_X / 2)
        y_position = ((self.height / self.GRID_SIZE_Y) * y_index) + \
            (self.height / self.GRID_SIZE_Y / 2)

        sprite = self.__load_sprite(filename)
        sprite.set_position(x_position, y_position)
        return sprite

    def __init_board(self) -> None:
        self.board = [[None for x in range(self.GRID_SIZE_X)]
                      for y in range(self.GRID_SIZE_Y)]

    def __init_variables(self) -> None:
        self.xo_sprite_list = arcade.SpriteList()
        self.X_FILENAME = 'TikTakToe-X.png'
        self.O_FILENAME = 'TikTakToe-O.png'
        self.GRID_SIZE_X = 3
        self.GRID_SIZE_Y = 3
        self.SYMBOL_SPRITE_SIZE = 0.25
        self.x_turn = True
        self.winner = None

    def __is_game_finished(self) -> bool:
        if self.__check_diagonal_for_winner(
                self.GRID_SIZE_X, self.GRID_SIZE_Y):
            return True
        return self.__check_horizontal_and_vertical_for_winner(
            self.GRID_SIZE_X, self.GRID_SIZE_Y)

    def __check_horizontal_and_vertical_for_winner(self,
                                                   x_range: int,
                                                   y_range: int) -> bool:
        # Check for horizontal winner
        for y in range(y_range):
            symbol = self.board[0][y]
            if symbol is None:
                continue
            symbol_count = 0
            for x in range(x_range):
                if self.board[x][y] == symbol:
                    symbol_count += 1
            if symbol_count == 3:
                self.winner = symbol
                return True

        # Check for vertical winner
        for x in range(x_range):
            symbol = self.board[x][0]
            if symbol is None:
                continue
            symbol_count = 0
            for y in range(y_range):
                if self.board[x][y] == symbol:
                    symbol_count += 1
            if symbol_count == 3:
                self.winner = symbol
                return True
        return False

    def __check_diagonal_for_winner(self, x_range: int, y_range: int) -> bool:
        symbol = self.board[0][0]
        symbol_count = 0
        for x, y in zip(range(x_range), range(y_range)):
            if symbol is None:
                break

            if self.board[x][y] == symbol:
                symbol_count += 1
            if symbol_count == 3:
                self.winner = symbol
                return True

        symbol = self.board[0][y_range - 1]
        symbol_count = 0
        for x, y in zip(range(x_range), reversed(range(y_range))):
            if symbol is None:
                break

            if self.board[x][y] == symbol:
                symbol_count += 1
            if symbol_count == 3:
                self.winner = symbol
                return True
        return False
