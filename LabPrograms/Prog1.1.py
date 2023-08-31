import time
import numpy.random as np
import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        L, M = arr[:r], arr[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            arr[k], i, j, k = (L[i], i + 1, j, k + 1) if L[i] < M[j] else (M[j], i, j + 1, k + 1)
        while i < len(L):
            arr[k], i, k = L[i], i + 1, k + 1
        while j < len(M):
            arr[k], j, k = M[j], j + 1, k + 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def selectionSort(arr):
    size = len(arr)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[step], arr[min_idx] = arr[min_idx], arr[step]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1], j = arr[j], j - 1
        arr[j + 1] = key

def read_Input():
    n = int(input("Enter the number of TV Channels: "))
    return [int(input(f"Enter the number of viewers of Channel {i+1}: ")) for i in range(n)]

methods = [mergeSort, quickSort, selectionSort, insertionSort]
labels = ["Merge Sort", "Quick Sort", "Selection Sort", "Insertion Sort"]
ch = int(input("1. Merge Sort\n2. Quick Sort\n3. Selection Sort\n4. Insertion Sort\nChoose your Algorithm: "))-1
array = read_Input()
method, labeldata= methods[ch], labels[ch]
method(array)
print('Sorted Array is:')
print(array)

print("******************Running Time Analysis*******************")
elements, times = [], []
for i in range(1, 10):
    array = np.randint(0, 1000 * i, 1000 * i)
    start = time.time()
    method(array.copy())
    end = time.time()
    print(len(array), "Elements Sorted by", labeldata, end - start)
    elements.append(len(array))
    times.append(end - start)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements, times, label=labeldata)
plt.grid()
plt.legend()
plt.show()