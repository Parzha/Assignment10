import arcade


SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
SCREEN_TITLE = "Complex Loops - Box"


class BackGround(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
    def on_draw(self):
        arcade.start_render()
        self.DiamondMaker()

    def DiamondMaker(self):
        count = 0
        for i in range(140,375,25):
            for j in range(140,375,25):
                count += 1
                if i % 2 == 0:
                    if count % 2 == 0:
                        arcade.draw_rectangle_filled(j, i, 10, 10, arcade.color.BLUE, 45)
                    else:
                        arcade.draw_rectangle_filled(j, i, 10, 10, arcade.color.RED, 45)
                else:
                    if count % 2 == 0:
                        arcade.draw_rectangle_filled(j, i, 10, 10, arcade.color.RED, 45)
                    else:
                        arcade.draw_rectangle_filled(j, i, 10, 10, arcade.color.BLUE, 45)


if __name__ == "__main__":
    gui = BackGround()
    arcade.run()