def spam(number):
    return 'bulochka'*number


def my_sum(list_of_numbers):
    sum = 0
    for item in list_of_numbers:
        sum += item
    return sum

def shortener(string):
    arr = string.split(' ')
    strarr = []
    for item in arr:
        if len(item) > 6:
            strarr.append(item[:6] + '*')
        else:
            strarr.append(item)
    res = ' '.join(strarr)
    return res


def compare_ends(words):
    counter = 0
    for item in words:
        if len(item)>=2:
            if item[0] == item[len(item)-1]:
                counter += 1
    return counter

