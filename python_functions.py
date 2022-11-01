def sum_to(n):
  sum = 0
  for n in range(1, n + 1):
    sum += 1
  return sum  

sum_to(20)  


def largest(nums):
  highest = 0
  for num in nums:
    if num > highest:
      highest = num
  return  highest

largest([5, 10, 15])  


def occurrences(str, l):
  letters = str.replace(l, '')
  return (len(str) - len(letters)) // len(l)

occurrences('pepper', 'p')  


def product(*args):
  mult = 1
  for arg in args:
    mult *= arg
  return mult  

product(2,7,3)