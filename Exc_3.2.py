#!/usr/bin/env python3
sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
   fh = float(sh)
   fr = float(sr)
	#print(fh,fr)
except:
	print("Error, Enter numeric input")
	quit()
if fh > 40 :
	print("Overtime")
	reg = fr * fh
	otp = (fh - 40) * (fr * 0.5)
	print (reg,otp)
	xp = reg + otp
else:
	print("Regular")
	xp = fh * fr
print("Pay: ",xp)