from board import Board
class Game:
   
    def __init__(self):
        self._board = Board(6,5)
        self._whiteCaps=[]
        self._blackCaps=[]

    def viewMoves(self):
                
        self._board.printBoard()
        moves = []
        for r in range(self._board.rows):
            for c in range(self._board.cols):
                sq = self._board.grid[r][c]
                if sq.is_occupied and sq.pieceOccupying.color == "White":
                    moves.extend(sq.pieceOccupying.viewLegalMoves(self._board))

        print(f"Total white moves: {len(moves)}")
        for m in moves:
            print(m)
    def getLegalMoves(self,color):
        moves = []
        color = color

        for r in range(self._board.rows):
            for c in range (self._board.cols):
                sq = self._board.grid[r][c]
                if sq.is_occupied and sq.pieceOccupying.color == color:
                    moves.extend(sq.pieceOccupying.viewLegalMoves(self._board))
        return moves
    
    @property
    def board(self):
        return self._board