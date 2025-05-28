def addmultiplenumbers(numbers): 
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(num):
   if (num % 2 == 0):
    return True
   else:
      return False 


def isitaninteger(num):
    if isinstance(num, int):
       return True
    if isinstance(num, float):
      if num.is_integer():
        return True
    else:
        return False

print(isitaninteger(7.3))