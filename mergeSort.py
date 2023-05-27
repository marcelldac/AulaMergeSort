'''

len() : Tamanho do array

Função lambda : 

Ex.: soma = lambda x, y: x + y
print(soma(2, 3))

'''

def merge(a,b,compare):
	result = [] 
	i,j = 0,0
	while (i < len(a) and j < len(b)):
		if compare(a[i],b[j]):
			result.append(a[i])
			i += 1
		else:
			result.append(b[j])
			j += 1
	while (i < len(a)):
		result.append(a[i])
		i += 1
	while (j < len(b)):
		result.append(b[j])
		j += 1
	return result

def merge_sort(arr, compare = lambda x, y: x < y):
	if len(arr) < 2:
		return arr[:] # Shallow Copy
	else:
		middle = len(arr) // 2 
		a = merge_sort(arr[:middle], compare)
		b = merge_sort(arr[middle:], compare)
		return merge(a, b, compare) 

arr = [1,13,2,52,342,4,13,1,31,2]
print(merge_sort(arr))
