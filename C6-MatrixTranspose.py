 #Initialize matrix
x = [[8,4,3],
     [4,1,9],
     [1,4,8]]

answer = [[0,0,0,],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        #Transpose the matrix by turning the column into rows and turning rows into columns
        answer[i][j] = x[j][i]

#print the output
for r in answer:
    print(r)