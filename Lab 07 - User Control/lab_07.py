""" Lab 7 - User Control """

import arcade
from random import randint
# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)
    def on_draw(self):
        arcade.start_render()
        # CIELO
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
        arcade.start_render()
        # SOL
        arcade.draw_circle_filled(750, 560, 100, arcade.color.WHITE)
        # ARENA
        arcade.draw_rectangle_filled(400, 0, 800, 400, arcade.color.GOLDEN_YELLOW)
        arcade.draw_rectangle_filled(400, 0, 800, 300, arcade.color.YELLOW_ROSE)
        # PIRAMIDE DERECHA
        arcade.draw_triangle_filled(0, 100, 300, 100, 150, 400, arcade.color.LIGHT_YELLOW)
        # SOMBRA PIRAMIDE DERECHA
        arcade.draw_triangle_filled(15, 100, 285, 100, 150, 385, arcade.color.YELLOW_ORANGE)
        # PIRAMIDE DERECHA
        arcade.draw_triangle_filled(800, 100, 500, 100, 650, 400, arcade.color.LIGHT_YELLOW)
        # SOMBRA PIRAMIDE DERECHA
        arcade.draw_triangle_filled(785, 100, 515, 100, 650, 385, arcade.color.YELLOW_ORANGE)
        # ESTRELLAS
        for _ in range(75):
            randx = randint(15, 650)
            randy = randint(400, 575)
            arcade.draw_rectangle_filled(randx, randy, 5, 5, arcade.color.GOLD)

        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
            """ Called to update our objects.
            Happens approximately 60 times per second."""
            self.ball.position_x = x
            self.ball.position_y = y
def main():
    window = MyGame()
    arcade.run()



main()