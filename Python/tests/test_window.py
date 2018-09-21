import window


class TestWindow(object):

    def setup_method(self, test_method):
        self.width = 640
        self.height = 640
        self.game = window.TikTakToe(self.width, self.height)
        self.game.setup()

    def test_is_game_finished_horizontally_in_row_1(self):
        for x in range(3):
            self.game.board[x][0] = 'X'

        assert self.game._TikTakToe__is_game_finished()

    def test_is_game_finished_horizontally_in_row_2(self):
        for x in range(3):
            self.game.board[x][1] = 'X'

        assert self.game._TikTakToe__is_game_finished()

    def test_is_game_finished_horizontally_in_row_3(self):
        for x in range(3):
            self.game.board[x][2] = 'X'

        assert self.game._TikTakToe__is_game_finished()

    def test_is_game_finished_vertically_in_column_1(self):
        for y in range(3):
            self.game.board[0][y] = 'X'

        assert self.game._TikTakToe__is_game_finished()

    def test_is_game_finished_vertically_in_column_2(self):
        for y in range(3):
            self.game.board[1][y] = 'X'

        assert self.game._TikTakToe__is_game_finished()

    def test_is_game_finished_vertically_in_column_3(self):
        for y in range(3):
            self.game.board[2][y] = 'X'

        assert self.game._TikTakToe__is_game_finished()
