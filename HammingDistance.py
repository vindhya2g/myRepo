x = 680142203
y = 1111953568


a = "{:032b}".format(x)
b = "{:032b}".format(y)


k = 0
for i,j in zip(a,b):
	if i != j :
		k += 1

print(k)





