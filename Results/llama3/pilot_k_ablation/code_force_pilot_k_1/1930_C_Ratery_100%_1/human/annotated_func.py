#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (1 <= n <= 3 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    arr = list(map(sum, enumerate(map(int, input().split()), start=1)))
    arr.sort(reverse=True)
    ans = [arr[0]]
    for x in arr[1:]:
        if x >= ans[-1]:
            ans.append(ans[-1] - 1)
        else:
            ans.append(x)
        
    #State: `n` is an integer, `arr` is a sorted list of `n` integers in descending order, `ans` is a list containing the maximum element of `arr` and a sequence of elements where each element is either the corresponding element in `arr` or one less than the previous element in `ans`, and `x` is the last element in `arr`. If `arr` has only one element, `ans` contains only the maximum element of `arr`.
    print(*ans)
    #This is printed: The maximum element of arr, followed by a sequence of elements where each element is either the corresponding element in arr or one less than the previous element in ans

#Overall this is what the function does:The function reads a sequence of test cases from standard input, where each test case consists of an integer n followed by n integers. It then processes each test case by sorting the integers in descending order, and generates a new sequence where each element is either the corresponding element in the sorted sequence or one less than the previous element in the new sequence. The function prints the maximum element of the sorted sequence followed by the generated sequence.

