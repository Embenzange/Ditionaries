#Create a function that takes a number num and returns its length.
def num_length(num):
    # Convert the number to a string and find its length
    num_str = str(num)
    length = len(num_str)
    
    return length

number = int(input("Please enter a number: "))
result = num_length(number)
print(f"The length of {number} is {result}")


