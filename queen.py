from piece import Piece
class Queen(Piece):
    def  __init__(self,cRow,cCol,color):
        super().__init__(cRow,cCol,color,"Q")

    def viewLegalMoves(self,board):
           directions = [(-1,0),(1,0),
                        (0,-1),(0,1),(-1,-1),(1,1),
                            (1,-1),(-1,1)]
            
           
           return self.slide(board,directions)
        