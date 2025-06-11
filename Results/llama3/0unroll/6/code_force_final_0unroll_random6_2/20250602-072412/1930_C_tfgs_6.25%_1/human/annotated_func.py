#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The first integer is a positive integer (>= 1) and represents the length of the list. The list contains integers (>= 1) and its length is equal to the first integer. The sum of the lengths of all lists does not exceed 3 * 10^5.
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: The list 'a' contains elements that are the sum of the original elements and their 1-based index plus one, and 'n' remains unchanged.
    counter = Counter(a)
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, counter[a[i - 1]])
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            counter[a[i - 1]] -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
    #State: Output State: The list 'a' remains unchanged, 'n' remains unchanged, 'counter' contains the frequency of each element in the original list 'a' minus the number of times each element was appended to 'ans', 'cnt' is 0, and 'ans' contains all elements from the original list 'a' in descending order, with each element repeated a number of times equal to its frequency in the original list, and with all missing numbers between the elements of the original list 'a' inserted in descending order.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: The list 'a' remains unchanged, 'n' remains unchanged, 'counter' contains the frequency of each element in the original list 'a' minus the number of times each element was appended to 'ans', 'cnt' is 0, and 'ans' contains all elements from the original list 'a' in descending order, with each element repeated a number of times equal to its frequency in the original list, with all missing numbers between the elements of the original list 'a' inserted in descending order, and with 'cnt' number of elements decremented by 1 appended at the end.
    print(*ans)
    #This is printed: All elements from the original list 'a' in descending order, with each element repeated a number of times equal to its frequency in the original list, with all missing numbers between the elements of the original list 'a' inserted in descending order, and with 'cnt' number of elements decremented by 1 appended at the end.

#Overall this is what the function does:The function reads input from stdin, processes it, and prints the processed output. It accepts no parameters and returns no value. The function takes multiple test cases as input, where each test case consists of a positive integer (n) representing the length of a list, followed by a list of integers. The function modifies the list by adding the 1-based index plus one to each element, removes duplicates, sorts the list in descending order, and then reconstructs the list by inserting missing numbers between the elements and repeating each element a number of times equal to its frequency in the original list. Finally, it appends any remaining missing numbers at the end of the list and prints the resulting list.

