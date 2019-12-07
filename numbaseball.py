import time as t
import random as r


def randnum():
    numlis = []
    cnt = 0

    while cnt <= 2:
        num = r.randint(0, 9)
        if num not in numlis:
            numlis.append(num)
            cnt += 1

    return numlis


def isnum(num):
    try:
        if ' ' in num:
            return '띄어쓰기 없이 입력합니다', 0
        if num == 'exit':
            return '이렇게 포기하다니', 1
        if int(num) != abs(int(num)):
            return '음수를 입력하지 마세요', 0
        if len(num) != 3:
            return '3개숫자를 입력하세요', 0
        for check in num:
            if num.count(check) > 1:
                return '숫자는 중복되지 않습니다', 0
    except ValueError:
        return '자연수를 입력하세요', 0
    else:
        return int(num), 2


def iscorrect(solution, num):
    if num == solution:
        return 0, 0, 1

    ball = 0
    strike = 0

    for a in range(3):
        if num[a] in solution:
            if num[a] == solution[a]:
                strike += 1
            else:
                ball += 1

    return strike, ball, 0


def timecheck(start_time):
    end_time = int(t.time() - start_time)
    minute = end_time // 60
    second = end_time % 60

    return minute, second


def main():
    solution = randnum()
    start_time = t.time()

    print('-'*50)
    print('숫자야구게임을 시작합니다!')
    print('0부터 9까지의 자연수 3개를 맞히는 게임입니다')
    print()
    print(f'게임을 그만두시려면 exit를 입력해주세요')
    print('-'*50)

    cnt = 0
    run = True
    while run:
        while run:
            print()
            num = input('숫자 3개를 입력해주세요\n입력 : ')
            check = isnum(num)

            if check[1] == 0:
                print(check[0])
                continue

            elif check[1] == 1:
                repeat = True
                while repeat:
                    print()
                    print('정말로 포기하시겠어요?')
                    select = input('[y] / [n] : ')

                    if select == 'y':
                        repeat = False
                        run = False
                    elif select == 'n':
                        repeat = False
                    else:
                        print('Yes / No 를 선택해주세요')
                        continue

            else:
                break

        if run == False:
            end_time = timecheck(start_time)

            print()
            print('-' * 50)

            if cnt:
                print(f'{end_time[0]}분 {end_time[1]}초 동안 {cnt}번 시도해놓고')
                print(check[0])

            else:
                print(f'{end_time[0]}분 {end_time[1]}초 동안 한번도 시도하지 않고')
                print(check[0])

            print('-' * 50)
            break

        cnt += 1

        numlis = []
        for appndnum in num:
            numlis.append(int(appndnum))

        result = iscorrect(solution, numlis)
        if result[2] == 1:
            end_time = timecheck(start_time)
            print('3스트라이크, 삼진 아웃!')
            print()
            print('-' * 50)
            print('축하합니다!!')
            print(f'{end_time[0]}분 {end_time[1]}초 걸려서 {cnt}번 만에 맞히셨네요!')
            print('-' * 50)
            run = False
        else:
            print(f'{result[0]}스트라이크 {result[1]}볼')


if __name__ == '__main__':
    main()
