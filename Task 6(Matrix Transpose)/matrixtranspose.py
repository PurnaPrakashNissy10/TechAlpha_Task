def transpose_matrix(matrix):
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize the transpose matrix with the dimensions swapped
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Populate the transpose matrix
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose


matrix = [[1, 2], [3, 4], [5, 6]]
# Get the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
print(transposed_matrix)
