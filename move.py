class Move:
   # no old x setter needed logic because we would never update it      
    def __init__(self,oldRow,oldCol,newRow,newCol,piece,capture):
        self._oldRow=oldRow
        self._oldCol=oldCol
        self._newRow=newRow
        self._newCol=newCol
        self._piece=piece
        self._wasCap=capture

    @property
    def oldRow(self):
        return self._oldRow
    
    @property
    def oldCol(self):
        return self._oldCol
    

    @property
    def newRow(self):
        return self._newRow
    

    @property
    def newCol(self):
        return self._newCol
    
    @property
    def newCol(self):
        return self._piece
    



    
   