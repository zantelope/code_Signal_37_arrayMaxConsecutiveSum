def arrayMaxConsecutiveSum(inputArray, k):
    
    ## define sum of initial k elements
    sumK = sum(inputArray[:k])
    
    ## define largest sum of k adjacent elements
    sumM = sumK
    
    ## iterate through inputArray - k
    for i in range(len(inputArray) - k):
    
        ## print statements make it easier to see why this works
        '''print(inputArray)
        print("previous sumK = %d" % sumK)'''
        
        ## subtract previous first element of k sequence, add next
        sumK += (inputArray[i+k] - inputArray[i])

        '''print("inputArray[i+k] = %d" % inputArray[i+k])
        print("inputArray[i] = %d" % inputArray[i])
        print("inputArray[i+k] - inputArray[i] = %d" % (inputArray[i+k] - inputArray[i]))
        print("sumK = %d" % sumK)'''

        ## if sumK is larger than sumM, change sumM to value of sumK
        if sumK > sumM:
            sumM = sumK
    return sumM
