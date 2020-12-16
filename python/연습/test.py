def multiply(*var):
    result = 1
    for num in var:
        result = result * num
    return result


print(multiply(10, 20))