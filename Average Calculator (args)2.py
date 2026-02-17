def average_numbers(*args):
    if not args:
        return "No numbers provided"
    
    return sum(args)/ len(args)

print (average_numbers())
print (average_numbers(10,20,30))
