# Tic-Tac-Toe
===================================================================================================================================

### Description

   Tic-tac-toe (or Noughts and crosses, Xs and Os) is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal row wins the game. The  best play from both parties leads to a draw (often referred to as cat or cat's game).

   The simplicity of Tic-tac-toe makes it ideal as a pedagogical tool for teaching the concepts of good sportsmanship and the branch of artificial intelligence that deals with the searching of game trees.  It is straightforward to write a computer program to play Tic-tac-toe perfectly. The game can be generalized to an m,n,k-game in which two players alternate placing stones of their own color on an m×n board, with the goal of getting k of their own color in a row. Tic-tac-toe is the (3,3,3)-game.

   Despite its apparent simplicity, Tic-tac-toe requires detailed analysis to determine even some elementary combinatory facts, the most interesting of which are the number of possible games and the number of possible positions. A position is merely a state of the board, while a game usually refers to the way a terminal position is obtained.
   
   Naive counting leads to 19,683 possible board layouts, and 362,880 possible games (different sequences for placing the Xs and Os on the board). However, two matters much reduce these numbers:

   1. The game ends when three-in-a-row is obtained.
   2. The number of Xs is always either equal to or exactly 1 more than the number of Os (if X starts).

The complete analysis is further complicated by the definitions used when setting the conditions, like board symmetries.

   When considering only the state of the board, and after taking into account board symmetries (i.e. rotations and reflections), there are only 138 terminal board positions. Assuming that X makes the first move every time:
   1. 91 unique positions are won by (X)
