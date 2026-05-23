from square import Square
from knight import Knight
from queen import Queen
from king import King
from pawn import Pawn
from rook import Rook
from bishop import Bishop
import copy
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
                     rook= Rook(0,c,"Black")
                     pawn= Pawn(1,c,"Black")


                    # WHITE PIECES
                     Wpawn= Pawn(4,c,"White")
                     Wrook= Rook(5,c,"White")
                     
                     self.grid[0][c].pieceOccupying=rook
                     self.grid[1][c].pieceOccupying=pawn
                     self.grid[4][c].pieceOccupying=Wpawn
                     self.grid[5][c].pieceOccupying=Wrook

                    
                    elif c==1:
                     BKnight= Knight(0,c,"Black")
                     Bpawn= Pawn(1,c,"Black")


                    # WHITE PIECES
                     Wpawn= Pawn(4,c,"White")
                     WKnight= Knight(5,c,"White")
                     
                     self.grid[0][c].pieceOccupying=BKnight
                     self.grid[1][c].pieceOccupying=Bpawn
                     self.grid[4][c].pieceOccupying=Wpawn
                     self.grid[5][c].pieceOccupying=WKnight
                    elif c==2:
                        Bbishop= Bishop(0,c,"Black")
                        Bpawn= Pawn(1,c,"Black")


                        # WHITE PIECES
                        Wpawn= Pawn(4,c,"White")
                        Wbishop= Bishop(5,c,"White")
                        
                        self.grid[0][c].pieceOccupying=Bbishop
                        self.grid[1][c].pieceOccupying=Bpawn
                        self.grid[4][c].pieceOccupying=Wpawn
                        self.grid[5][c].pieceOccupying=Wbishop
                    elif c==3:
                        Bqueen= Queen(0,c,"Black")
                        Bpawn= Pawn(1,c,"Black")


                        # WHITE PIECES
                        Wpawn= Pawn(4,c,"White")
                        Wqueen= Queen(5,c,"White")
                        
                        self.grid[0][c].pieceOccupying=Bqueen
                        self.grid[1][c].pieceOccupying=Bpawn
                        self.grid[4][c].pieceOccupying=Wpawn
                        self.grid[5][c].pieceOccupying=Wqueen
                    elif c==4:
                        BKing= King(0,c,"Black")
                        Bpawn= Pawn(1,c,"Black")


                        # WHITE PIECES
                        Wpawn= Pawn(4,c,"White")
                        WKing= King(5,c,"White")
                        
                        self.grid[0][c].pieceOccupying=BKing
                        self.grid[1][c].pieceOccupying=Bpawn
                        self.grid[4][c].pieceOccupying=Wpawn
                        self.grid[5][c].pieceOccupying=WKing

        def getVisibleSquares(self,color):
                atqSq=set()
                for r in range(self.rows):
                        for c in range (self.cols):
                                sq = self.grid[r][c]
                                if sq.is_occupied and sq.pieceOccupying.color == color:
                                        atqSq.add((r,c))
                                        atqSq.update(sq.pieceOccupying.getAttackSquars(self))

                                   
                
                return atqSq
                       
        def getLegalMoves(self,color):
                moves = []
                color = color

                for r in range(self.rows):
                        for c in range (self.cols):
                                sq = self.grid[r][c]
                                if sq.is_occupied and sq.pieceOccupying.color == color:
                                        moves.extend(sq.pieceOccupying.viewLegalMoves(self))
                return moves               

        def isValidLocation(self,computedRow,computedCol,color):
     
                if computedRow>=0 and computedRow<self.rows:
                        if computedCol>=0 and computedCol<self.cols:
                                if self.grid[computedRow][computedCol].is_occupied and self.grid[computedRow][computedCol].pieceOccupying.color==color:
                                        return False,False
                                elif self.grid[computedRow][computedCol].is_occupied and self.grid[computedRow][computedCol].pieceOccupying.color!=color:
                                        return True,True
                                elif not self.grid[computedRow][computedCol].is_occupied:
                                      return True,False
                        else:
                              return False,False
                else:
                       return False,False

        #Is the piece surrounded by a a friendly piece at the specified row and col
        def isSurroundedByFriend(self,computedRow,computedCol,color):
     
                if computedRow>=0 and computedRow<self.rows:
                        if computedCol>=0 and computedCol<self.cols:
                                if self.grid[computedRow][computedCol].is_occupied and self.grid[computedRow][computedCol].pieceOccupying.color==color:
                                        return True
                                else:
                                       return False
                        else:
                               return False       
                else:
                       return False
        def inBounds (self,computedRow,computedCol) :
                if computedRow>=0 and computedRow<self.rows:
                        if computedCol>=0 and computedCol<self.cols:
                               return True
                        else:
                               return False
                else: return False


        def apply_move(self,move):
                targetSq= self.grid[move.newRow][move.newCol]
                piece=self.grid[move.oldRow][move.oldCol].pieceOccupying
                if targetSq.is_occupied:
                        move.capturedPiece= targetSq.pieceOccupying

                #check setter if this fails
                self.grid[move.newRow][move.newCol].pieceOccupying = piece
                self.grid[move.oldRow][move.oldCol].pieceOccupying=None
                piece._currRow = move.newRow
                piece._currCol = move.newCol


        def checkWinner(self,move):
                if move.wasCap:
                        pieceCapped = move.capturedPiece

                        if pieceCapped.symbol =="K":
                                return move.piece.color
                        else:
                                return None


        def copyBoard(self):
                newBoard= Board.__new__(Board)
                newBoard.rows=self.rows
                newBoard.cols=self.cols
                newBoard.grid=[]
                       
       
                for r in range(self.rows):
                                row=[]
                                for c in range (self.cols):
                                        originalSQ=copy.deepcopy(self.grid[r][c])
                                        if originalSQ.is_occupied:
                                                originalSQ.pieceOccupying._currRow=r
                                                originalSQ.pieceOccupying._currCol=c
                                        row.append(originalSQ)
                                newBoard.grid.append(row)
                return newBoard


        def printBoard(self,color):
                        visibleSq=self.getVisibleSquares(color)
                        print()
                        print(f"{color}s turn")
                        print("     a    b    c    d    e")
                        print("   +----+----+----+----+----+")
                        for r in range(self.rows):
                                print(f" {r} |", end="")
                                for c in range(self.cols):
                                        square = self.grid[r][c]
                                        if square.is_occupied and square._pieceOccupying.color==color:
                                                       
                                                print(f" {square.pieceOccupying.displaySymbol()} |", end="")
                                        elif (r,c) in visibleSq:
                                                if square.is_occupied and square._pieceOccupying.color!=color:
                                                        print(f" {square.pieceOccupying.displaySymbol()} |", end="")
                                                if not square.is_occupied :
                                                        print(f" #  |", end="")
                                        else:
                                                print(f" ?? |", end="")
                                       
                                print()
                                print("   +----+----+----+----+----+")
                        print()