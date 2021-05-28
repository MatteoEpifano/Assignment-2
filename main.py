print("Question 1")
# Get user to input any binary number to be converted to decimal
num = int(input('Type a binary number you would like to convert to decimal: '))

# use equation to convert Binary to Decimal using while loop
def BinaryDecimal(n):  
    n, d, base = n, 0, 1
     #set change = n 
    change = n
    #while change is a binary number
    while(change):
      #Use this equation to make digit equal to change % 10
        digit = change % 10

        #Use this other equation to make change has to equal to change / 10
        change = int(change / 10)
        
        #do d + digit * base
        d += digit * base

        #set base = base * 2 
        base = base * 2

    return d
# display result and print a message saying the final answer
print('The decimal value for this binary is =', BinaryDecimal(num))

print("Question 2 ")
#Get user to enter any amount of words while separating them with a "?"
Words = input("Input a series of words and separate each word with a '?': \n")
 
#Count the amount of "?" to determine the # of words
numberW = (Words.count("?"))

#Replace every "?" after each word with a "space"
space = Words.replace("?"," ")

#print the final results
print ("The Sentence without question marks is:",space,"\nThe total number of words typed is:" ,numberW)

