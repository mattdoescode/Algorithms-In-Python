def insertion_sort(input):
    for index in range(1, len(input)):
        valueToAdd = input[index]
        currentPos = index

        while currentPos > 0 and input[currentPos - 1] > valueToAdd:
            input[currentPos] = input[currentPos - 1]
            currentPos = currentPos - 1
        
        array[currentPos] = valueToAdd

    return input

def insertion_sort_explained(input):
    print("initial array: ", input)
    for index in range(1, len(input)):
        valueToAdd = input[index]
        currentPos = index
        print("looking at ", valueToAdd, " in position ", currentPos)
        
        while currentPos > 0 and input[currentPos - 1] > valueToAdd:
            input[currentPos] = input[currentPos - 1]
            currentPos = currentPos - 1
            print("previous value in array is larger shifting it 1 position. Looking at new element.")
        
        array[currentPos] = valueToAdd
        print("added ", valueToAdd ," to array")
        print("array now looks like ", input)

    return input

# array = [4,5,6,2,6,69,7,2,7,8,2,3,57,13]
array = [4,7,1,3,9,2,7]


print(insertion_sort_explained(array))





