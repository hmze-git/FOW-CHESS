from game import Game
from move import Move
from QLearning import QLearningAgent
from train import train
import json
#g = Game()
#g.viewMoves()
#b=g.board


#move = b.grid[4][0].pieceOccupying.viewLegalMoves(b)[0]
#print(f"Applying: {move}")
#b.apply_move(move)

# manually force a king capture
#amove = Move(5, 3, 0, 4, g.board.grid[5][3].pieceOccupying, True)
#print(f"testing: {amove}")
#g.board.apply_move(amove)
#print(g.board.checkWinner(amove))  # should print "white"
#b.printBoard()

#s= g.board.copyBoard()
#q=QLearningAgent()
#print("ORG")
#b.printBoard("White")
#b.printBoard("Black")

#bestMove=q.select_move(b,b.getLegalMoves("White"),"White")

#print("BEST MOVE IS", bestMove)
#print("COP")
#s.printBoard("White")
#s.printBoard("Black")
#g.selfPlay()
a=train(500)

#save final weights to file
a.saveWeights()

#load from file




#run sims against random agent

def load_weights_json(agent, filename="trained_weights.json"):
    f=open(filename, 'r')
    weights_data = json.load(f)
    agent._weights = weights_data["Weights"]
    print(f"Weights loaded: {agent.weights}")
    return agent

# Usage:
agent = QLearningAgent()
load_weights_json(agent, "trained_weights.json")
g=Game()

g.randomVsTrained(agent,200,"White")
