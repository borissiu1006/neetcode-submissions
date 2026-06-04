class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                
                if board[row][col] in cols[col] or board[row][col] in rows[row] or board[row][col] in boxes[(row // 3, col // 3)]:
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                boxes[(row // 3, col // 3)].add(board[row][col])
            
        return True

    '''
        # Check dublicates
            rows = board
            columns = [[] for _ in range(9)]
            subboxes = [[] for _ in range(9)]

            for num in rows:
                checker = {}
                for i in num:
                    if i == '.':
                        continue

                    if i not in checker:
                        checker[i] = 1
                    else:
                        return False

            for col in range(9):
                for row in range(9):
                    val = board[row][col]
                    if val == '.':
                        continue

                    if val not in columns[col]:
                        columns[col].append(val)
                    else:
                        return False

            box = 0
            for row in range(9):
                if 0 <= row <= 2:
                    box = 0
                elif 3 <= row <= 5:
                    box = 3
                elif 6 <= row <= 8:
                    box = 6

                for num in range(9):
                    val = board[row][num]
                    if val == '.':
                        continue

                    if 0 <= num <= 2:
                        target = box
                    elif 3 <= num <= 5:
                        target = box + 1
                    elif 6 <= num <= 8:
                        target = box + 2

                    if val not in subboxes[target]:
                        subboxes[target].append(val)
                    else:
                        return False
            
            return True
    '''
