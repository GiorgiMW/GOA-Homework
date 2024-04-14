#Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    
    total_sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
            
    return total_sum