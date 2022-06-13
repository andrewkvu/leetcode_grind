class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(9):
            seenSet = set()
            for c in range(9):
                if board[r][c] != "." and board[r][c] not in seenSet:
                    seenSet.add(board[r][c])
                elif board[r][c] in seenSet:
                    print("false in rows")
                    return False

        # check columns
        for r in range(9):
            seenSet = set()
            for c in range(9):
                if board[c][r] != "." and board[c][r] not in seenSet:
                    seenSet.add(board[c][r])
                elif board[c][r] in seenSet:
                    print("false in cols")
                    return False
        # check boxes
        for boxR in range(0, 9, 3):
            for boxC in range(0, 9, 3):
                seenSet = set()
                for r in range(3):
                    for c in range(3):
                        if board[boxR + r][boxC + c] != "." and board[boxR + r][boxC + c] not in seenSet:
                            seenSet.add(board[boxR + r][boxC + c])
                        elif board[boxR + r][boxC + c] in seenSet:
                            print("false in box")
                            return False
        return True