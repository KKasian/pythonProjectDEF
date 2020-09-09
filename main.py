def mathem (a, b, c):
 try:
  sum = a + b
  if sum > c:
   print ("the sum of the first and second arguments is greater than the third")
  elif sum <= c:
   print ("the sum of the first and second arguments is less than the third")
  else:
   print ("not valid Data")
 except:
  print("not valid Data")
