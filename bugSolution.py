def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

result = my_function(10, 0)  # result will be 0 now
print(result)