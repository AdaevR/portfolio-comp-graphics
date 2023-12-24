import numpy

user_input = numpy.array([])
transform = numpy.array([[1, 3], [4, 1]])

print("Enter x and y:")
for i in range(2):
    element = int(input())
  
    user_input = numpy.append(user_input, element)
output = numpy.matmul(user_input, transform)

print("User input", user_input)
print("Transform", transform)
print("Output", output)
