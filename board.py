from square import Square
from knight import Knight
from queen import Queen
from king import King
from pawn import Pawn
from rook import Rook
from bishop import Bishop
class Board:
        def __init__(self,rows:int =6,cols:int=5):
                self.rows=rows
                self.cols=cols
                self.grid =[
                       
                        [
                                Square(r,c) for c in range(5)
                        ]
                         for r in range(6)
                ] # reads backwards 
                self.setupBoard()

        def  setupBoard(self):
            for c in range(self.cols):
                    if c==0:
                     rook= Rook(0,c,False)
                     pawn= Pawn(1,c,False)


                    # WHITE PIECES
                     Wpawn= Pawn(4,c,True)
                     Wrook= Rook(5,c,True)
                     
                     self.grid[0][c].pieceOccupying=rook
                     self.grid[1][c].pieceOccupying=pawn
                     self.grid[4][c].pieceOccupying=Wpawn
                     self.grid[5][c].pieceOccupying=Wrook

                    
                    elif c==1:
                     BKnight= Knight(0,c,False)
                     Bpawn= Pawn(1,c,False)


                    # WHITE PIECES
                     Wpawn= Pawn(4,c,True)
                     WKnight= Knight(5,c,True)
                     
                     self.grid[0][c].pieceOccupying=BKnight
                     self.grid[1][c].pieceOccupying=Bpawn
                     self.grid[4][c].pieceOccupying=Wpawn
                     self.grid[5][c].pieceOccupying=WKnight
                    elif c==2:
                        Bbishop= Bishop(0,c,False)
                        Bpawn= Pawn(1,c,False)


                        # WHITE PIECES
                        Wpawn= Pawn(4,c,True)
                        Wbishop= Bishop(5,c,True)
                        
                        self.grid[0][c].pieceOccupying=Bbishop
                        self.grid[1][c].pieceOccupying=Bpawn
                        self.grid[4][c].pieceOccupying=Wpawn
                        self.grid[5][c].pieceOccupying=Wbishop
                    elif c==3:
                        Bqueen= Queen(0,c,False)
                        Bpawn= Pawn(1,c,False)


                        # WHITE PIECES
                        Wpawn= Pawn(4,c,True)
                        Wqueen= Queen(5,c,True)
                        
                        self.grid[0][c].pieceOccupying=Bqueen
                        self.grid[1][c].pieceOccupying=Bpawn
                        self.grid[4][c].pieceOccupying=Wpawn
                        self.grid[5][c].pieceOccupying=Wqueen
                    elif c==4:
                        BKing= King(0,c,False)
                        Bpawn= Pawn(1,c,False)


                        # WHITE PIECES
                        Wpawn= Pawn(4,c,True)
                        WKing= King(5,c,True)
                        
                        self.grid[0][c].pieceOccupying=BKing
                        self.grid[1][c].pieceOccupying=Bpawn
                        self.grid[4][c].pieceOccupying=Wpawn
                        self.grid[5][c].pieceOccupying=WKing
            
        def printBoard(self):
             for r in range(self.rows):
                
                for c in range(self.cols):

                        if not self.grid[r][c].is_occupied:
                             print("*",end=" ")
                        else:
                            print(self.grid[r][c].pieceOccupying.displaySymbol(),end=" ")
                print()
                       
