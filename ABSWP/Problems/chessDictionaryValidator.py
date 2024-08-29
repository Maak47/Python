chessBoard = {'1h': 'bking', '6c': 'wqueen', '7d': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e':'wking', '8d': 'bking',
}

def isValidChessBoard(board):
    #one white king and one black king
    if 'wking' not in board.values() or 'bking' not in board.values():
        print('You have more than one black or white king')
        return False
    
    #total number of pieces
    if len(board.values()) > 32:
        print('You have more than 32 pieces on board')
        return False

    #most 8 pawns both players
    piece_count = {}
    for piece in board.values():
        piece_count[piece] = piece_count.get(piece, 0) + 1

    #pieces of pawn
    if piece_count.get('wpawn', 0) > 8 or piece_count.get('bpawn', 0) > 8:
        print('You have more than 8 pieces of either black or white pawn')
        return False

    #position
    for position in board.keys():
        if int(position[0]) > 8 or position[1] not in 'abcdefgh':
            print('Pieces not on board, position is wrong')
            return False

    #pieces count        
    for piece, maxCount in [('wbishop', 2), ('bbishop', 2), ('wknight', 2), ('bknight', 2), ('wrook', 2), ('brook', 2), ('wqueen', 1), ('bqueen', 1)]:
        if piece_count.get(piece, 0) > maxCount:
            print(f'More pieces of {piece} than {maxCount}')
            return False

    return True

print(isValidChessBoard(chessBoard))

