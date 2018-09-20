
import arcade
import os


class TikTakToe(arcade.Window):
    """Main Application class."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self) -> None:
        self.xo_sprite_list = arcade.SpriteList()
        self.X_FILENAME = 'TikTakToe-X.png'
        self.O_FILENAME = 'TikTakToe-O.png'
        self.x_turn = True

        self.game_board = arcade.Sprite(
            self.__getResourcePath('GameBoard.png'), 1.0)
        self.game_board.set_position(self.width / 2, self.height / 2)

    def on_draw(self) -> None:
        arcade.start_render()
        self.game_board.draw()
        self.xo_sprite_list.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        self.__evaluate_turn(x, y)

    def update(self, delta_time: float):
        pass

    def __evaluate_turn(self, x: float, y: float) -> None:
        if self.x_turn:
            sprite = self.__load_sprite(self.X_FILENAME)
        else:
            sprite = self.__load_sprite(self.O_FILENAME)

        sprite.set_position(x, y)
        self.xo_sprite_list.append(sprite)

        self.x_turn = not self.x_turn

    def __getResourcePath(self, resource: str) -> str:
        return os.path.join(os.path.dirname(__file__), '..', 'Res', resource)

    def __load_sprite(self, filename: str) -> arcade.Sprite:
        return arcade.Sprite(self.__getResourcePath(filename), 0.25)
