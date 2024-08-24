# Python_Games

Snake and Apple Game 

>>Import Statements

pygame: The primary library used for creating the game (includes modules for handling graphics, sound, and events).

time: Used for adding delays in the game loop.

random: Used for generating random positions for the apple.

Global Variables
SIZE: Defines the size of each block in the game (40 pixels).
background_color: RGB color (110, 110, 5) used for filling the screen in the Snake.draw() method.


>>Class: Apple

__init__(self, parent_screen)
Initializes the apple with the image located at "assets/apple (1).jpg".
Sets initial position x and y of the apple (default position is at 3 blocks away from origin).

draw(self)
Draws the apple image onto the parent_screen at its current x and y coordinates.
Uses pygame.display.flip() to update the display after drawing the apple.

move(self)
Randomly repositions the apple within the grid by assigning new x and y coordinates, ensuring it remains inside the game area.

>>Class: Snake

__init__(self, parent_screen, length)
Initializes the snake with a default length and sets up the snake body as a series of blocks.
Loads the snake block image from "assets/block.jpg".
Sets the initial direction of movement (default is "down").

increase_length(self)
Increases the length of the snake by appending a new block to its body.
Adds -1 to the snake's x and y lists, representing an off-screen block to be moved during the next game update.

draw(self)
Draws all blocks of the snake on the parent_screen at their respective coordinates using the blit method.
pygame.display.flip() updates the display after drawing.

Movement Methods
move_left(self): Sets the snake's movement direction to "left".
move_right(self): Sets the snake's movement direction to "right".
move_up(self): Sets the snake's movement direction to "up".
move_down(self): Sets the snake's movement direction to "down".

walk(self)
Updates the position of the snake's body blocks by shifting each block to the position of the block in front of it.
Moves the head of the snake according to the current direction (up, down, left, right).
Calls draw() to render the snake after the movement.

>>Class: GAME

__init__(self)
Initializes the game window, sets up the snake and apple, and starts background music.
Loads and draws the snake and apple on the screen.

is_collision(self, x1, y1, x2, y2)
Checks if there is a collision between two objects (like the snake and the apple or the snake and itself).
Returns True if the coordinates overlap within a block size, False otherwise.

display_score(self)
Displays the current score (which is the length of the snake) at the top right corner of the screen.

play_background_music(self)
Loads and plays the background music from "assets/bg_music_1 (1).mp3".

render_background(self)
Loads and displays a background image from "assets/background.jpg" onto the game screen.

play(self)
Main logic for running the game. It handles:
Rendering the background.
Moving the snake and drawing it.
Drawing the apple.
Displaying the current score.
Detecting collisions between the snake and the apple (for scoring) and between the snake and itself (for game over).
Handles collisions with the game boundaries.

show_game_over(self)
Displays the "Game Over" screen with the player's score and instructions to restart or quit.
Pauses the background music.

reset(self)
Resets the game by reinitializing the snake and apple.

run(self)

>>Main game loop:

Listens for key events (e.g., moving the snake, pausing the game, restarting).
If no game over occurs, it continuously updates the game state by calling the play() method.
Handles game over by showing the game over screen and waiting for player input to either restart or exit the game.

Main Block (if __name__ == "__main__":)
Initializes an instance of the GAME class and starts the game by calling game.run().

Key Concepts:
Game Loop: The run() method maintains a loop that processes events, updates the game state, and renders the game.

Collision Detection: Implemented in is_collision(), the game checks for various collisions (e.g., snake-apple, snake-self, and snake-boundaries).

Event Handling: The run() method captures and handles player inputs like movement, restarting, or exiting the game.




THANK YOU for reading it till here :)
