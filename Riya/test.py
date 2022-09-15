'''def findMinRec(arr, i, sumCalculated, sumTotal):

    if (i == 0):
        return abs((sumTotal - sumCalculated) -
                   sumCalculated)

    return min(findMinRec(arr, i - 1, sumCalculated + arr[i - 1], sumTotal),
    findMinRec(arr, i - 1, sumCalculated, sumTotal))

def findMin(arr, n):
    if __name__ == "__main__":
        arr = [20, 10, 40, 20, 25, 15,14,10]
        sort(arr)
        n = len(arr)
    print(len(n))
    print("The minimum difference " +
              "between two sets is ",
              findMin(arr, n))
'''

# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/


'''u = input('Enter a string:')
u1 = str.replace("str" ,  "fyj" )
print(u1)'''

'''s="Hello$ Python3$"
s1=s.replace("$","")
print (s1)'''

'''u=input('Enter a string:')
import re
u1=re.sub("is","",u)
print (u1)'''

'''u=str(input('Enter a string:'))
temp = u.split()
print(u)
result=[]
i=len(temp)
#print(i)
while i>=0:
    result.replace("is","",u)
    i=i+1
print(result)
output=''.join(result)
print(output)'''


'''def minimumDifference(self, nums: list[int]) -> int:
    total = sum(nums)
    l = len(nums)
    if l == 2:
        return abs(nums[0] - nums[1])

    # obtain the sum of possible 0 to l//2 numbers
    # to reduce complexity
    s1 = self.kSum(nums[0:l // 2])
    s2 = self.kSum(nums[l // 2:l])

    # if the sum of each party is target, then the difference is the smallest
    target = total / 2
    ans = inf
    for i in range(l // 2):
        j = l // 2 - i
        # find in s1[i] and s2[j] which number is closest to target
        y = len(s2[j]) - 1
        for x in s1[i]:
            while y >= 0:
                ans = min(ans, abs(total - 2 * (x + s2[j][y])))
                if s2[j][y] + x > target:
                    y -= 1
                else:
                    break
    return ans


def kSum(self, nums: list[int]) -> list[list]:
    l = len(nums)
    s = [0] * (l + 1)
    # use sets to avoid duplicates
    for i in range(l + 1):
        s[i] = set()
    n = 0
    s[0].add(0)
    for i in nums:
        j = n
        while j >= 0:
            for element in s[j]:
                s[j + 1].add(element + i)
            j -= 1
        n += 1

    # sort it
    for i in range(len(s)):
        s[i] = sorted(list(s[i]))
    return s


'''string1=input("Enter a string:")
string2="is"
characters=string2
new=filter(lambda i: i not in characters,string1)
new_string1=""
for i in new:
    new_string1+=i
    print(new_string1)'''
    
    
    

