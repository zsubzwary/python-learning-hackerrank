import re

def checkIfValid(regex):
  is_valid = False
  try:
    re.compile(regex)
    is_valid = True
  except re.error:
    is_valid = False
  return is_valid


num = int(input())
result = []

if(num > 0 and num < 100):
  for i in range(0, num):
    regexToCheck = input()
    output = checkIfValid(regexToCheck)
    result.append(output)

  for item in result:
    print(item)
