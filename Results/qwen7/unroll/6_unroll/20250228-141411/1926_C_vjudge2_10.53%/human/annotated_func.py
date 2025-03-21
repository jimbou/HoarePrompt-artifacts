#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: Output State: `t` integers are read from the input and added to the list `numbers`. The list `numbers` contains these `t` integers.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: Output State: The list `numbers` contains `t` integers; the list `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; the list `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]; `total` is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: Output State: The list `numbers` contains `t` integers; the list `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; the list `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 1, 4, 7, 10, 15, 21, 28, 36, 45, 55]; `total` is 55.
    for n in numbers:
        print(sum_values[n])
        
    #State: Output State: The list `numbers` contains `t` integers; the list `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; the list `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 1, 4, 7, 10, 15, 21, 28, 36, 45, 55]; `total` is 55. During the loop execution, the values from the `values` list are printed based on the indices specified in the `numbers` list, but the lists and the total variable remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves reading an integer `t` (1 ≤ t ≤ 10^4) and `t` integers `n` (1 ≤ n ≤ 2·10^5). It then constructs two lists, `values` and `sum_values`, based on these integers and a predefined sequence. Finally, it prints the values from the `sum_values` list corresponding to the integers read in the test cases. The function does not return any value but modifies and uses global lists `values` and `sum_values` and an integer `total` during its execution.

