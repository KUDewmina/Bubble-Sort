array = list(map(int, input("Input array seperated by spaces :").split()))
n = len(array)
for i in range(n):
  for j in range(n-i-1):
    if array[j] > array[j+1]:
      array[j],array[j+1] = array[j+1],array[j]
print(array)
