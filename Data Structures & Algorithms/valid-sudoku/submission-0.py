from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## how many set I need? i j 0-2 3-5 6-8
        #  check row , col  separately?
        
        # for i in range(3), for j in range(3)

        # no , block index is better. Collase 2D to 1D
        # index = row / 3 * 3 + col /3


        for i in range(9):
            Srow = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in Srow:
                    Srow.add(board[i][j])
                else:
                    return False

        # board_inv =[[0]*9]*9 wrong
        board_inv = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                board_inv[i][j] = board[j][i] 

        for i in range(9):
            Srow = set()
            for j in range(9):
                if board_inv[i][j] == '.':
                    continue
                if board_inv[i][j] not in Srow:
                    Srow.add(board_inv[i][j])
                else:
                    return False

        D = defaultdict(set)
        for i in range(9):
            for j in range(9):
                block_id = i // 3 * 3 + j // 3
                if board[i][j] == '.':
                    continue
                if board[i][j] not in D[block_id]:
                    D[block_id].add(board[i][j])
                else:
                    return False

        return True
