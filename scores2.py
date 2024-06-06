#!/usr/bin/env python3
score = input("Enter Score, 0.0 to 1.0: ==>")
fscore = float(score)
if fscore >= 0.9:
	print("Grade is: A")
elif fscore >= 0.8:
	print("Grade is: B")
elif fscore >= 0.7:
	print("Grade is: C")
elif fscore >= 0.6:
	print("Grade is: D")
elif fscore < 0.6:
	print("Grade is: F")
	
else:
    print("Score Grade: >= 0.9 A; >= 0.8 B; >= 0.7 C; >= 0.6 D; < 0.6 F")
	