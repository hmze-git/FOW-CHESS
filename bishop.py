from piece import Piece
class Bishop(Piece):
    def  __init__(self,cRow,cCol,color):
        super().__init__(cRow,cCol,color,"B",3)


    def viewLegalMoves(self,board):
        directions = [(-1,-1),(1,1),
                        (1,-1),(-1,1)]
                
        return self.slide(board,directions)
    
    def getAttackSquars(self,board):
        directions = [(-1,-1),(1,1),
                        (1,-1),(-1,1)]
        return self.slideAttack(board,directions)