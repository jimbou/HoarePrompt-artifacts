def count_beautiful_pairs(test_cases):
    results = []
 
    for n, x, y, arr in test_cases:
        count = 0
        mod_x = {}
        mod_y = {}
 
        for num in arr:
            # Remainders needed for conditions
            rem_x = (-num) % x
            rem_y = (num % y)
 
            # Count valid pairs based on previously seen elements
            count += mod_x.get(rem_x, 0) and mod_y.get(rem_y, 0)
 
            # Update the dictionaries
            mod_x[num % x] = mod_x.get(num % x, 0) + 1
            mod_y[num % y] = mod_y.get(num % y, 0) + 1
 
        results.append(count)
 
    return results
 
 
# Input and output handling
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
 
    t = int(data[0])
    test_cases = []
    idx = 1
 
    for _ in range(t):
        n, x, y = map(int, data[idx].split())
        arr = list(map(int, data[idx + 1].split()))
        test_cases.append((n, x, y, arr))
        idx += 2
 
    results = count_beautiful_pairs(test_cases)
 
    for result in results:
        print(result)
 
 
if __name__ == "__main__":
    main()