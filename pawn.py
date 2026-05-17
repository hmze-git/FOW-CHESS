from piece import Piece
class Pawn(Piece):
    def  __init__(self,cRow,cCol,isWhite):
        super().__init__(cRow,cCol,isWhite,"P")


