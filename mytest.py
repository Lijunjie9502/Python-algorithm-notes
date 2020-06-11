def add_two_big_positive_number(number1:str, number2:str) -> str:
    """
    实现两个正数字符串的加法
    """
    number1_length = len(number1)
    number2_length = len(number2)
    max_length = max(number1_length, number2_length)

    number1_list = [0] * max_length
    number2_list = [0] * max_length
    result = [0] * (max_length + 1)

    for i in range(number1_length):
        number1_list[i] = ord(number1[number1_length - i - 1]) - ord('0')
    for i in range(number2_length):
        number2_list[i] = ord(number2[number2_length - i - 1]) - ord('0')
    
    n_takeover = 0
    for i in range(max_length):
        result[i] = number1_list[i] + number2_list[i] + n_takeover
        if result[i] >= 10:
            result[i] -= 10
            n_takeover = 1
        else:
            n_takeover = 0
        
    result[max_length] = n_takeover
    return convert_list_to_str(result)


def sub_two_big_number(bignumer:str, smallnumber:str) -> str:
    """
    大数减小数
    
    :argument
    
    bignumber: 大数
    smallnumber: 小数
    """
    bignumer_list = [0] * (len(bignumer))
    smallnumber_list = [0] * (len(bignumer))
    result = [0] * (len(bignumer))

    for i in range(len(bignumer)):
        bignumer_list[i] = ord(bignumer[len(bignumer) - 1 - i]) - ord('0')
    for i in range(len(smallnumber)):
        smallnumber_list[i] = ord(smallnumber[len(smallnumber) - 1 - i]) - ord('0')
    
    n_takeover = 0
    for i in range(len(bignumer)):
        result[i] = bignumer_list[i] - smallnumber_list[i] + n_takeover
        if result[i] < 0:
            result[i] += 10
            n_takeover = - 1
    
    return convert_list_to_str(result)


def add_two_big_number(number1:str, number2:str) -> str:
    """
    实现两个大数的加法
    """
    if number1[0] != '-' and number2[0] != '-':
        return add_two_big_positive_number(number1, number2)
    elif number1[0] == '-' and number2[0] == '-':
        return '-' + add_two_big_positive_number(number1[1:], number2[1:])
    else:
        if number1[0] == '-':
            number1, number2 = number2, number1
        flag = compare_two_number(number1, number2[1:]) 
        if flag == 1:
            return add_two_big_positive_number(number1, number2[1:])
        elif flag == -1:
            return  '-' + add_two_big_positive_number(number1, number2[1:])
        elif flag == 0:
            return '0'
        


def compare_two_number(number1: str, number2: str) -> int:
    """
    比较两个字符串数字的大小
    
    if number1 > number2  return 1
    if number1 < number2  return -1
    if number1 == number2 return 0
    """
    if len(number1) > len(number2):
        return 1
    elif len(number1) < len(number2):
        return -1
    else:
        for i in range(len(number1)):
            if number1[i] > number2[i]:
                return  1
            elif number1[i] < number2[i]:
                return -1
    
    return 0 




def convert_list_to_str(number: list) -> str:
    """
    将列表转换为字符串
    """
    is_beginning0 = True
    n_length = len(number)
    res = ''
    for i in range(n_length-1, -1, -1):  # 去掉列表尾部的 0
        if is_beginning0 and number[i] != 0:
            is_beginning0 = False

        if not is_beginning0:
            res += chr(number[i] + ord('0'))
    if is_beginning0:
        res = '0'
    return res


if __name__ == "__main__":
    a_list = ['-12345678', '98', '0', '456', '-12345']
    b_list = ['123456', '-22', '0', '-456', '-12321']
    for a, b in zip(a_list, b_list):
        print('{} + {} = {}'.format(a, b, add_two_big_number(a, b)))
