def Cube (number):
    return number*number*number
def X (number):
   if number%3==0:
      return Cube(number)
   else:
      return False
print(X(9))
print(X(8))