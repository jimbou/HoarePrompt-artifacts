def func_1(t, test_cases):
    results = []
    for i in range(t):
        (n, arr) = test_cases[i]
        arr.sort()
        median_index = n // 2
        current_median = arr[median_index]
        heap = arr[median_index:]
        heapq.heapify(heap)
        operations = 0
        while heap[0] <= current_median:
            smallest = heapq.heappop(heap)
            heapq.heappush(heap, smallest + 1)
            operations += 1
        results.append(operations)
    return results
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    test_cases = []
    for _ in range(t):
        n = int(data[index])
        arr = list(map(int, data[index + 1:index + 1 + n]))
        test_cases.append((n, arr))
        index += 1 + n
    results = func_1(t, test_cases)
    for result in results:
        print(result)