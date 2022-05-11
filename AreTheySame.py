# It gave true result if both of the inputs are arries. 
def IsItInput(i1, i2):
    return isinstance(i1, list) and isinstance(i2, list)

def IsItNotEmpty(i):
    return i != [] and i != None