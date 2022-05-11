# It gave true result if both of the inputs are arries and none of them is none or empty list. 
def IsItInput(i1, i2):
    return isinstance(i1, list) and isinstance(i2, list) and IsItNotEmpty(i1) != False and IsItNotEmpty(i2) != False

# It gave false result if the inputs is none or empty list. 
def IsItNotEmpty(i):
    return i != [] and i != None