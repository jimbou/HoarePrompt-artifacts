#State of the program right berfore the function call: x and n are integers such that 1 <= x < n <= 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: Output State: `output1` contains all divisors of `x` that are less than or equal to the square root of `x`, and `output2` contains the corresponding quotients for each divisor in `output1`.
    output1.reverse()
    return output2 + output1
    #The program returns a list that is the concatenation of `output2` (which contains the corresponding quotients for each divisor in the reversed `output1`) and `output1` (which contains all divisors of `x` that are less than or equal to the square root of `x`, in reverse order)
#Overall this is what the function does:The function accepts an integer `x` and returns a list containing all divisors of `x` that are less than or equal to the square root of `x`, in reverse order, followed by their corresponding quotients.

