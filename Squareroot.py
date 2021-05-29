import time
import math
try:
  print(math.sqrt(float(input("Please enter number here: "))))
except:
  print("Please enter a number instead of a letter")
finally:
  time.sleep(1.5)
  print("Thank you for using the square root calculator")

