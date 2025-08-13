# 1. Main
def test(n):
    '''
    Допустим мы изменили документицию и хотим закинуть ее в dev
    dev dev
    dev edv
    :param n: количество чисел
    :return: квадрат чисел
    '''

    # выше описывается Docs, а ниже function
    return [i**2 for i in range(n)]