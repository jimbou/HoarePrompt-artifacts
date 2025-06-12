#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains one integer (n) and the second line contains n space-separated integers. n is a positive integer and each integer in the second line is a positive integer less than or equal to 10^9.
    n = int(input())
    arr = list(map(sum, enumerate(map(int, input().split()), start=1)))
    arr.sort(reverse=True)
    ans = [arr[0]]
    for x in arr[1:]:
        if x >= ans[-1]:
            ans.append(ans[-1] - 1)
        else:
            ans.append(x)
        
    #State: `n` is a positive integer, `arr` is a list of `n` positive integers less than or equal to 10^9, sorted in descending order, with each element being the sum of its original value and its 1-based index, `ans` is a list containing the largest element of `arr` and the largest `n-1` elements of `arr` (or `arr` minus 1 if the element is greater than or equal to the largest element in `arr`), `x` is the last element in the list, stdin contains multiple test cases minus one. If `arr` has only one element, `ans` is a list containing the largest element of `arr`.
    print(*ans)
    #This is printed: The largest element of arr and the largest n-1 elements of arr (or arr minus 1 if the element is greater than or equal to the largest element in arr)

#Overall this is what the function does:This function reads a test case from standard input, where the first line contains a positive integer n, and the second line contains n space-separated positive integers. It then processes these integers by adding their 1-based index to each value, sorts them in descending order, and generates a new list containing the largest element and the largest n-1 elements (or the element minus 1 if it's greater than or equal to the largest element). Finally, it prints this new list. The function repeats this process for multiple test cases provided in the input.

