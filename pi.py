import time as tm
import random as rd


def LeibnizSeries(roundtime):
    res = 0
    cnt = 0

    for n in range(1, roundtime, 2):
        cnt += 1
        if cnt % 2 == 0:
            res -= 1 / n
        else:
            res += 1 / n

    return res * 4


def MontecarloMethod(randtime):
    cin = 0

    for cnt in range(randtime):
        x = rd.uniform(0, 1)
        y = rd.uniform(0, 1)

        if (x ** 2 + y ** 2) <= 1:
            cin += 1

    res = cin * 4 / randtime
    return res


def choice(choose, cnt):
    if choose == 0:
        return LeibnizSeries(cnt)
    elif choose == 1:
        return MontecarloMethod(cnt)


def run():
    method = ['[0] Leibniz Series', '[1] Montecarlo Method']
    choose = 1
    print(method[choose][4:], 'selected.')

    cnt = int(input('input round time : '))
    print('\ncalculating...', end='')

    start = tm.time()
    pi = choice(choose, cnt)
    runtime = str(tm.time() - start)[0:10]

    print('\n')
    print('pi :', pi)
    print('runtime :', runtime, 'seconds')


if __name__ == '__main__':
    run()
