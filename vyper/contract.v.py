# Setting up the private variables (only callable from within the contract)
# See more at https://vyper.readthedocs.io/en/latest/index.html

Game: {
    name: string
    board: address[9] 
    player: address[2] 
    blocked_until: uint 
    movs: uint 
    turn: uint 
    amount: uint 
    waiting: bool 
    finish: bool 
}

@public
Game room

@public
def TicTacToe():
    room.finish = True
    
modifier waiting():
@require(room.waiting == True)

modifier notWaiting():
@require(room.waiting == False)
    
modifier otherPlayer():
@require(room.player[0] != msg.sender)
    
modifier checkBid():
@require(room.amount <= msg.value)
    
modifier myTurn():
@require(room.player[room.turn] == msg.sender)
    
modifier playable(c):
@require(room.board[c] == 0)
    
modifier notOpen():
@require(room.finish == True)
    
modifier open():
@require(room.finish == False)
    
modifier canReclaim():
@require(room.blocked_until >= block.number)

event TurnChange(_t)
event PlayerJoin(_t)
event NewGame(_name, _amount)
event EndGame(_winner, _amount)

@internal
def nextTurn():
    if (room.turn == 0):
        room.turn = 1
    else:
        room.turn = 0
    TurnChange(room.player[room.turn])


@constant
@public
def getPlayers():
    return room.player


@constant
@public
def roomFree():
    return room.finish


@constant
@public
def getRoomName():
    return room.name


@constant
@internal
def checkBoard(c):
    address[9] = room.board
    if c == 0:
        if ((board[0] == board[4]  && board[0] == board[8]) || (board[0] == board[1]  && board[0] == board[2]) || (board[0] == board[3] && board[0] == board[6])):
            return True
        else:
            return False
    else if c== 1:
        if ((board[1] == board[0] && board[1] == board[2])|| (board[1] == board[4] && board[1] == board[7])):
            return True
        else:
            return False
    else if (c == 2):
        if ((board[2] == board[0] && board[2] == board[1])|| (board[2] == board[4] && board[2] == board[6])|| (board[2] == board[5] && board[2] == board[8])):
            return True
        else:
            return False
    else if (c == 3):
        if ((board[3] == board[0] && board[3] == board[6])|| (board[3] == board[4] && board[3] == board[5])):
            return True
        else:
            return False
    else if (c == 4):
        if ((board[3] == board[4] && board[4] == board[5])|| (board[2] == board[4] && board[4] == board[6])|| (board[1] == board[4] && board[4] == board[7])|| (board[0] == board[4] && board[4] == board[8])):
            return True
        else:
            return False
    else if (c == 5):
        if ((board[3] == board[5] && board[4] == board[5])|| (board[2] == board[5] && board[8] == board[5])):
            return True
        else:
            return False
    else if (c == 6):
        if ((board[6] == board[0] && board[6] == board[3]) || (board[6] == board[7] && board[6] == board[8]) || (board[6] == board[4] && board[6] == board[2])):
            return True
        else:
            return False
    else if (c == 7):
        if ((board[7] == board[6] && board[7] == board[8]) || (board[7] == board[4] && board[7] == board[1])):
            return True
        else:
            return False
    else if (c == 8):
        if ((board[8] == board[6] && board[8] == board[7]) ||  (board[8] == board[2] && board[8] == board[5]) || (board[8] == board[0] && board[8] == board[4])):
            return True
        else:
            return False


@constant
@public
def getBid():
    return room.amount

@constant
@public
def getBoard():
    if room.waiting == True || room.finish == True:
        return board
    return room.board


@constant
@public
def getTurn():
    if room.waiting == True || room.finish == True:
        return address(0)
    return room.player[room.turn]

@public
@playable
def newGame(room_name):
    room.board = [address(0),address(0),address(0),address(0),address(0),address(0),address(0),address(0),address(0)]
    room.name = room_name
    room.player[0] = msg.sender
    room.turn = 0
    room.amount = msg.value
    room.waiting = True
    room.finish = False
    room.blocked_until = block.number + 100
    room.movs = 9
    NewGame(room.name,msg.value)

@constant
@public
def isWaiting():
    return room.waiting


@public
@payable
def joinGame():
    if msg.value > room.amount:
        msg.sender.transfer(msg.value-room.amount)
    
    room.amount = this.balance
    room.player[1] = msg.sender
    room.waiting = False
    room.blocked_until = block.number + 100
    PlayerJoin(msg.sender)


@public
def reclaim():
    if room.waiting:
        if msg.sender == room.player[0]:
            room.player[0] = address(0)
            room.waiting = False
            room.finish = True
            msg.sender.transfer(room.amount)
        
    else:
        if room.turn == 0:
            if room.player[1] == msg.sender:
                room.finish = True
                room.player[1].transfer(room.amount)
        else:
            if room.player[0] == msg.sender:
                room.finish = True
                room.player[0].transfer(room.amount)


@public
def play(c):
    room.board[c] = msg.sender
    room.movs = room.movs -1
    room.blocked_until = block.number + 100

    if (checkBoard(c)):
        room.finish = True
        msg.sender.transfer(room.amount)
        EndGame(msg.sender,room.amount)
    else:
        if (room.movs == 0):
            room.finish = True
            room.player[0].transfer(room.amount/2)
            room.player[1].transfer(room.amount/2)
            EndGame(address(0),0)
        else:
            room.blocked_until = block.number + 100
            nextTurn()
