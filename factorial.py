#팩토리얼 계산기 - 임정훈
n = (int) (input("Input : "))
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)


print factorial(n) #min=0,max=996
