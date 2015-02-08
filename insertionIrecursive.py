# insertion recursive

def insertionSortRecursive(A,n):
	if n>1:
		insertionSortRecursive(A,n-1)
		key=A[n-1]
		i=A[n-2]
		while i>=0 and key<A[i]:
			A[i+1]=A[i]
			i-=1
		A[i+1]=key
	return A


A=[9.8,0,3,33,-1,-234,-34]

print insertionSortRecursive(A,len(A))
