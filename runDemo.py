from QLearning import QLearningAgent
from game import Game
from board import Board
import random
import json
def fileLogging(file,text):
    file.write(text +"\n")
    file.flush()


def humanVsAgentLoop(humanColor="Black",logFileName="human_vs_agent_log.txt"):
    g=Game()
    b=g.board
    q=QLearningAgent()
    load_weights_json(q) #load trained weights from JsonFile
    logFile=open(logFileName,"w")
    while g._numMoves<200:
        color ="White" if g._isWhitesTurn else "Black"
        moves=g.getLegalMoves(color)
        if not moves:
            print("No legal moves : Game Draw")
            fileLogging(logFile,"Game Over: Draw")
            break

        if color==humanColor:
            b.printBoard(humanColor)
            displayCurrentLegalMoves(moves)

            moveChosen=None
            while moveChosen is None:
                userInput=input("Enter your move in algebraic chess notation")
                if userInput.lower()=="quit":
                    return #exit condiiton
                
                moveChosen=algebraicToMove(userInput,moves)

                if moveChosen is None:
                    print("Invalid move. Please try again.")
            b.apply_move(moveChosen)
            moveALGuser= moveToAlgebraic(moveChosen)
            msgCapture= f" Capture: {moveChosen._capturedPiece.symbol}" if moveChosen.wasCap else ""
            print(f"You played: {moveALGuser} {msgCapture}")
            fileLogging(logFile,f"Human plays: {humanColor} {moveALGuser} {msgCapture}")
        else:
            fileLogging(logFile,b.boardToString(color))
            moveChosen=q.selectMove(b,moves,color,learning=False)
            b.apply_move(moveChosen)
            moveALGagent= moveToAlgebraic(moveChosen)
            msgCapture= f" Capture: {moveChosen._capturedPiece.symbol}" if moveChosen.wasCap else ""
            print(f"Agent plays: {color} {moveALGagent} {msgCapture}")
            fileLogging(logFile,f"Agent plays: {color} {moveALGagent} {msgCapture}")
        result = b.checkWinner(moveChosen)

        if result is not None:
            print(f"Game Over: {result} wins!")
            fileLogging(logFile,f"Game Over: {result} wins!")
            break
        g._isWhitesTurn = not g._isWhitesTurn
        g._numMoves += 1
    logFile.close()

def load_weights_json(agent, filename="trained_weights.json"):
    f=open(filename, 'r')
    weights_data = json.load(f)
    agent._weights = weights_data["Weights"]
    print(f"Weights loaded: {agent.weights}")
    return agent



COLUMNS=["a","b","c","d","e"]

def moveToAlgebraic(move):
    fromSq=f"{COLUMNS[move.oldCol]}{move.oldRow}"
    toSq=f"{COLUMNS[move.newCol]}{move.newRow}"
    return fromSq+"->"+toSq

def algebraicToMove(input,legalMoves):

    text=input.strip().lower()
    for move in legalMoves:
        if moveToAlgebraic(move)==text:
            return move
    return None

def displayCurrentLegalMoves(legalMoves):
    moves= [moveToAlgebraic(move) for move in legalMoves]
    print("Legal moves:")
    for move in moves:
        print(move)


humanVsAgentLoop()