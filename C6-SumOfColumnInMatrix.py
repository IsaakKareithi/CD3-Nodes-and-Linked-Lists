#Initialize the matrices
x = [[8,2,3],
     [4,1,9],
     [1,4,8]]

answer = 0

for i in range(len(x)):
    for j in range(len(x[0])):
        #Column-wise sum of items
        answer = answer + x[j][i]

#print the column sum
print(answer, end=" ")
answer = 0