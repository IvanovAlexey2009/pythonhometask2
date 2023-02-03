result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as value_error:
        print (value_error)
    except IndexError as index_error:
        print(index_error)
    except Exception as error:
        print(error)

print(result)
