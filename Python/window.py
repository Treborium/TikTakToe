
import arcade
import os


class TikTakToe(arcade.Window):
    """Main Application class."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.xo_sprite_list = arcade.SpriteList()
        self.x_turn = True

        self.game_board = arcade.Sprite(
            self.__getResourcePath('GameBoard.png'), 1.0)
        self.game_board.set_position(self.width / 2, self.height / 2)

    def on_draw(self):
        arcade.start_render()
        self.game_board.draw()
        self.xo_sprite_list.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.x_turn:
            sprite = arcade.Sprite(
                self.__getResourcePath('TikTakToe-X.png'), 0.25)
            self.x_turn = False
        else:
            sprite = arcade.Sprite(
                self.__getResourcePath('TikTakToe-O.png'), 0.25)
            self.x_turn = True

        sprite.set_position(x, y)
        self.xo_sprite_list.append(sprite)

    def update(self, delta_time: float):
        pass

    def __getResourcePath(self, resource: str) -> str:
        return os.path.join(os.path.dirname(__file__), '..', 'Res', resource)
