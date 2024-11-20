#Nancy Liddle nll2128
import random
import math
import time
from BaseAI import BaseAI
class IntelligentAgent(BaseAI):
    def __init__(self):
        self.time_limit = 0.18  # Time limit per move in seconds (0.2 minus buffer)
        self.start_time = None
    def getMove(self, grid):
        self.start_time = time.time()
        heuristics = {}
        moveset = grid.getAvailableMoves()
        if len(moveset)==0:
            return None
        for move in moveset:
            heuristics[move[0]]=self.minimax(move[1],4,float('-inf'),float('inf'),False)
        return max(heuristics, key=heuristics.get)
    def minimax(self, grid, depth, alpha, beta, us):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.time_limit:
            return self.heuristic(grid)
        if depth==0 or len(grid.getAvailableCells())==0:
            return self.heuristic(grid)
        if us:
            maxEval = float('-inf')
            for move in grid.getAvailableMoves():
                eval = self.minimax(move[1], depth-1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta<=alpha:
                    break
            return maxEval
        else:
            avg=0
            empty=grid.getAvailableCells()
            num_samples = min(len(empty), 4)
            sampled_cells = random.sample(empty, num_samples)
            for sqr in sampled_cells:
                for value, prob in [(2, 0.9), (4, 0.1)]:
                    temp=grid.clone()
                    temp.setCellValue(sqr, value)
                    eval=self.minimax(temp, depth-1, alpha, beta, True)
                    avg+=(prob / num_samples) * eval
            return avg
    def heuristic(self, grid):

        weights=[
            [16,15,14,13],
            [9,10,11,12],
            [8,7,6,5],
            [1,2,3,4]]
        neighbors = [
            [[(0, 1)], [(0, 0), (0, 2)], [(0, 1), (0, 3)], [(0, 2), (1, 3)]],
            [[(1, 1), (2, 0)], [(1, 0), (1, 2)], [(1, 3), (1, 1)], [(0, 3), (1, 2)]],
            [[(1, 0), (2, 1)], [(2, 0), (2, 2)], [(2, 3), (2, 1)], [(3, 3), (2, 2)]],
            [[(3, 1)], [(3, 0), (3, 2)], [(3, 3), (3, 1)], [(2, 3), (3, 2)]]]

        weight=0
        smooth=0
        for i in range(4):
            for j in range(4):
                cur = grid.getCellValue((i, j))
                weight+=(cur*(4**weights[i][j]))
                for neighbor in neighbors[i][j]:
                    if grid.getCellValue(neighbor) !=0 and cur != 0:
                        smooth -= abs(math.log2(grid.getCellValue(neighbor)) - math.log2(cur))
        return smooth+weight+len(grid.getAvailableCells())
