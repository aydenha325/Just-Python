def input_num(xoy):
    run = True
    while run:
        try:
            idx = int(input(f'{xoy} : '))
            if idx > 3:
                print('number is out of range')
                continue
        except:
            print('please input int number')
            continue
        else:
            run = False

    return idx-1


def check_idx(board, idx_y, idx_x):
    change = False
    if board[idx_y][idx_x] == ' ':
        change = True

    return change


def check_win(board, idx_y, idx_x, player):
    win_cnt = 0
    for minus in range(3):
        if board[idx_y - minus][idx_x] == player:
            win_cnt += 1
    if win_cnt == 3:
        end = True
        return end

    win_cnt = 0
    for minus in range(3):
        if board[idx_y][idx_x - minus] == player:
            win_cnt += 1
    if win_cnt == 3:
        end = True
        return end

    win_cnt = 0
    for idx in range(3):
        if board[idx][idx] == player:
            win_cnt += 1
    if win_cnt == 3:
        end = True
        return end

    win_cnt = 0
    for idx in range(3):
        if board[idx][-idx] == player:
            win_cnt += 1
    if win_cnt == 3:
        end = True
        return end


def tictactoe_main():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    run = True
    while run:
        for player in ['O', 'X']:
            change = False
            while not change:
                print(f'player \'{player}\' turn')
                idx_y = input_num('y')
                idx_x = input_num('x')

                change = check_idx(board, idx_y, idx_x)
                if not change:
                    print('this idx was overlapped')
                    continue

            board[idx_y][idx_x] = player
            end = check_win(board, idx_y, idx_x, player)

            for line in board:
                print(line)
            print()

            if end:
                print(f"{'-'*10}")
                print(f'Game Over\nplayer {player} win')
                print(f"{'-'*10}")
                run = False
                break


if __name__ == '__main__':
    tictactoe_main()
