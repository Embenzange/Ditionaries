def number_length(num):
#Convert interger to string
	return(num_length)
num = int(input("Please enter a number: "))
num_str = str(num)
num_length = 0
for i in num_str:
		num_length += 1
    
result = number_length(num)
print(f"The length of {num} is {result}")