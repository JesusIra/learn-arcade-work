# Importamos arcade
import arcade
from random import randint
# open window
arcade.open_window (800,600, "Drawing example")
# CIELO
arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
arcade.start_render()
# SOL
arcade.draw_circle_filled(750, 560, 100, arcade.color.WHITE)
# ARENA
arcade.draw_rectangle_filled(400, 0 , 800, 400, arcade.color.GOLDEN_YELLOW)
arcade.draw_rectangle_filled(400, 0, 800, 300, arcade.color.YELLOW_ROSE)
# PIRAMIDE DERECHA
arcade.draw_triangle_filled(0, 100, 300, 100, 150, 400, arcade.color.LIGHT_YELLOW)
# SOMBRA PIRAMIDE DERECHA
arcade.draw_triangle_filled(15, 100, 285, 100, 150, 385, arcade.color.YELLOW_ORANGE)
# PIRAMIDE DERECHA
arcade.draw_triangle_filled(800, 100, 500, 100, 650, 400, arcade.color.LIGHT_YELLOW)
# SOMBRA PIRAMIDE DERECHA
arcade.draw_triangle_filled(785, 100, 515, 100, 650,385, arcade.color.YELLOW_ORANGE)
# ESTRELLAS
for _ in range(75):
    randx= randint(15, 650)
    randy=randint(400,575)
    arcade.draw_rectangle_filled(randx, randy, 5, 5, arcade.color.GOLD)
arcade.finish_render()
arcade.run()