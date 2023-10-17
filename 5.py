s1 = "abcdefG1"
s2 = "CCDDEExy"
s3 = "1234567b"
s4 = "8665"

def processString(input_str):
    output_str = ""
    for char in input_str:
       if char.isnumeric():
            output_str += char * 2
    if len(output_str) > len(input_str):
        return True
    else:
        return False


def deltaDebug(string):
    newArray = list(string) # change string to list to get chars

    for i in range(0, len(newArray)): # check all chars in list
        if processString(newArray[i]): # check if string passes
            print("Character: " + newArray[i])
            print("Fail")
        else:
            print("Pass")


deltaDebug(s1)