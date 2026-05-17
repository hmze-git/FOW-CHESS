class Piece:
    def __init__(self,cRow,cCol,isWhite,symbol):
        self.isWhite=isWhite
        self.isBlack= not isWhite
        self._currRow=cRow
        self._currCol=cCol
        self._isCaptured=False
        self._Symbol=symbol

    #get the captured proprty
    @property
    def isCaptured(self):
        return self._isCaptured

    @isCaptured.setter
    def isCaptured(self,Captured):
        self._isCaptured=Captured


    def displaySymbol(self):
        return self._Symbol    

    