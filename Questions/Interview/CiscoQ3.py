"""



"""


def checkIPValidity(addressIP):
    # Write your code here
    list = addressIP.split(".")
    print(list)
    print(type(list))
    for i in list:
        if int(i) < 0 or int(i) > 255:
            return False
    return True

print(checkIPValidity("255.3.2.256"))