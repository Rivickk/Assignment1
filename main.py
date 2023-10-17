import random

testCaseArray = []

def insertionSort(array):
    for i in range(1, len(array)): #loop through list taking the length
        element = array[i] # the element to be sorted
        compare = i - 1 # the element to compare against to check if its greater than or less

        while array[compare] > element: # this check creates the bug, the if statement and array ccompare should be both checked against the element, otherwise
            # it continues with a new sorting list to fix, compare the if statement with the element size as well
            if compare >= 0: # shift values
                array[compare + 1] = array[compare]
                compare -= 1
            else:
                array[compare + 1] = element #key needs to be in right position
                return array
        array[compare + 1] = element
    return array

unsortedArray = [1,4,2,7,5,9,8,12,13]


def testCaseGen(array):
    i = random.randint(3,11) #random length
    while i >= 3:
        testCaseArray.append(random.randint(5,100)) #random integer input
        i -= 1
    return array


if __name__ == '__main__':
    #print(insertionSort(unsortedArray))
    if insertionSort(testCaseGen(testCaseArray)) == sorted(testCaseArray):
        print(testCaseArray)
        print("Pass")
    else:
        print(testCaseArray)
        print("Fail")


