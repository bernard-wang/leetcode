"""
Link:
https://leetcode.com/problems/spiral-matrix/

Description:
Given a `m x n` matrix, return all elements of the matrix in spiral order

Constrains:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

Ideas:
Use boundaries to control the position, and increment / decrement when finishing traversal in one direction; use two flag to 
control the direction of traversal and update accordingly

* better idea:
can be viewed as taking first row and then rotate the matrix counterclock 90 degree, then recursively do the taking action,
until after taking the 1 by 1 matrix

Interview:
Dingdui, 2025-06-06

"""

from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        # bounds and flags
        left_to_right = True
        up_to_down = True
        left_bound = 0
        right_bound = m - 1
        upper_bound = 0
        lower_bound = n - 1

        # current pos, row and col
        row = 0
        col = 0

        toReturn = []
        while left_bound <= right_bound and upper_bound <= lower_bound:
            # now, four types of traversal

            # first, left to right, condition: left_to_right && up_to_down, col++ until right bound, 
            # then update left_to_right & upper_bound
            if left_to_right and up_to_down:
                while col <= right_bound:
                    toReturn.append(matrix[row][col])
                    col += 1
                left_to_right = False
                upper_bound += 1
                # notice here: row increments to avoid duplicate elements, col updates due to no do-while mechanism
                row += 1
                col = right_bound
            # second, up to down, condition: !left_to_right && up_to_down, row++ until lower bound,
            # then update up_to_down & right_bound
            elif (not left_to_right) and up_to_down:
                while row <= lower_bound:
                    toReturn.append(matrix[row][col])
                    row += 1
                up_to_down = False
                right_bound -= 1
                col -= 1
                row = lower_bound
            # third, right to left, condition: !left_to_right && !up_to_down, col-- until left bound,
            # then update left_to_right & lower_bound
            elif (not left_to_right) and (not up_to_down):
                while col >= left_bound:
                    toReturn.append(matrix[row][col])
                    col -= 1
                left_to_right = True
                lower_bound -= 1
                row -= 1
                col = left_bound
            # finally, down to up, condition: left_to_right && !up_to_down, row-- until upper bound,
            # then update up_to_down & left_bound
            else:
                while row >= upper_bound:
                    toReturn.append(matrix[row][col])
                    row -= 1
                up_to_down = True
                left_bound += 1
                col += 1
                row = upper_bound
        return toReturn
    
    # a one line solution (corresponding to the `better idea`):
    # return matrix and ([*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1]))
    # the first `matrix` is for the termination condition, i.e., stop when `matrix` becomes []
    # the `[*matrix.pop(0)]` pops the first row, then make it a 1-D list
    # the `self.spiralOrder()` part does the recursion, and concat with the list from last line
    # the `[*zip(*matrix)]` first zips up the columns, working like transpose, 
    # then combines `[::-1]` to achieve the effect of rotation
    # though the first time to run matrix.pop(0), the return type has already been list
    # the parameter of recursive calls is actually list of tuples, so the [*] operation is needed
