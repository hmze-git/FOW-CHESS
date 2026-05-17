class Move:
   # no old x setter needed logic because we would never update it      
    def __init__(self,oldRow,oldCol,newRow,newCol,piece,capture):
        self._oldRow=oldRow
        self._oldCol=oldCol
        self._newRow=newRow
        self._newCol=newCol
        self._piece=piece
        self._wasCap=capture
        self._capturedPiece=None

    @property
    def oldRow(self):
        return self._oldRow
    
    @property
    def oldCol(self):
        return self._oldCol
    
    @property
    def wasCap(self):
        return self._wasCap

    @property
    def newRow(self):
        return self._newRow
    

    @property
    def newCol(self):
        return self._newCol
    @property
    def capturedPiece(self):
        return self._capturedPiece
    @capturedPiece.setter
    def capturedPiece(self,capPiece):
        self._capturedPiece=capPiece
    @property
    def piece(self):
        return self._piece
  


    def __repr__(self):
        return f"{self._piece.displaySymbol()} ({self.oldRow},{self.oldCol})->({self.newRow},{self.newCol}) {'CAP' if self._wasCap else 'NOCAP'}"
    
   