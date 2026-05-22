class QLearning:
        def __init__(self):
            self._features=None

        def extractFeatures(self,board,color):
              #Visibility
              #KingCaptureable
              #material balance
              #pieceCapturability
              #moveavailability
              pass
        def canSeeEnemyKing (self,board,color,visibility):
            for r in range(board.rows):
                for c in range(board.cols):
                    sq=board.grid[r][c]

                    if sq.is_occupied and sq. sq.pieceOccupying.color != color and sq.pieceOccupying.symbol=="K":
                        return 1.0 if (r,c) in visibility else 0.0
                              
            return 0.0
        def visibilityLevel (self,visibleSquares):
             # level of visibility depends on the board and the number of squares that can currently be seen
             # do this to scale down the feature to match can see king otherwise its wonky
             
             return len(visibleSquares)/30
        def moveAvailability(self,board,color):
             moves=board.getLegalMoves(color)

            # this might break later if too many moves become available
             return min(len(moves) /30,1.0)
        def pieceCapturability(self,board,color):
            moves = board.getLegalMoves(color)
            capValue=0
            squaresVisited = set() # prevent double counting capturing of a piece

            for m in moves:
                  if m.wasCap:
                       squareToVisit= (m.newRow,m.newCol)
                       if squaresVisited not in squaresVisited:
                            boardSquare= board.grid[m.newRow][m.newCol]
                            if boardSquare.is_occupied:
                                 capValue+=squaresVisited.pieceOccupying.value
                                 squaresVisited.add(squareToVisit)
            return min((capValue/30),1.0)