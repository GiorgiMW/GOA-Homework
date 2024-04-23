def variance(numbers): 
    tot = sum(numbers) / len(numbers)
    return sum((i - tot) ** 2 for i in numbers) / len(numbers)