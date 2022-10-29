class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return []

        ROWS = len(board)
        COLS = len(board[0])

        x, y = click
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]

        def available(r, c):
            return r >= 0 and r < ROWS and c >= 0 and c < COLS

        def dfs(board, r, c):
            # check for empty cell in order to actually use
            if not available(r, c) or board[r][c] != "E":
                return
            # count adjacent mines
            mine_count = 0
            for dr, dc in directions:
                if available(r + dr, c + dc) and board[r + dr][c + dc] == "M":
                    mine_count += 1

            if mine_count:
                # have mines in adjacent cells
                board[r][c] = str(mine_count)
            else:
                # no adjacent mines
                board[r][c] = "B"
                for dr, dc in directions:
                    dfs(board, r + dr, c + dc)


        if board[x][y] == "M":
            board[x][y] = "X"
        elif board[x][y] == "E":
            dfs(board, x, y)
        return board