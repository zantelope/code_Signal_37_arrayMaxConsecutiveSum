def arrayMaxConsecutiveSum(inputArray, k):
    
    largestSum = 0
    sumLast = 0
    sumBefore = 0


    for i in range(len(inputArray) - (k - 1)):
      print(sumLast)
      sumLast = sumBefore + inputArray[k+i-1] - inputArray[i-1]
    return sumLast
