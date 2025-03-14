#State of the program right berfore the function call: The function `func_1` is expected to take input parameters, but the provided function definition does not include any. The correct function definition should include parameters for the number of test cases `t`, the length of the array `n`, and the array `a` itself. The input should be such that 1 ≤ t ≤ 10^4, 1 ≤ n ≤ 3·10^5, and 1 ≤ a_i ≤ n, with the additional constraint that the array `a` is beautiful in every test case, and the sum of `n` over all test cases does not exceed 3·10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `n` is an input integer, `arr` is a list of integers read from input, `flag` is True if all elements in `arr` from index 1 to `n-1` are equal to the element at index 0, otherwise `flag` is False, and `i` is `n-1` if the loop completes without breaking, otherwise `i` is the index where the first inequality was found.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `n` is an input integer, `arr` is a list of integers read from input, `flag` is True if all elements in `arr` from index 1 to `n-1` are equal to the element at index 0, otherwise `flag` is False, `i` is `n-1` if the loop completes without breaking, otherwise `i` is the index where the first inequality was found, `ans` is the minimum of the lengths of consecutive sequences of `val` in `arr` if any inequality was found, otherwise `ans` remains Decimal('Infinity'), `val` is `arr[0]`, `cnt` is the length of the last consecutive sequence of `val` in `arr` if the loop completes without breaking, otherwise `cnt` is 0.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0
    #State: *`n` is an input integer, `arr` is a list of integers read from input, `val` is `arr[0]`. If `flag` is True, `i` is `n-1`, `ans` is the minimum of `Decimal('Infinity')` and `cnt`, and `cnt` is the length of the last consecutive sequence of `val` in `arr`. If `flag` is False, `i` is the index where the first inequality was found, `ans` is the minimum of the lengths of consecutive sequences of `val` in `arr`, and `cnt` is 0.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the input. It checks if all elements in `arr` are equal. If they are, it prints `-1`. Otherwise, it calculates the minimum length of consecutive sequences of the first element in `arr` and prints this value. The function does not return any value.

