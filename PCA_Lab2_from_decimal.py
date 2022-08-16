#hi
dict = {
  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 
  16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 
  22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 
  28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 
  34: 'Y', 35 :'Z'
}

def from_decimal(d, b):
  ans = ""
  while d // b != 0:
    if (d % b) < 10:
        ans += str(d % b)
        d = d//b
    else:
        var = dict[d % b]
        ans += var
        d = d//b
      
  if (d % b) < 10: #for last digit
      ans += str(d % b)
      d = d//b
  else:
    var = dict[d % b]
    ans += var
    d = d//b
  print(ans[::-1])
  
d = int(input("Enter an integer: "))
b = int(input("Enter a base: "))

if b > 36:
    print("Error - Base > 36")
elif d < 0:
    print("Error - Negative Integer")
elif b < 0:
    print("Error - Negative Base")
else:
    from_decimal(d, b)