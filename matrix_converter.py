# Enter rows: 2
# Enter columns: 3

# 1 2 3
# 4 5 6
#store as
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
def display(matrix):
    for row in matrix:
        print(row)

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        new_rows = []

        for i in range(rows):
            new_rows.append(matrix[i][j])

        result.append(new_rows)
    
    return result

def add_matrices(matrix1,matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix1[0])):
            sum_value = matrix1[i][j] + matrix2[i][j]
            row.append(sum_value)

        result.append(row)


    return result 

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

matrix = []

for i in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)



#step 5: Menu
while True:
    print("\n1.Display")
    print("2. Transpose")
    print("3.Exit")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        display(matrix)

    elif choice == 2:
        t = transpose(matrix)
        display(t)

    elif choice == 3:
        matrix2 = []

        print("Enter second matrix:")

        for i in range(rows):
            row = list(map(int,input().split()))
            matrix2.append(row)

        result = add_matrices(matrix,matrix2)

        print("Result:")
        display(result)

    elif choice == 4:
        break 

    else:
        print("Invalid choice")


