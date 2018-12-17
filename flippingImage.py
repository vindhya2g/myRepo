A = [[1,1,0],[1,0,1],[0,0,0]]

for i in range(len(A)):
	A[i].reverse()
	for j in range(len(A[i])):
		if A[i][j] == 0:
			A[i][j] = 1
		elif A[i][j] == 1:
			A[i][j] = 0	

print(A)	



		
