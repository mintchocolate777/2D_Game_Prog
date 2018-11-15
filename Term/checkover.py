import reverse
import game_state

def checkOver():
    for y in range(8):
        for x in range(8):
            reversible = reverse.checkReverse(x, y)
            if reversible & 1:
                j = y - 1
                while game_state.board[j][x] != game_state.nowTurn and game_state.board[j][x] != 'None' and game_state.board[j][x] != 'hurdle':
                    j -= 1
                if game_state.board[y][x]=='None':
                    return True
            reversible >>= 1

            if reversible & 1:
                j = y + 1
                while game_state.board[j][x] != game_state.nowTurn and game_state.board[j][x] != 'None' and game_state.board[j][x] != 'hurdle':
                    j += 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
                    i -= 1
                if game_state.board[y][x]=='None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
                    i += 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y - 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i -= 1
                    j -= 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y - 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i += 1
                    j -= 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y + 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i -= 1
                    j += 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y + 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i += 1
                    j += 1
                if game_state.board[y][x] == 'None':
                    return True
    if game_state.nowTurn == 'bean':
        game_state.nowTurn = 'chick'
    else:
        game_state.nowTurn ='bean'
    for y in range(8):
        for x in range(8):
            reversible = reverse.checkReverse(x, y)
            if reversible & 1:
                j = y - 1
                while game_state.board[j][x] != game_state.nowTurn and game_state.board[j][x] != 'None' and game_state.board[j][x] != 'hurdle':
                    j -= 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                j = y + 1
                while game_state.board[j][x] != game_state.nowTurn and game_state.board[j][x] != 'None' and game_state.board[j][x] != 'hurdle':
                    j += 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
                    i -= 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
                    i += 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y - 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i -= 1
                    j -= 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y - 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i += 1
                    j -= 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x - 1
                j = y + 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i -= 1
                    j += 1
                if game_state.board[y][x] == 'None':
                    return True
            reversible >>= 1

            if reversible & 1:
                i = x + 1
                j = y + 1
                while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
                    i += 1
                    j += 1
                if game_state.board[y][x] == 'None':
                    return True
    return False

def outcome():
    beancount=0
    chickcount=0
    for i in range(8):
        for j in range(8):
            if game_state.board[i][j]=='bean':
                beancount+=1
            elif game_state.board[i][j]=='chick':
                chickcount+=1
    if beancount>chickcount:
        return 'bean'
    else:
        return 'chick'