from piece import Piece
from move import Move
class Pawn(Piece):
    def  __init__(self,cRow,cCol,color):
        super().__init__(cRow,cCol,color,"P")


    
    def viewLegalMoves(self,board):
        moves=[]

        forward = self._currRow+ 1 if self.color=="black" else -1

        if board.inBounds(forward,self._currCol):
            m= Move(self._currRow,self._currCol,forward,self._currCol,self,False)
            moves.append(m)

        #capture moves
        for dc in [-1,1]:
            capRow= forward
            capCol=self._currCol+dc
            if board.inBounds(capRow,capCol):
                sq= board.grid[capRow][capCol]
                if sq.is_occupied and sq.pieceOccupying.color != self.color:
                        m = Move(self._currRow,self._currCol,capRow,capCol,self,True)
        return moves
        