"""
Starting Template

"""
import random

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)


        # If you have sprite lists, you should create them here,
        # and set them to None
        self.car_list = None
        self.truck_list = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.car_list = arcade.SpriteList()
        self.truck_list = arcade.SpriteList()


        for y in range(100, 700, 200):
            for i in range(5):
                car = arcade.Sprite("/Users/taylorpaxman/Desktop/School Fall 2021/CSE210/cse210-tc03/cse210-project/frogger/Pictures/convertible-car.png",0.05)
                car.center_x = random.randrange(100, 700, 100)
                car.center_y = y

                car.change_x = 4 #random.randrange(1,5)
                self.car_list.append(car)

        for y in range(200, 600, 200):
            for i in range(3):
                truck = arcade.Sprite("/Users/taylorpaxman/Desktop/School Fall 2021/CSE210/cse210-tc03/cse210-project/frogger/Pictures/truck.png",0.20)
                truck.center_x = random.randrange(100, 700, 150)
                truck.center_y = y

                truck.change_x = 1#random.randrange(1,5)
                self.truck_list.append(truck)

        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)



    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.car_list.draw()
        self.truck_list.draw()


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        for car in self.car_list:
            car.center_x -= car.change_x
            if car.center_x <= 0:
                car.center_x = 800
        for truck in self.truck_list:
            truck.center_x += truck.change_x
            if truck.center_x >= 800:
                truck.center_x = 0



    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
