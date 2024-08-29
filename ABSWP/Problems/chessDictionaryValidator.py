chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e':'wking', '8d': 'bking',
}

def isValidChessBoard(board):

    for position in board.keys():
        if int(position[0]) > 8 or position[1] not in 'abcdefgh':
            print('Board is INVALID, the piece can\'t be on a position thats 9 and greater or not in a-h')
            return False
    
    if 'bking' not in board.values() or 'wking' not in board.values():
        print('Board is INVALID because the kings are not present')
        return False
    
    if len(board.values()) > 16:
        print('Board is INVALID, there are more pieces than 16')
        return False
    
    if list(board.values()).count('wpawn') > 8 or list(board.values()).count('bpawn') > 8:
        print('Board is INVALID, because of more pieces of pawn than 8')
        return False

    for piece in ['wbishop', 'bbishop', 'wknight', 'bknight', 'wrook', 'brook']:
        if list(board.values()).count(piece) > 2:
            print('Board is INVALID, because of more pieces of bishop, knight or rook than 2 each player')
            return False
        
    for piece in ['wqueen', 'bqueen']:
        if list(board.values()).count(piece) > 1:
            print('Board is INVALID, because of more pieces of wqueen or bqueen than 1')
            return False
    
    return True

print(isValidChessBoard(chessBoard))