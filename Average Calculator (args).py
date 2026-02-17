def average_numbers(*args):
    if len (args) ==0 :
       return ("No numbers Provided")

    total = 0

    for num in args:
        total += num
    return total/len(args)

print(average_numbers(10, 20, 30))
print(average_numbers())