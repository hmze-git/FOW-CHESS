from piece import Piece
class Rook(Piece):
    def  __init__(self,cRow,cCol,color):
        super().__init__(cRow,cCol,color,"R")

    def viewLegalMoves(self,board):
           directions = [(-1,0),(1,0),
                        (0,-1),(0,1)]
           
           return self.slide(board,directions)
    
    def getAttackSquars(self,board):
        directions = [(-1,0),(1,0),
                        (0,-1),(0,1)]
        return self.slideAttack(board,directions)