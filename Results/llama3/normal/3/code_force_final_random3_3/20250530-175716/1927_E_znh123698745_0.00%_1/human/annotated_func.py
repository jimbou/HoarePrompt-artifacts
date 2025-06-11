#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers n and k (2 <= k <= n <= 2 * 10^5), where k is even.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        array = list(range(1, n + 1))
        
        answer = [1]
        
        a = [1, -1]
        
        for i in range(1, n):
            if (-1) ** i == -1:
                answer.append(array[a[-1]])
                a[-1] -= 1
            else:
                answer.append(array[a[0]])
                a[0] += 1
        
        print(*answer)
        
    #State: The loop has finished executing, and the final output state is that the loop has iterated over all the input test cases. The variables n and k have been updated to the last input test case, array is a list of integers from 1 to n, answer is a list of integers from 1 to n in alternating order starting from 1, a is a list containing the integers n and -1, stdin is empty, and the list of integers from 1 to n in alternating order starting from 1 is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k, and generates a list of integers from 1 to n in alternating order starting from 1. It then prints this list for each test case. The function iterates over all input test cases, updating the variables n and k accordingly, and finally prints the list of integers in alternating order for the last test case.

