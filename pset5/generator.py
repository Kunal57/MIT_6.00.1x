def genPrimes():
  primeNumbers = [2]
  count = 2
  yield count
  while True:
    prime = True
    for num in primeNumbers:
      if count % num == 0:
        prime = False
    if prime == True:
      primeNumbers.append(count)
      yield count
    else:
      count += 1


x = genPrimes()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())



