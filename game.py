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
        lastFeatures={"White":None,"Black":None}
        while self._numMoves<200:

            color ="White" if self._isWhitesTurn else "Black"
            moves=self.getLegalMoves(color)
 
            if not moves:
                
                return "Draw"
            
            moveMade=None
            visibleBefore= self.board.getVisibleSquares(color)
            featuresBefore = QAgent.extractFeatures(self._board,color,visibleBefore)
            qBeforeMove=QAgent.getQvalue(featuresBefore)

            moveMade=QAgent.selectMove(self._board,self._board.getLegalMoves(color),color)
            self._board.apply_move(moveMade)

            if featuresBefore[0] > 0:  # canSeeEnemyKing
                print(f"King visible at move {self._numMoves}")
 
            if moveMade.wasCap:
                print(f"CAPTURE: {color} captured {moveMade.capturedPiece.symbol}")

            reward=0.0

            if moveMade.wasCap:
                if moveMade.capturedPiece.symbol =="K":
                     reward= 3.0
                else:
                    reward= (moveMade.capturedPiece.Value/ 10) #9 is the highest value in the queen in this way capturing a piece returns that isnt king gives 0.9 and the king 1.0

            visibleAfter = self._board.getVisibleSquares(color)
            featuresAfter = QAgent.extractFeatures(self._board,color,visibleAfter)
            qAfterMove= QAgent.getQvalue(featuresAfter)

            #SARSA because we work with actions actually taken not what we can take and its value
            temporalDiff=reward+QAgent.discountFactor*qAfterMove-qBeforeMove


            print(f"Weight Before {QAgent.weights}")
            QAgent.updateWeights(featuresBefore,temporalDiff) # update weights based on how much better or worse the position is now
            print(f"Weight After {QAgent.weights}")

            lastFeatures[color]=featuresAfter

            #returns winning pieces color
            result = self._board.checkWinner(moveMade)
            if result==color:
                print(f"{result} is the winner")
                reward=10.0
            else:
                reward=-10.0
            
            
                # since were using 1 agent use loss signal as well 
                # updates weights to account for what leads to a loss or bad outcome with a strong signal
                loserColor="Black" if result =="White" else "White"
                terminalDiff=-3.0-QAgent.getQvalue(lastFeatures[loserColor])

                #use features after is the position that led to a loss so we want those features to be associated with a loss
                QAgent.updateWeights(lastFeatures[loserColor],terminalDiff)
                return result

            self._isWhitesTurn = not self._isWhitesTurn
            self._numMoves += 1
        return "Draw"

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
