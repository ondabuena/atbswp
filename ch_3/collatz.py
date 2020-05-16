def collatz(number):
	if number % 2 ==0:
		print(number // 2)
		return number//2
	elif number % 2 ==1:
		print(3* number + 1)
		return 3*number+1	
	
try:
	ask=int(input("Give me a number "))
	while ask != 1:
		ask = collatz(ask)
except ValueError:
	print("Please enter an integer. ")			







