def prime_number():
 listOfPrimeNumbers = []
 for currentNumber in range(1, 251):
   dividableNumbers = 0
   for num in range(1, currentNumber + 1):
     if currentNumber % num == 0: 
       dividableNumbers += 1  
   if dividableNumbers < 3: 
     listOfPrimeNumbers.append(currentNumber)
 return listOfPrimeNumbers
  
# def prime_number():
#  for currentNumber in range(1, 251):
#    dividableNumbers = 0
#    for num in range(1, currentNumber + 1):
#      if currentNumber % num == 0:
#         dividableNumbers += 1
#   #  print(f'{currentNumber} ==> {dividableNumbers}')
  
#    if dividableNumbers < 3:
#     print(currentNumber)
   
# prime_number()
