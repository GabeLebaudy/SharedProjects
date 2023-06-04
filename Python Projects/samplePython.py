#Import modules
import math

#Functions
def sampleFunction(num1, num2):
    finalNum = math.sqrt(num1 * num2)
    return finalNum

#Main Script
if __name__ == "__main__":
    sampleNum = sampleFunction(10, 10)
    print(sampleNum)
    