#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 <= n <= 3 * 10^5). The second line of each test case contains n integers a_1,a_2,...,a_{n} (1 <= a_i <= 10^9).
    n = int(input())
    arr = list(map(sum, enumerate(map(int, input().split()), start=1)))
    arr.sort(reverse=True)
    ans = [arr[0]]
    for x in arr[1:]:
        if x >= ans[-1]:
            ans.append(ans[-1] - 1)
        else:
            ans.append(x)
        
    #State: stdin contains multiple test cases minus one, n is an integer, arr is a list of n integers sorted in descending order where each integer is the sum of its 1-based index and its original value, ans is a list containing the largest integer in arr and the rest of the elements in ans are either one less than the last element in ans or the corresponding element in arr whichever is smaller.
    print(*ans)
    #This is printed: the elements of ans (where ans contains the largest integer in arr and the rest of the elements in ans are either one less than the last element in ans or the corresponding element in arr whichever is smaller)

#Overall this is what the function does:This function reads a test case from standard input, where the first line contains the number of elements and the second line contains the elements themselves. It then processes the elements by adding their 1-based index to each element, sorts them in descending order, and constructs a new list where each element is either the corresponding element in the sorted list or one less than the previous element in the new list, whichever is smaller. The function then prints the elements of this new list.

