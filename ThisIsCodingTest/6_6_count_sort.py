array = []

def count_sort(array):
    counts = [0] * (max(array)+1)
    for i in range(len(array)):
        counts[array[i]] += 1
    
        
    for i in range(len(counts)):
        for j in range(counts[i]):
            print(i, end = ' ')