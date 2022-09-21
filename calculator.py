# Claculator file, contains static methods for all calculator functionality
def addition(num1, num2):
    if (isinstance(num1, int, float) & isinstance(num2, int, float)):
        return(num1 + num2)
    else:
        return("err")