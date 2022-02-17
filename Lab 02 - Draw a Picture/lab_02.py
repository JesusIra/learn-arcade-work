# Importamos arcade
import arcade

# open window
arcade.open_window (800,600, "Drawing example")
# CIELO
arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
arcade.start_render()
# SOL
arcade.draw_circle_filled(750, 575, 100, arcade.color.WHITE)
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
arcade.draw_rectangle_filled(0, 500, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(10, 500, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(60, 500, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(130, 500, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(210, 500, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(300, 559, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(15, 400, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(300, 450, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(500, 450, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(610, 555, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(15, 570, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(15, 590, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(30, 580, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(60, 585, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(90, 570, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(115, 590, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(150, 590, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(200, 590, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(455, 555, 5, 5, arcade.color.GOLD)
arcade.draw_rectangle_filled(800, 489, 5, 5, arcade.color.GOLD)

arcade.finish_render()
arcade.run()