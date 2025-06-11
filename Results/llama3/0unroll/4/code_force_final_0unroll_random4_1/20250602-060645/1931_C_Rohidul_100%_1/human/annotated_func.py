#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then t times: first an integer n (1 <= n <= 2 * 10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        le = len(a)
        
        l, r = 0, n - 1
        
        st, end = 1, 1
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        ans = le - max(st, end)
        
        if a[0] == a[-1]:
            ans = max(0, le - (st + end))
        
        print(ans)
        
    #State: The output state will contain the number of non-identical elements in each of the t input sequences, excluding the longest sequence of identical elements at the beginning and end of each sequence. If the first and last elements of a sequence are the same, the output will be the maximum of 0 and the length of the sequence minus the sum of the lengths of the longest sequences of identical elements at the beginning and end.

#Overall this is what the function does:This function reads multiple input sequences from standard input, where each sequence consists of an integer n followed by n integers. It then processes each sequence to count the number of non-identical elements, excluding the longest sequence of identical elements at the beginning and end of each sequence. If the first and last elements of a sequence are the same, it returns the maximum of 0 and the length of the sequence minus the sum of the lengths of the longest sequences of identical elements at the beginning and end. The function prints the result for each input sequence.

