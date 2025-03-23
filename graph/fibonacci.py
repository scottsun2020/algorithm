def fibonacci(n): 
    #create a list of fibonacci number
    fib_num = [0] * n
    fib_num[0] = 1
    fib_num[1] = 1
    for i in range(2, n):
        #calculate a fibonacci number based on the defination
        fib_num[i] = fib_num[i-1] + fib_num[i-2]
    return fib_num

#print a list of 10
print(fibonacci(10))
#output is [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#runtime is O(n) since the array has been created at begin and one iteration of length of array will complete the task