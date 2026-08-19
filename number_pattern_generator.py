def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    numbers = []
    for number in range(1, n + 1):
        numbers.append(str(number))
    
    return ' '.join(numbers)

print(number_pattern(4))  
print(number_pattern(12))  
print(number_pattern(-4))  
print(number_pattern(5.43)) 
