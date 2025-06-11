#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers. The integer is a positive integer and does not exceed 3 * 10^5. The sum of n over all test cases does not exceed 3 * 10^5. The integers in the list are positive integers and do not exceed 10^9.
    n = int(input())
    arr = list(map(sum, enumerate(map(int, input().split()), start=1)))
    arr.sort(reverse=True)
    ans = [arr[0]]
    for x in arr[1:]:
        if x >= ans[-1]:
            ans.append(ans[-1] - 1)
        else:
            ans.append(x)
        
    #State: `n` is a positive integer not exceeding 3 * 10^5, `arr` is an empty list, `ans` is a list containing the largest integer in the original `arr`, the second largest integer in the original `arr`, and a sequence of integers where each integer is either one less than the previous integer or the current value of `x` if `x` is less than the previous integer, `x` is not defined, stdin contains no test cases.
    print(*ans)
    #This is printed: [undefined, undefined, sequence of undefined integers]

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of a positive integer n and a list of n positive integers. It then processes the list by sorting it in descending order and generating a new list where each element is either one less than the previous element or the current element if it is less than the previous element. The function prints the generated list to standard output.

