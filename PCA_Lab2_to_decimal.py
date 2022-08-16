dict2 = {
  '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
  '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 
  'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 
  'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 
  'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 
  'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35
}

def to_decimal(s, b):
  L_ist = []
  for digit in s:
    L_ist.append(dict2[digit])
  power = len(L_ist) - 1 #exponent
  count_elem = 0 #element digits
  ans = 0
  
  while power >= 0:
    ans += L_ist[count_elem] * (b**power)
    power -= 1
    count_elem += 1
    
  if max(L_ist) >= b:
    print("Error - Incorrect Integer/Base")
  else:
    print(ans)
s = str(input("Enter a string: "))
b = int(input("Enter a base: "))

if b > 36:
  print("Error - Base > 36")
elif '-' in s:
  print("Error - Negative String")
elif b < 0:
  print("Error - Negative Base")
else:
  to_decimal(s, b)