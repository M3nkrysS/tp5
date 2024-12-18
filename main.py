"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import arcade
from random import randint, choice


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"

def random_number(randomness):
    number = randint(0, randomness)
    return number


class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # Si vous avez des listes de sprites, il faut les créer ici et les
        # initialiser à None.

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        self.black = 0, 0, 0
        self.blue = 0, 0, 255
        self.brown = 177, 117, 89
        self.dark_blue = 0, 0, 128
        self.cyan = 0, 255, 255
        self.gold = 255, 220, 70
        self.green = 0, 255, 0
        self.red = 255, 0, 0
        self.grey = 180, 180, 180
        self.orange = 255, 120, 0
        self.pink = 255, 0, 128
        self.purple = 170, 0, 255
        self.silver = 240, 240, 235
        self.violet = 238, 130, 238
        self.white = 255, 255, 255
        self.yellow = 255, 255, 0
        self.salmon = 255, 76, 76
        self.copper = 245, 175, 145
        self.brass = 220, 175, 90
        self.mandarin = 255, 156, 0
        self.color_list = [self.black, self.dark_blue, self.blue, self.brown, self.cyan, self.gold, self.green, self.red, self.grey, self.orange, self.pink, self.purple, self.silver, self.violet, self.white, self.yellow, self.salmon, self.salmon, self.copper, self.brass, self.mandarin]
        self.number_of_repeats = 0

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """
        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".

        while self.number_of_repeats <= 20:
            self.random_color = choice(self.color_list)
            self.circle = arcade.draw_circle_filled(random_number(800), random_number(600), random_number(100),(self.random_color))
            self.color_list.remove(self.random_color)
            self.number_of_repeats += 1
        # Invoquer la méthode "draw()" de vos sprites ici.

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Cette méthode est invoquée à chaque fois que l'usager tape une touche
        sur le clavier.
        Paramètres:
            - key: la touche enfoncée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

        Pour connaître la liste des touches possibles:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres:
            - key: la touche relâchée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Méthode invoquée lorsque le curseur de la souris se déplace dans la fenêtre.
        Paramètres:
            - x, y: les coordonnées de l'emplacement actuel de la sourir
            - delta_X, delta_y: le changement (x et y) depuis la dernière fois que la méthode a été invoqué.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button: le bouton de la souris appuyé
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button: le bouton de la souris relâché
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
