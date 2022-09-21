# Claculator file, contains static methods for all calculator functionality

# Division of two numbers, note: throws exception if y = 0
def division(x: float, y: float) -> float:
    return x/y

def addition(num1, num2):
    if (isinstance(num1, int, float) & isinstance(num2, int, float)):
        return(num1 + num2)
    else:
        return("err")
