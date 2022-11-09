from numpy import *
num_grid=array([
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) 
res=array([
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
]
)
k=0
for i in range (5):
    for j in range(5):
        res[i][j]=int(res[i,j])
        if num_grid[i][j]=="#" :
            res[i][j]=num_grid[i][j]
            res[i+1][j]=+1
            res[i][j+1]=+1
            res[i+1][j+1]=+1

            res[i-1][j]=+1
            res[i][j-1]=+1
            res[i-1][j-1]=+1
            
            res[i-1][j+1]=+1
            res[i+1][j-1]=+1
          
            res[i+1][j]=+1
            res[i][j+1]=+1
            res[i+1][j+1]=+1
            

            
        #else:
        #    res[i][j]=k
print(res)
print(type(res[1,1]))
