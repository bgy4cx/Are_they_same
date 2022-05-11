# It gave true result if both of the inputs are arries and none of them is none or empty list. 
def IsItInput(i1, i2):
    return isinstance(i1, list) and isinstance(i2, list) and IsItNotEmpty(i1) != False and IsItNotEmpty(i2) != False

# It gave false result if the inputs is none or empty list. 
def IsItNotEmpty(i):
    return i != [] and i != None

def comp(i1, i2):
    counter = 0
    for y in i2:
        for x in i1:
            if y == x*x:
                print(y, x)
                counter += 1
                break
    print(i2, counter)
    return counter == len(i2) and counter != 0

