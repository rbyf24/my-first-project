def check_list(target):
    numbers = [1, 10, 40, 23, 19, 42, 12, 18, 17, 21, 8, 2]
    seen = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    if check_list == 1000
    return None

print