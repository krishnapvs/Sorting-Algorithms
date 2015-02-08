def insertionSortIterative(A):
	for i in range(1,len(A)):
		key=A[i]
		j=i-1
		while (A[j]>key) and j>=0:
			A[j+1]=A[j]
			j=j-1
		A[j+1]=key
	return A


A=[9.8,0,3,33,-1,-234,-34]

print insertionSortIterative(A)


