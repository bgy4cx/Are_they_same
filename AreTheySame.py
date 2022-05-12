# It gave true result if both of the inputs are arries and none of them is none or empty list. 
def IsItInput(i1, i2):
    return isinstance(i1, list) and isinstance(i2, list) and i1 != None and i2 != None

# If the imput is correct than the code check the elements of the arries. In case of empty arries it is true.
def comp(i1, i2):
    counter = 0
    Flag = False
    if IsItInput(i1, i2):
        for y in i2:
            r = [x for x in i1 if y==x*x]
            if r != []:
                counter += 1
                i1.remove(r[0])
        Flag = counter == len(i2) and counter != 0 or i1 == [] and i2 == []
    else:
        Flag = False
    return Flag
