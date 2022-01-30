import sys

data = sys.stdin.readlines()

firstline = data[0].split()

l = int(firstline[0])
d = int(firstline[1])
n = int(firstline[2])

pos = []

for i in range(n):
	num = data[1+i][:-1]
	pos.append(int(num))

def mergeSort(arr):
        if len(arr) > 1:
                middle = len(arr)//2
                left = arr[:middle]
                right = arr[middle:]
                mergeSort(left)
                mergeSort(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                        if left[i] < right[j]:
                                arr[k] = left[i]
                                i += 1
                        else:
                                arr[k] = right[j]
                                j += 1
                        k += 1

                while i < len(left):
                        arr[k] = left[i]
                        i += 1
                        k += 1

                while j < len(right):
                        arr[k] = right[j]
                        j += 1
                        k += 1

mergeSort(pos)
max = 0
x = 6
bird = 0
while x <= (l-6):
	if bird < len(pos):
		if x > (pos[bird] - d) and x < (pos[bird] + d):
			x = pos[bird] + d
			bird += 1
		else:
			max += 1
			x += d
	else:
		max += 1
		x += d
print(max)
