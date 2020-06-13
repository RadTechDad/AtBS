# chessDictionaryValidator.py
# AtBS - Chapter 5
# Code by Darrell Dudics

MAX_PIECES = 16

validChessPieces = {
    'pawn':8,
    'knight':10,
    'bishop':10,
    'rook':10,
    'queen':9,
    'king':1
}

validTiles = ['12345678', 'abcdefgh']
validColors = 'bw'

def isValidChessBoard(board):
    allPieceCounter = 0
    pieceCounter = {}
    chessBoardIsValid = True
    
    for tile, piece in board.items():
        if tile[0] not in validTiles[0] or tile[1] not in validTiles[1]:
            print('\'' + tile + '\' is an invalid tile.')
            chessBoardIsValid = False
        if piece[0] not in validColors:
            print('\'' + piece[0] + '\' in \'' + piece + '\' is referencing an invalid color.')
            chessBoardIsValid = False
        if piece[1:] not in validChessPieces.keys():
            print(piece[1:] + ' is an invalid chess piece.')
            chessBoardIsValid = False
        allPieceCounter += 1
        pieceCounter.setdefault(piece, 0)
        pieceCounter[piece] += 1
    
#    print(pieceCounter)
    for k, v in pieceCounter.items():
        #print(str(v) + ' -> ' + str(validChessPieces[k[1:]]))
        if v > validChessPieces[k[1:]]:
            color = ''
            if k[0] == 'b':
                color = 'black'
            else:
                color == 'white'

            print('Too many ' + color + ' ' + k[1:] + 's')
    
    if allPieceCounter < 0:
        print('Not enough chess pieces on the board.')
        chessBoardIsValid = False
    elif allPieceCounter > MAX_PIECES:
        print('Too many chess pieces on the board.')
        chessBoardIsValid = False
        
    return chessBoardIsValid

board = {
    '1h':'bking',
    '6c':'wqueen',
    '2g':'bbishop',
    '5h':'bqueen',
    '3e':'wking'
}

if isValidChessBoard(board):
    print("Chessboard is valid")
else:
    print("Chessboard is invalid")
