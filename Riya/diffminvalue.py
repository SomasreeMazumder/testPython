

def findMinimumValue(arr, i, sumCalculated, sumTotal):
    if (i == 0):
        return abs((sumTotal - sumCalculated) - sumCalculated)
    return min(findMinimumValue(arr, i - 1, sumCalculated + arr[i - 1], sumTotal),
                findMinimumValue(arr, i - 1, sumCalculated, sumTotal))
def findMinValue(arr, l):
    sumTotal = 00
    for i in range(l): sumTotal += arr[i]
    return findMinimumValue(arr, l, 0, sumTotal)
if __name__ == "main":
    arr = [3, 4, 5, 3, 100, 1, 83, 54, 23, 20]
    l = len(arr)
    print("The minimum difference " + "between two sets is ", (arr, l))