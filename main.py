x = [-5, -2, 2, 5]
length = len(x)


def action(x):
    global length
    result_list = []
    for i in range(length):
        current_element = x[i]
        if current_element == 0:
            continue
        example = (current_element + (current_element ** 3) -3)/(2 * (current_element ** 2)) - (4 * current_element) + 2 + (6 * (current_element ** 5))
        print(example)
        result_list.append(example)
    return result_list

result = action(x)
result.sort()
print(result)