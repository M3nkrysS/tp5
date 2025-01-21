"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import arcade
from random import randint


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"

def random_number(randomness):
    number = randint(0, randomness)
    return number


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK_BEAN)


        # Si vous avez des listes de sprites, il faut les créer ici et les
        # initialiser à None.

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """
        self.clear()

        arcade.draw_circle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.55, 222, arcade.color.CHARTREUSE,
                                   10, random_number(45), 7)



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
        arcade.draw.draw_ellipse_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.55, 200, (1,1,1))


def main():
    my_game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()


if __name__ == "__main__":
    main()
