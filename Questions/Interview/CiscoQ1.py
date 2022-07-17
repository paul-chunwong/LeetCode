"""

"""


def meanAndMode(inputArr):
    # Write your code here
    numOfArr = len(inputArr)
    sum = 0

    for i in inputArr:
        sum = sum + i

    maxCount = 0
    i = 0
    while i < numOfArr:
        print(inputArr.count(inputArr[i]))
        print(inputArr.count(inputArr[maxCount]))
        print(inputArr[maxCount])
        print(inputArr[i])
        if inputArr.count(inputArr[i]) >= inputArr.count(inputArr[maxCount]):
            if inputArr.count(inputArr[i]) == inputArr.count(inputArr[maxCount]):
                if inputArr[maxCount] > inputArr[i]:
                    maxCount = i
            else:
                maxCount = i
        i = i + 1

    mode = inputArr[maxCount]

    return [round(sum / numOfArr, 2), round(mode,2)]


print(meanAndMode([-4,-4,3,3,0,0,0,-4,-5,8,8,8,8,-9,-9,-9,-9]))
