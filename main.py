"""
Lucas Beaudry Tinkler
GR: 401
dessin d'un écran Hacké
"""

import arcade
from random import randint


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.EERIE_BLACK)

        # Si vous avez des listes de sprites, il faut les créer ici et les
        # initialiser à None.

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """
        self.clear()
        arcade.draw_circle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_HEIGHT/2, arcade.color.CHARTREUSE,
                                   10, 0, 8)

        self.bones_draw()
        self.skull_draw()
        self.hacked_draw()



    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        pass

    def skull_draw(self):
        # cranium
        arcade.draw.draw_ellipse_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.55,
                                        400, 370, arcade.color.BONE)
        arcade.draw_ellipse_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.55,
                                    400, 370, arcade.color.BLACK, 5)
        # yeux
        arcade.draw_circle_filled(300, 400,
                                  50, arcade.color.RED_DEVIL)
        arcade.draw_circle_filled(500, 400,
                                  50, arcade.color.RED_DEVIL)
        arcade.draw_circle_outline(300, 400,
                                    50, arcade.color.BLACK, 5)
        arcade.draw_circle_outline(500, 400,
                                   50, arcade.color.BLACK, 5)
        # dent(4)
        r0 = arcade.rect.XYWH(SCREEN_WIDTH/2, 240, 200, 100)
        arcade.draw_rect_filled(r0, arcade.color.BONE)
        arcade.draw_arc_filled(325, 190, 50, 70,
                               arcade.color.BONE, 0, 180, 180)
        arcade.draw_arc_filled(375, 190, 50, 70,
                               arcade.color.BONE, 0, 180, 180)
        arcade.draw_arc_filled(425, 190, 50, 70,
                               arcade.color.BONE, 0, 180, 180)
        arcade.draw_arc_filled(475, 190, 50, 70,
                               arcade.color.BONE, 0, 180, 180)

        arcade.draw_arc_outline(325, 190, 50, 70,
                                arcade.color.BLACK, 0, 180, 5, 180)
        arcade.draw_arc_outline(375, 190, 50, 70,
                                arcade.color.BLACK, 0, 180, 5, 180)
        arcade.draw_arc_outline(425, 190, 50, 70,
                                arcade.color.BLACK, 0, 180, 5, 180)
        arcade.draw_arc_outline(475, 190, 50, 70,
                                arcade.color.BLACK, 0, 180, 5, 180)
        arcade.draw_arc_outline(325, 200, 50, 60,
                                arcade.color.BLACK, 0, 180, 5)
        arcade.draw_arc_outline(375, 200, 50, 60,
                                arcade.color.BLACK, 0, 180, 5)
        arcade.draw_arc_outline(425, 200, 50, 60,
                                arcade.color.BLACK, 0, 180, 5)
        arcade.draw_arc_outline(475, 200, 50, 60,
                                arcade.color.BLACK, 0, 180, 5)

        points_list0 = [(300, 260), (300, 200)]
        points_list1 = [(500, 260), (500, 200)]
        arcade.draw_lines(points_list0, arcade.color.BLACK, 3)
        arcade.draw_lines(points_list1, arcade.color.BLACK, 3)

        # nez
        y = SCREEN_HEIGHT / 2
        x = SCREEN_WIDTH / 2
        arcade.draw.draw_triangle_filled(x, y + 50,
                                         x - 40, y - 20,
                                         x + 40, y - 20,
                                         arcade.color.BLACK)

    def bones_draw(self):
        # os 1
        r1 = arcade.rect.XYWH(SCREEN_WIDTH/2.1, SCREEN_HEIGHT/2, 700, 150)
        arcade.draw_rect_filled(r1, arcade.color.RED, 45)
        arcade.draw_rect_outline(r1, arcade.color.BLACK, 5, 45)
        # os 2
        r2 = arcade.rect.XYWH(SCREEN_WIDTH / 1.9, SCREEN_HEIGHT / 2, 700, 150)
        arcade.draw_rect_filled(r2, arcade.color.RED, 135)
        arcade.draw_rect_outline(r2, arcade.color.BLACK, 5, 135)

    def hacked_draw(self):
        hacked = arcade.Text("H  CKED", 200, 10, arcade.color.ANTI_FLASH_WHITE, 100, 20)
        hacked.draw()
        points_list2 = [(285, 5), (305, 5), (315, 35), (325, 5), (345, 5), (315, 105)]
        arcade.draw_polygon_filled(points_list2, arcade.color.IMPERIAL_RED)
        arcade.draw_polygon_outline(points_list2, arcade.color.BLACK, 5)


def main():
    my_game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()


if __name__ == "__main__":
    main()