def findMin1(arr, i, sumCalculated, sumTotal):
    if (i == 0):
        return abs((sumTotal - sumCalculated) - sumCalculated)

    return min(findMin1(arr, i - 1, sumCalculated + arr[i - 1], sumTotal),
               findMin1(arr, i - 1, sumCalculated, sumTotal))


def findMin2(arr, l):
    sumTotal = 0
    for i in range(l): sumTotal += arr[i]
    return findMin1(arr, l, 0, sumTotal)


if __name__ == "__main__":
    arr = [3, 4, 5, 3, 100, 1, 83, 54, 23, 20]
    l = len(arr)
    print("The minimum difference " + "between two sets is ", findMin2(arr, l))
