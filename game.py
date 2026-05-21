from board import Board
import random
class Game:
   
    def __init__(self):
        self._board = Board(6,5)
        self._whiteCaps=[]
        self._blackCaps=[]
        self._numMoves =0
        self._isWhitesTurn=True

    def viewMoves(self):
                
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



    def selfPlay(self):
        while self._numMoves<500:
            moves=self.getLegalMoves("White" if self._isWhitesTurn else "Black")
            self.board.printBoard("White" if self._isWhitesTurn else "Black")
            if not moves:
                print("Draw due to no more moves")
                return
           
            randMove= random.choice(moves)
            self.board.apply_move(randMove)
        
            print(f"{'White' if self._isWhitesTurn else 'Black'} played: {randMove}")

            result = self.board.checkWinner(randMove)
            if result:
                print(f"{result} is the winner")
                break

            self._isWhitesTurn = not self._isWhitesTurn
            self._numMoves += 1

        print("MOVE LIM")
    @property
    def board(self):
        return self._board