# Return the max of two numbers
def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result

def main():
    i = 5
    j = 2
    k = max(i, j) # Call the max function
    print("The larger number of", i, "and", j, "is", k)

main() # Call the main function
