import random
class QLearningAgent:
        def __init__(self):
            self._weights=[random.uniform(-1,1) for _ in range(5)]
            self._epsilon=0.2
            self._learningRate=0.1


        def extractFeatures(self,board,color,visibleSquares):
              #Visibility
              #KingCaptureable
              #material balance
              #pieceCapturability
              #moveavailability
            featuresArray=[
                     self.canSeeEnemyKing(board,color,visibleSquares),
                     self.visibilityLevel(visibleSquares),
                     self.moveAvailability(board,color),
                     self.pieceCapturability(board,color),
                     self.kingProtection(board,color)
                ]

            return featuresArray

              
        def canSeeEnemyKing (self,board,color,visibility):
            for r in range(board.rows):
                for c in range(board.cols):
                    sq=board.grid[r][c]

                    if sq.is_occupied and  sq.pieceOccupying.color != color and sq.pieceOccupying.symbol=="K":
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
                       if squareToVisit not in squaresVisited:
                            boardSquare= board.grid[m.newRow][m.newCol]
                            if boardSquare.is_occupied:
                                print(boardSquare.pieceOccupying.Value)
                                capValue+=boardSquare.pieceOccupying.Value
                                squaresVisited.add(squareToVisit)
            return min((capValue/30),1.0)
        #FIx later off board areas mean safety so include iun count 
        def kingProtection(self,board,color):

            for r in range(board.rows):
                for c in range(board.cols):
                    sq=board.grid[r][c]

                    if sq.is_occupied and  sq.pieceOccupying.color == color and sq.pieceOccupying.symbol=="K":
                        count=sq.pieceOccupying.numPiecesSurrounding(board)
                        protectionRatio=count/8
                        return protectionRatio
                        

           

            # if game end
            return 0.0 
        
        def getQvalue(self,features):
             
            qVal= sum(weight*feature for weight,feature in zip(self._weights,features))
            return qVal
        def updateWeights(self,prevFeatures,tempralDiff):
            self._weights=[weight+(self._learningRate*tempralDiff*feature) for weight,feature in zip(self._weights,prevFeatures)]
             
        def select_move(self,board,legal_moves,color):
             
            #DO NOT UPDATE THE SQUARES WHEN RUNNING THE RL IT BREAKS FOG MASK 
            visibleSquares= board.getVisibleSquares(color)  

            if random.random()<self._epsilon:
                return random.choice(legal_moves)


           
            bestMove=None
            bestScore=float('-inf')
            for m in legal_moves:
                bCopy=board.copyBoard()
                bCopy.apply_move(m)
                features=self.extractFeatures(bCopy,color,visibleSquares)
                score= self.getQvalue(features)



  
                if score>bestScore:
                     bestScore=score
                     bestMove=m
                
            return bestMove

