
def sum_strings(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    total_len = 0

    if n1 > n2:
        diff = n1 - n2
        str2 = '0'*diff + str2
        total_len = n1

    elif n1 < n2:
        diff = n2-n1
        str1 = '0'*diff + str1
        total_len = n2
    
    else:
        total_len = n1

    added = ''
    done = False
    iterations = 0
    while not done:
        carry = 0
        for place in range(total_len-1, -1, -1):
            iterations += 1
            a = int(str1[place])
            b = int(str2[place])
            place_sum = a + b + carry
            if place_sum >= 10:
                carry = 1
                place_sum = place_sum - 10
            else:
                carry = 0
            added = str(place_sum) + added
        if iterations == total_len:
            if carry == 1:
                added = str(carry) + added
            done = True
    return added

print(sum_strings('111', '9999'))


def multiply_strings(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    small_len = 0
    if n1 > n2:
        small_len = n2
        small_str = str2
        big_len = n1
        big_str = str1
    elif n2 > n1:
        small_len = n1
        small_str = str1
        big_len = n2
        big_str = str2
    else:
        small_len = n1
        small_str = str1
        big_len = n2
        big_str = str2

    done = False
    iterations = 0
    max_iter = big_len * small_len
    list_of_multiplied = []

    while not done:
        carry = 0

        for place in range(small_len-1, -1, -1):
            to_multiply = int(small_str[place])
            multiplied = '' + '0'*(small_len-place-1)

            for num in range(big_len-1, -1, -1):
                big_multiply = int(big_str[num])
                iterations += 1
                place_multiplication = (to_multiply * big_multiply) + carry
                carry = place_multiplication // 10
                place_multiplication = place_multiplication % 10
                multiplied = str(place_multiplication) + multiplied
                
            if carry > 0:
                multiplied = str(carry) + multiplied
            list_of_multiplied.append(multiplied)
        if iterations == max_iter:
            done = True
    
    print(list_of_multiplied)
    total_sum = ''
    for i in range(len(list_of_multiplied)):
        total_sum = sum_strings(list_of_multiplied[i], total_sum)

    return total_sum

print(multiply_strings('1124', '1124'))

    

