import random
import json
class QLearningAgent:
        def __init__(self):
            self._weights=[random.uniform(-0.1, 0.1) for _ in range(5)]
            self._epsilon=0.2
            self._learningRate=0.05 # slow learning set high number of epochs so can see smoth curve
            self._discountFactor=0.6 # since there is no monte carlo integration discount is set to a more greedy value to force imeediate learing 

        @property
        def discountFactor(self):
            return self._discountFactor
        
        @property
        def weights(self):
            return self._weights
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
            for (r,c) in visibility:
                    sq=board.grid[r][c]

                    if sq.is_occupied and  sq.pieceOccupying.color != color and sq.pieceOccupying.symbol=="K":
                        return 1.0 if (r,c) in visibility else 0.001 
                              
            return 0.0
        def visibilityLevel (self,visibleSquares):
             # level of visibility depends on the board and the number of squares that can currently be seen
             # do this to scale down the feature to match can see king otherwise its wonky
             
             return len(visibleSquares)/30
        def moveAvailability(self,board,color):
             moves=board.getLegalMoves(color)

            # this might break later if too many moves become available
             return len(moves) / (board.rows*board.cols)
        def pieceCapturability(self,board,color):
            moves = board.getLegalMoves(color)
            totalCapturesAvailable=0
            squaresVisited = set() # prevent double counting capturing of a piece

            for m in moves:
                        
                       
                       tagetSq=board.grid[m.newRow][m.newCol]

                       if tagetSq.is_occupied and tagetSq.pieceOccupying.color!=color:
                            squareToVisit= (m.newRow,m.newCol)
                            if squareToVisit not in squaresVisited:
                                       
                                totalCapturesAvailable+=tagetSq.pieceOccupying.Value #Scale captures to the same level as the learning loop to prevent weird mismatches
                                squaresVisited.add(squareToVisit)
            if len(moves)==0:
                return 0.0
            return min(totalCapturesAvailable/10.0,1.0) 
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
            self._weights=[
                 
                weight+(self._learningRate*tempralDiff*feature) for weight,feature in zip(self._weights,prevFeatures)]
             
        def selectMove(self,board,legal_moves,color,learning=True):
             
            #DO NOT UPDATE THE SQUARES WHEN RUNNING THE MOVE CHANGE IT BREAKS FOG MASK 
            #visibleSquares= board.getVisibleSquares(color)  

            if learning:
                if random.random()<self._epsilon:
                    return random.choice(legal_moves)
            


           
            bestMove=None
            bestScore=float('-inf')
            for m in legal_moves:
                bCopy=board.copyBoard()
               

                bCopy.apply_move(m)
                visibleSquares= bCopy.getVisibleSquares(color)  
                features=self.extractFeatures(bCopy,color,visibleSquares)
                score= self.getQvalue(features)



  
                if score>bestScore:
                     bestScore=score
                     bestMove=m
                
            return bestMove

        def saveWeights(self,fileName="trained_weights.json"):
            weightData={
                
                "Weights":self._weights,
                "Epsilon":self._epsilon,
                "LeraningRate": self._learningRate, 
                "DiscountFactor":self._discountFactor, 

            }
            out_file=open(fileName,"w")
            json.dump(weightData,out_file,indent=4)

