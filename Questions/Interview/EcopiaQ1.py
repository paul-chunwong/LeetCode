"""


"""


def getLargestNumber(num):
    # Write your code here
    list1 = list(num)
    while True:
        i = 0
        while i < len(list1) - 1:
            if int(list1[i + 1]) > int(list1[i]):
                if int(list1[i + 1]) % 2 == 0 and int(list1[i]) % 2 == 0:
                    temp = list1[i]
                    list1[i] = list1[i + 1]
                    list1[i + 1] = temp
                    break
                elif int(list1[i + 1]) % 2 == 1 and int(list1[i]) % 2 == 1:
                    temp = list1[i]
                    list1[i] = list1[i + 1]
                    list1[i + 1] = temp
                    break
            i = i + 1
            if i == len(list1)-1:
                strResule = ""
                for s in list1:
                    strResule = strResule + s
                return strResule


print(getLargestNumber("7596201"))
