from piece import Piece
from move import Move
class Pawn(Piece):
    def  __init__(self,cRow,cCol,color):
        super().__init__(cRow,cCol,color,"P",1)


    
    def viewLegalMoves(self,board):
        moves=[]

        dir=1 if self.color=="Black" else -1
        forward = self._currRow+ dir

        if board.inBounds(forward,self._currCol):
            if not board.grid[forward][self._currCol].is_occupied:
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
                        moves.append(m)
        return moves
        
    def getAttackSquars(self,board):
        attackSQ=set()
        dir=1 if self._color=="Black" else -1


        forward = self._currRow+ dir
            #capture moves
        for dc in [-1,1]:
            capRow= forward
            capCol=self._currCol+dc
            print("CAP COL",capCol)
            if board.inBounds(capRow,capCol):
                    attackSQ.add((capRow,capCol)) 
        return attackSQ