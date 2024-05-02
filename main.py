import math

x1 = 0.1
x2 = 0.3
y = 0.03

w1 = 0.5
w2 = 0.2
b = 1.83

for i in range(400):
  summation = x1*w1 + x2*w2 + b
  
  prediction = 1 / (1 + math.exp(-summation)) #sigmoid function
  
  error = 0.5 * ((y - prediction) * (y - prediction)) #MSE error
  
  w1 = w1 - 0.05 * error * 0.1 #0.05 is learning rate
  w2 = w2 - 0.05 * error * 0.3
  b = b - 0.05 * error * 1
  
  if (i == 1 or i == 399):
    print(prediction)
    print(error)
