from move import Move
class Piece:
    def __init__(self,cRow,cCol,color,symbol):
        self._color=color
        self._currRow=cRow
        self._currCol=cCol
        self._isCaptured=False
        self._Symbol=symbol

    #get the captured proprty
    @property
    def isCaptured(self):
        return self._isCaptured

    @property
    def color(self):
        return self._color
    
    @isCaptured.setter
    def isCaptured(self,Captured):
        self._isCaptured=Captured

    @property
    def symbol(self):
        return self._Symbol


    def displaySymbol(self):
        prefix= "w" if self._color=="White" else "b"
        return f"{prefix}{self._Symbol}"    
    
    def makeMove(self):
        pass

    def viewLegalMoves(self):
        pass
    def slide(self,board,directions):
        moves=[]
        for dr,dc in directions:
            computedRow = self._currRow + dr
            computedCol = self._currCol + dc

        while True:
            isLegal,isCap=board.isValidLocation(computedRow,computedCol,self._color)

            if not board.inBounds(computedRow,computedCol):
                break
   
            if isLegal:
                m = Move(self._currRow,self._currCol,computedRow,computedCol,self,isCap)
                moves.append(m)

            #stop sliding when you hit your own piece or enemy piece

            if isCap or not isLegal:
                break
            #Add every tuple until you see the limit for all of them
            computedRow+=dr
            computedCol+=dc


        return moves  


    