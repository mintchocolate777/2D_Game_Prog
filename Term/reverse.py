import game_state

damageCount = 0 # hp 감소량을 위한 변수임

def checkReverse(x, y):
    result=0
    #남쪽 체크
    if y>1 and game_state.board[y-1][x]!=game_state.nowTurn and game_state.board[y-1][x]!='hurdle' and game_state.board[y-1][x]!='None':
        for j in range(y-2,-1,-1):
            if game_state.board[j][x]==game_state.nowTurn:
                result+=1
                break
            if game_state.board[j][x]=='None' or game_state.board[j][x]=='hurdle':
                break
    #북쪽 체크
    if y<6 and game_state.board[y+1][x]!=game_state.nowTurn and game_state.board[y+1][x]!='hurdle' and game_state.board[y+1][x]!='None':
        for j in range(y+2,8,1):
            if game_state.board[j][x]==game_state.nowTurn:
                result+=2
                break
            if game_state.board[j][x] == 'None' or game_state.board[j][x] == 'hurdle':
                break
    #서쪽 체크
    if x>1 and game_state.board[y][x-1]!=game_state.nowTurn and game_state.board[y][x-1]!='hurdle'and game_state.board[y][x-1]!='None':
        for i in range(x-2,-1,-1):
            if game_state.board[y][i]==game_state.nowTurn:
                result+=4
                break
            if game_state.board[y][i]=='None' or game_state.board[y][i] =='hurdle':
                break
    #동쪽 체크
    if x<6 and game_state.board[y][x+1]!=game_state.nowTurn and game_state.board[y][x+1]!='hurdle'and game_state.board[y][x+1]!='None':
        for i in range(x+2, 8, 1):
            if game_state.board[y][i]==game_state.nowTurn:
                result+=8
                break
            if game_state.board[y][i]=='None' or game_state.board[y][i]=='hurdle':
                break
    #
    if x>1 and y>1 and game_state.board[y-1][x-1]!=game_state.nowTurn and game_state.board[y-1][x-1]!='hurdle'and game_state.board[y-1][x-1]!='None':
        i=x-2
        j=y-2
        while i>=0 and j>=0:
            if game_state.board[j][i]==game_state.nowTurn:
                result+=16
                break
            if game_state.board[j][i]=='None' or game_state.board[j][i]=='hurdle':
                break
            i-=1
            j-=1
    #
    if x<6 and y>1 and game_state.board[y-1][x+1]!=game_state.nowTurn and game_state.board[y-1][x+1]!='hurdle'and game_state.board[y-1][x+1]!='None':
        i=x+2
        j=y-2
        while i<8 and j>=0:
            if game_state.board[j][i]==game_state.nowTurn:
                result+=32
                break
            if game_state.board[j][i]=='None' or game_state.board[j][i]=='hurdle':
                break
            i+=1
            j-=1
    #
    if x>1 and y<6 and game_state.board[y+1][x-1]!=game_state.nowTurn and game_state.board[y+1][x-1]!='hurdle'and game_state.board[y+1][x-1]!='None':
        i=x-2
        j=y+2
        while i>=0 and j<8:
            if game_state.board[j][i]==game_state.nowTurn:
                result+=64
                break
            if game_state.board[j][i]=='None' or game_state.board[j][i]=='hurdle':
                break
            i-=1
            j+=1
    #
    if x<6 and y<6 and game_state.board[y+1][x+1]!=game_state.nowTurn and game_state.board[y+1][x+1]!='hurdle'and game_state.board[y+1][x+1]!='None':
        i=x+2
        j=y+2
        while i<8 and j<8:
            if game_state.board[j][i]==game_state.nowTurn:
                result+=128
                break
            if game_state.board[j][i]=='None' or game_state.board[j][i]=='hurdle':
                break
            i+=1
            j+=1
    return result

def reverse(x,y):
    global damageCount
    damageCount=0
    reversed =0
    reversible = checkReverse(x,y)
    if reversible==0:
        if game_state.nowTurn == 'bean':
            game_state.nowTurn = 'chick'
        else:
            game_state.nowTurn = 'bean'
        return 0
    game_state.board[y][x]=game_state.nowTurn
    if reversible&1:
        j=y-1
        while game_state.board[j][x]!=game_state.nowTurn and game_state.board[j][x]!='None' and game_state.board[j][x]!='hurdle':
            game_state.board[j][x]=game_state.nowTurn
            damageCount+=1
            reversed+=1
            j-=1
    reversible>>=1

    if reversible&1:
        j=y+1
        while game_state.board[j][x] != game_state.nowTurn and game_state.board[j][x] != 'None' and game_state.board[j][x] != 'hurdle':
            game_state.board[j][x]=game_state.nowTurn
            damageCount += 1
            reversed+=1
            j+=1
    reversible>>=1

    if reversible&1:
        i=x-1
        while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
            game_state.board[y][i]=game_state.nowTurn
            damageCount += 1
            reversed+=1
            i-=1
    reversible>>=1

    if reversible & 1:
        i = x + 1
        while game_state.board[y][i] != game_state.nowTurn and game_state.board[y][i] != 'None' and game_state.board[y][i] != 'hurdle':
            game_state.board[y][i] = game_state.nowTurn
            damageCount += 1
            reversed += 1
            i += 1
    reversible >>= 1

    if reversible&1:
        i=x-1
        j=y-1
        while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
            game_state.board[j][i] = game_state.nowTurn
            damageCount += 1
            reversed += 1
            i -= 1
            j-=1
    reversible>>=1

    if reversible&1:
        i=x+1
        j=y-1
        while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
            game_state.board[j][i] = game_state.nowTurn
            damageCount += 1
            reversed += 1
            i += 1
            j-=1
    reversible>>=1

    if reversible&1:
        i=x-1
        j=y+1
        while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
            game_state.board[j][i] = game_state.nowTurn
            damageCount += 1
            reversed += 1
            i -= 1
            j+=1
    reversible>>=1

    if reversible&1:
        i=x+1
        j=y+1
        while game_state.board[j][i] != game_state.nowTurn and game_state.board[j][i] != 'None' and game_state.board[j][i] != 'hurdle':
            game_state.board[j][i] = game_state.nowTurn
            damageCount += 1
            reversed += 1
            i += 1
            j+=1
    reversible>>=1

    if game_state.nowTurn=='bean':
        game_state.nowTurn='chick'
    else:
        game_state.nowTurn='bean'
    for i in range(0,8,1):
        for j in range(0,8,1):
            if checkReverse(i,j):
                return reversed
    return -1

def hpSystem():
    global damageCount
    hpMinus=damageCount*100
    hpBonusMinus=0
    for i in range (0,damageCount):
        hpBonusMinus+=i*10
    hpMinus+=hpBonusMinus
    if game_state.nowTurn=='bean':
        game_state.beanHp-=hpMinus
    else:
        game_state.chickHp-=hpMinus
