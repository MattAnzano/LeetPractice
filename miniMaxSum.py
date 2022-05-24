def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minSum = 0
    maxSum = 0
    #min value 
    for i in range(0,len(arr)- 1):
        minSum += arr[i]
    
    #max value
    for i in range(1, len(arr)):
        maxSum += arr[i]
    
    print(str(minSum) + " " + str(maxSum))
