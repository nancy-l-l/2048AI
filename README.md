AI wins game by deciding best move based off of running an ExpectiMiniMax Search.
We simiulate the state of the board 4 moves in advance. A move is characterized by either us choosing a move (up, down, left, right) with the best outcome, 
or the computer spawning a tile irrespective of whether a spawn is the most adversarial to the user’s progress, with a 90% probability of a 2 and 10% for a 4 (expecti).
We simulate the computer's turn by inserting a tile (2 or 4) in a random sample of the free spaces on the board. We simulate our turn by choosing a move that anticipates the highest heuristic.
We determin heuristic by 3 criteria: monotonicity, ordering tiles in a snake formation, and the number of free spaces. 
Monotonicity was calculated by taking the log_2(x) difference of neighboring tiles.
snake formation was enforced by multiplying value at tile by 4^(weight). The below matrix ensured that bigger tiles located in top row, increasing left, would score a higher heuristic.
weights=[[16,15,14,13],
        [9,10,11,12],
        [8,7,6,5],
        [1,2,3,4]]
Lastly, we evaluated a board by the number of free spaces: more free spaces received a higher score.
We enforced that our AI to have .2 seconds to make a decision. 
