#Even or Odd
def even_or_odd(number):
    if number % 2 ==  0:
        return "Even"
    else:
        return "Odd"
#I use the if else function to determine that if the input number is equal % 2 , its even. else if the number is not, it would be odd.
    
#Removing Spaces
def no_space(x):
    return x.replace(" ", "") 
#I typed a function that removes spaces from the string (x). I used the .replace ti replace the spaces(" ") with empty string ("")

#Turning integers into a string
def number_to_string(num):
    return str(num)
num = 123
string = number_to_string(num)
print(string)
#For this function I put the value(num) to be 123 and string to equal number_to_string(num). If I preinted string it would just give me the value of string. I added return with the function str(nuu) in order to make sure it executes the function.

