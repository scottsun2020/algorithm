def fibonacci(n): 
    #create a list of fibonacci number
    fib_num = [0] * n
    fib_num[0] = 1
    fib_num[1] = 1
    for i in range(2, n):
        #calculate a fibonacci number based on the defination
        fib_num[i] = fib_num[i-1] + fib_num[i-2]
    return fib_num

#print a list of 5
print(fibonacci(10))