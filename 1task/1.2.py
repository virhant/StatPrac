"""
def rotate(matrix, direction):
    new_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]) - 1, -1, -1)]
    return new_matrix if direction == "left" else rotate(rotate(new_matrix, "left"), "left")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix = rotate(matrix, "right")

print(rotate_matrix) 
"""

def rotate(matrix, direction):
    if direction == "left":
        return list(map(list, zip(*matrix)))[::-1]
    if direction == "right":
        return list(map(list, zip(*matrix[::-1])))
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix, "right"))