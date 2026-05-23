from piece import Piece
from move import Move
class King(Piece):
    def  __init__(self,cRow,cCol,color):
        super().__init__(cRow,cCol,color,"K",0)


    def viewLegalMoves(self,board):
        moves=[]
        directions = [(-1,-1),(-1,0),(-1,1),
                      (-1,0),(0,1),
                      (1,-1),(1,0),(1,1)]
        
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
        directions = [(-1,-1),(-1,0),(-1,1),
                      (0,-1),(0,1),
                      (1,-1),(1,0),(1,1)]
        
        for dr,dc in directions:
            computedRow = self._currRow + dr
            computedCol = self._currCol + dc

            #Might need to change to isInbounds instead fine for now 
            # if the fow mask acts weird for king problem is here
            isInBounds=board.inBounds(computedRow,computedCol)

            if isInBounds:
                atqSQ.add((computedRow,computedCol))
        return atqSQ
    

    def numPiecesSurrounding(self,board):
                    directions = [(-1,-1),(-1,0),(-1,1),
                      (0,-1),(0,1),
                      (1,-1),(1,0),(1,1)]
                    counter=0
        
                    for dr,dc in directions:
                        computedRow = self._currRow + dr
                        computedCol = self._currCol + dc

                        isFriend=board.isSurroundedByFriend(computedRow,computedCol,self._color)

                        if isFriend:
                             counter+=1
                        else:
                             continue
                    
                    return counter