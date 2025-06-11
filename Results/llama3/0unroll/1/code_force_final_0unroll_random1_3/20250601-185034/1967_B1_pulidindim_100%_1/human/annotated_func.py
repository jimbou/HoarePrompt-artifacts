#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a positive integer t (1 <= t <= 10^4). Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: The output state will be the sum of the number of integers in the range [1, n] that are divisible by each integer from 2 to m (inclusive), for each test case. The sum is calculated by iterating over each integer from 2 to m, and for each integer, adding the number of multiples of that integer in the range [1, n] to the total sum. The number of multiples is calculated by dividing n by the current integer, and then adding 1 if the result is not an integer. The loop breaks if the number of multiples is less than the current integer.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates the sum of the number of integers in the range [1, n] that are divisible by each integer from 2 to m (inclusive), and prints the result. The calculation is done by iterating over each integer from 2 to m, counting the number of multiples of that integer in the range [1, n], and adding it to the total sum. The function handles multiple test cases and prints the result for each case.

