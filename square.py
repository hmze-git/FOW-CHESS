
class Square:
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self._pieceOccupying= None


    @property
    def is_occupied(self):
        return self.pieceOccupying is not None
    

    @property
    def pieceOccupying(self):
        return self._pieceOccupying
    
    @pieceOccupying.setter
    def pieceOccupying(self,piece):
        self._pieceOccupying=piece
