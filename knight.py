from piece import Piece
from move import Move
class Knight(Piece):
    def  __init__(self,cRow,cCol,color):
        super().__init__(cRow,cCol,color,"N")

  
    def viewLegalMoves(self,board):
        moves=[]
        directions = [(-2,-1),(-2,1),
                      (-1,-2),(1,-2),
                      (-1,2),(1,2),
                      (2,-1),(2,1)]
        
        for dr,dc in directions:
            computedRow = self._currRow + dr
            computedCol = self._currCol + dc

            isLegal,isCap=board.isValidLocation(computedRow,computedCol,self._color)

            if isLegal:
                m= Move(self._currRow,self._currCol,computedRow,computedCol,self,isCap)
                moves.append(m)

        return moves  
    def getAttackSquars(self,board):
        atqSQ=set()
        directions = [(-2,-1),(-2,1),
                      (-1,-2),(1,-2),
                      (-1,2),(1,2),
                      (2,-1),(2,1)]
        
        for dr,dc in directions:
            computedRow = self._currRow + dr
            computedCol = self._currCol + dc

            isLegal,isCap=board.isValidLocation(computedRow,computedCol,self._color)

            if isLegal:
                atqSQ.add((computedRow,computedCol))
        return atqSQ