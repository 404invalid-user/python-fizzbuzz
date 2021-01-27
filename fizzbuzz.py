m3 = []
m5 = []
for x in range(101):
  m3.append(x * 3)
  m5.append(x * 5)
  if x in m3 and x in m5:
      print("fizzbuzz")
  elif x in m3:
      print("fizz")
  elif x in m5:
    print("buzz")
  else:
      print(x)
