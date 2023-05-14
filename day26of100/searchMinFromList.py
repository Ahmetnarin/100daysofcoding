def searchMinFromList(L,n):
    minValue = L[0]
    counter = 1
    while(counter < n):
        v = L[counter]
        if v < minValue:
            minValue = v
            counter+=1
        else:
            counter+=1
    return minValue

my_values = [23,-4,0,73,-10,13,-15,5645,-251]
print(searchMinFromList(my_values, len(my_values)))