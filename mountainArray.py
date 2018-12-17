A= [0,2,1,0]

B = sorted(A)

highest = B[-1]

print(highest)
i = 0
for a in A:
	if a == highest:

		print(i)
		break
	i += 1

	

