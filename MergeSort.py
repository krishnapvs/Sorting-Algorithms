# writing the code for merge sort

def MergeSort(A):
	if len(A)<=1:
		return A
	mid=len(A)/2
	first=MergeSort(A[:mid])
	last=MergeSort(A[mid:])
	return Merge(first,last)

def Merge(first, last):
	i,j=0,0
	a=[]
	while i<len(first) and j <len(last):
		if first[i] <= last[j]:
			a.append(first[i])
			i+=1
		else:
			a.append(last[j])
			j+=1
			
	while i<len(first):
		a.append(first[i])
		i+=1

	while j<len(last):
		a.append(last[j])
		j+=1

	return a

#Testing the code
A=[3,2,6,7,2,5,1,54,124,76,23]
print MergeSort(A)
print A
