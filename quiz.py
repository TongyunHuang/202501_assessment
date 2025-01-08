
def reverse_list(l:list):

    """
    TODO: Reverse a list without using any built in functions
    Input l is a list which can contain any type of data.
    """
    n = len(l)
    for i in range(n // 2):
        l[i], l[n-1-i] = l[n-1-i], l[i]
    return l

 
def solve_sudoku(matrix):

    """
    TODO: Write a programme to solve 9x9 Sudoku board.
    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.
    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """
    n = 3
    N = n * n
    # Return True if 
    def is_valid_place(num, x, y):
        return num not in rows[x] and num not in columns[y] and num not in blocks[to_block_index(x, y)]

    def place_num(num, x, y):
        rows[x].add(num)
        columns[y].add(num)
        blocks[to_block_index(x, y)].add(num)
        matrix[x][y] = str(num)
    
    def remove_num(num, x, y):
        rows[x].remove(num)
        columns[y].remove(num)
        blocks[to_block_index(x, y)].remove(num)
        matrix[x][y] = '.'

    def backtrack(x, y) -> bool:
        next_x = x + 1 if y == N-1 else x
        next_y = 0 if y == N-1 else y + 1
        if matrix[x][y] == '.':
            for i in range(1, 10):
                if is_valid_place(i, x, y):
                        place_num(i, x, y)
                        if x == N-1 and y == N-1:
                            return True
                        res = backtrack(next_x, next_y)
                        if res == True:
                            return True
                        else:
                            remove_num(i, x, y)
        elif x == N-1 and y == N-1:
            return True
        else:
            return backtrack(next_x, next_y)


    def to_block_index(x,y):
        return (x//n) * n + y // n
    
    rows = [set() for _ in range(N)] # rows[i] is a set containing all number in that row
    columns = [set() for _ in range(N)]
    blocks = [set() for _ in range(N)] # 3x3 blocks
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != ".":
                num = int(matrix[i][j])
                place_num(num, i, j)
    backtrack(0,0)
    return matrix


    



"""
Unit Test
"""
import unittest
class TestStringMethods(unittest.TestCase):

    def test_reverse_list_even(self):
        self.assertEqual(reverse_list([1, 'a', 2, 'b']), ['b', 2, 'a', 1])

    def test_reverse_list_odd(self):
        self.assertTrue(reverse_list([1, 'a', 2]), [ 2, 'a', 1])

    def test_reverse_list_edge(self):
        self.assertEqual(reverse_list([]), [])
        self.assertTrue(reverse_list([1]), [1])

    def test_sudoku_0(self):
        input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        self.assertEqual(solve_sudoku(input), output)

if __name__ == '__main__':
    unittest.main()