import math

def lcm2(arr, index, temp):
    if index == len(arr) - 1:
        return temp
    return lcm2(arr, index+1, lcm(temp, arr[index+1]))
    
def lcm(x,y):
	return (x*y)//math.gcd(x,y)
    
def solution(arr):
    return lcm2(arr, 0, arr[0])