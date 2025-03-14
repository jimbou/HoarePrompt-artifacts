#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2⋅10^6.
def func():
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
        
    #State: Output State: `count` is equal to `m + 1`, `i` is equal to `t - 1`, `n` is the input integer provided by the user, `m` is the input integer such that 1 ≤ `m` ≤ 10^4, `countmins` is equal to `m`, `g` is 0, and `ans` is the initial value of `n` plus the sum of the contributions from each iteration of the loop for all `i` from 0 to `t - 1`.
    #
    #In natural language, after the loop executes all its iterations, the following will be true:
    #- `count` will be `m + 1` because the loop increments `count` until it exceeds `m`.
    #- `i` will be `t - 1` because the loop iterates `t` times, and `i` is the loop counter.
    #- `n` will remain the input integer provided by the user.
    #- `m` will remain the input integer such that 1 ≤ `m` ≤ 10^4.
    #- `countmins` will be `m` because it is initialized as `count - 1` and `count` becomes `m + 1` at the end of the loop.
    #- `g` will be 0 because the loop breaks when `g` becomes less than `countmins`.
    #- `ans` will be the initial value of `n` plus the sum of the series where each term is `int(int(n / i) / i) + 1` for `i` ranging from 2 to `m`, inclusive, for all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers \( n \) and \( m \). For each test case, it calculates a result based on \( n \) and updates it according to a specific formula involving \( m \). The function prints the final result for each test case. After processing all test cases, it ensures that the sum of \( n \) and \( m \) across all test cases does not exceed \( 2 \times 10^6 \).

