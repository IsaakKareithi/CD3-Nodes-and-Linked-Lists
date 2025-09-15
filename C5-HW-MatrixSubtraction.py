#initialize matrix

x = [[11,9],
     [2,4]]

y = [[7,5],
     [1,5]]

answer = [[0,0],
          [0,0]]

#traverse array 
for i in range(len(x)):
    for j in range(len(y[0])):
        answer[i][j] = x[i][j] - y[i][j]

for r in answer:
    print(r)