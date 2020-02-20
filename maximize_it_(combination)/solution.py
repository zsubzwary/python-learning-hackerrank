# !!__WARNING__!! 
# This is the worst case solution for this problem!
# It makes all possible combinations and then take out the answer.

import itertools

inpuut = input()
inpuut = inpuut.split(' ')
K = int(inpuut[0])
M = int(inpuut[1])

lisst = []
allPossibleAnswers = []

if ( (K>=1 and K<=7) and (M>=1 and M<=1000 ) ):
  for indexOne in range (0, K):
    nth = input()
    nth = nth.split(' ')
    
    #Below loop converts indiviual strings to integers.
    for indexTwo in range(0, len(nth)): 
      nth[indexTwo] = int(nth[indexTwo])
    
    del nth[0] #This line deletes the value present at index 0
    lisst.append(nth)

  allCombo = list(itertools.product(*lisst))

  for tuplle in allCombo:
    res = []
    for num in tuplle:
      num = num * num
      res.append(num)
    res = sum(res)
    S = res % M
    allPossibleAnswers.append(S)

  print(max(allPossibleAnswers))
