from unittest import result

from board import Board
import random
from QLearning import QLearningAgent
class Game:
   
    def __init__(self):
        self._board = Board(6,5)
        self._whiteCaps=[]
        self._blackCaps=[]
        self._numMoves =0
        self._isWhitesTurn=True

    def viewMoves(self):
                
        moves = []
        for r in range(self._board.rows):
            for c in range(self._board.cols):
                sq = self._board.grid[r][c]
                if sq.is_occupied and sq.pieceOccupying.color == "White":
                    moves.extend(sq.pieceOccupying.viewLegalMoves(self._board))

        print(f"Total white moves: {len(moves)}")
        for m in moves:
            print(m)
    def getLegalMoves(self,color):
        moves = []
        color = color

        for r in range(self._board.rows):
            for c in range (self._board.cols):
                sq = self._board.grid[r][c]
                if sq.is_occupied and sq.pieceOccupying.color == color:
                    moves.extend(sq.pieceOccupying.viewLegalMoves(self._board))
        return moves
    @property
    def board(self):
        return self._board


    def selfPlay(self,QAgent,epochNum):
        print(f"Epoch Number: {epochNum}")
        
        lastMove=None
        result=None
        while self._numMoves<200:

            color ="White" if self._isWhitesTurn else "Black"
            moves=self.getLegalMoves(color)
 
            if not moves:
                
                return "Draw"
            #Random agent self learning attempt 
            #if its not agents turn then apply random move and go on
            #if color!="White":
             #   moveMade= self.randomMove(moves)
              #  self._board.apply_move(moveMade)
               # result = self._board.checkWinner(moveMade)
                #if result is not None:
                 #   print(f"{result} is the winner")
                  #  return result
                #else:
                 #   continue

            #prev state
                 #returns winning pieces color
            #test if good keep if not then we take the featurres after
            
            if lastMove is not None:
                result = self._board.checkWinner(lastMove)
            if result is not None:

                finalReward=1.0 if result ==color else -1.0 #give a large reward for winning and a similar large punishment for losing
                temporalDiff=finalReward-qBeforeMove
                #use features after is the position that led to a loss so we want those features to be associated with a loss
                QAgent.updateWeights(featuresBefore,temporalDiff)
                return result

    
            visibleBefore= self.board.getVisibleSquares(color)
            featuresBefore = QAgent.extractFeatures(self._board,color,visibleBefore)
            qBeforeMove=QAgent.getQvalue(featuresBefore)

            lastMove=QAgent.selectMove(self._board, moves, color)
            self._board.apply_move(lastMove)

            #minor reward for making a move to push up wins
            reward=0.001 # introduce a small reward for making moves because currently only captures and wins give rewards which may happen too spread out

            if lastMove.wasCap:
                    reward+= (lastMove.capturedPiece.Value/ 10) #9 is the highest value in the queen in this way capturing a piece returns that isnt king gives 0.9 and the king 1.0

        # after move state
            visibleAfter = self._board.getVisibleSquares(color)
            featuresAfter = QAgent.extractFeatures(self._board,color,visibleAfter)
            qAfterMove= QAgent.getQvalue(featuresAfter)

       
            temporalDiff=reward+QAgent.discountFactor*qAfterMove-qBeforeMove


            print(f"Weight Before {QAgent.weights}")
            QAgent.updateWeights(featuresBefore,temporalDiff) # update weights based on how much better or worse the position is now
            print(f"Weight After {QAgent.weights}")

            self._isWhitesTurn = not self._isWhitesTurn
            self._numMoves += 1
        return "Draw"
    def randomMove(self,moves):
        return random.choice(moves)
    def randomVsTrained(self,trainedAgent,NumRuns,trainedAgentCol):
        wins=0
        losses=0
        draws=0


        for _ in range(NumRuns):
            self.__init__()
            gameEnded=False
            while self._numMoves<200:


                color ="White" if self._isWhitesTurn else "Black"
                moves=self._board.getLegalMoves(color)

                if not moves:
                    draws+=1
                    gameEnded=True
                    break
  
            
                moveMade=None           
                if trainedAgentCol!=color:
                    moveMade= random.choice(moves)              
                    self._board.apply_move(moveMade)
                    #self._board.printBoard(color)
                    
                else:
                     #print(f"Trained agent turn: color={color}, trainedAgentCol={trainedAgentCol}, moves={len(moves)}")
                     #moveMade = trainedAgent.selectMove(self._board, self._board.getLegalMoves(trainedAgentCol), trainedAgentCol, False)
                     #print(f"Move selected: {moveMade}")
                     #self._board.apply_move(moveMade)
                    moveMade=trainedAgent.selectMove(self._board,self._board.getLegalMoves(trainedAgentCol),trainedAgentCol,False)
                    self._board.apply_move(moveMade)
                    self._board.printBoard(trainedAgentCol)

                result = self._board.checkWinner(moveMade)
                if result==trainedAgentCol:
                    wins+=1
                    gameEnded=True
                    break
                    
                elif result!=trainedAgentCol and result is not None:
                    losses+=1
                    gameEnded=True
                    break



                self._isWhitesTurn = not self._isWhitesTurn
                self._numMoves += 1

            if not gameEnded:
                draws+=1

        print(f"Wins:{wins}")
        print(f"Draws:{draws}")
        print(f"Losses:{losses}")
