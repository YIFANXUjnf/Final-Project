# Final-Project
Boomboomboom - Final Project for 15112
Bomb Boom Boom

1.	Description of the project 
Bomb Boom Boom is a game that provides options for both one player and two players. There would be other three or two player controlled by computer so that there would be four players in total. Each player has unlimited bombs and starts his or her journey from one of the four corners. A round of the game would be 2 minutes long. In the end, a player wins if he or she gets the highest score.

To win the game, a player is going to occupy the square units as much as possible by explode their bombs. The area covered by an explosion caused by player A will be occupied by player A. Each player is represented by a specific color in blue, green, red and yellow. The occupied area will be colored by the color of the player. A square unit can be re-colored. In other word, player B can occupy the area that has been occupied by player A by making an explosion that covers this area. After being set up, a bomb needs 2 seconds to explode. 

Score:
+50: every square unit occupied
IMPORTANT: If a player is killed by being in the area that is covered by an explosion, his or her area would be cleared (be white) as well as the score (be zero).


2. Libraries and features that you will be using/implementing 
   Libraries like PyGame and Random will be used to develop the game. 
There would be other three or two player controlled by computer so that there would be four players in total. The algorithm of each computer controlled player will be different. 
For “single player” mode, the three other players, A, B, C, will be like this:
A will maximize its area by selecting the best position for next bomb.
B will randomly select a position for next bomb.
C will find the position having the highest possibility to kill the player representing the user.
For “two players” mode, the two other players, A, B, will be like this:
A will maximize its area by selecting the best position for next bomb.
B will randomly select a position for next bomb.

3. Description of the user interface for the project 
   The home page would have three buttons: rules, options, start. Clicking on “rules”, the users would get the introduction of this game. Clicking on “options”, the users can choose “single player” or “two players” to select modes. “Starts” is simply for starting the game.
   For different modes, choosing “single player” will automatically choose to use “←↑↓→”and “Space” to control the player, but the users can select the color they want to use. Clicking on “two players” will be led to next page to select player 1 and player 2 by the sequence of choosing the color. Player 1 will use “←↑↓→”and “Enter”; player 2 will use “WASD”and “Space”.
The playing area would contain 8 x 11 square units. There will be a column on the left to show the current score of each player. A timer would be on the top left corner. Two buttons will be in the bottom left corner. One is “home”, the other is “restart”.
In the end of a round, there will be a window to ask if the users want to go back to the home or to start the next round.


4. Set of features (with descriptions) that you will implement and demo by first milestone date of November 25. 
   Finish the algorithm of the player that is controlled by computer and maximize its score.  

5. Final set of complete features (with descriptions) that will be part of your final submission and demo on Thursday Dec 6. 
   Finish the algorithm of the other two players controlled by computer. 
