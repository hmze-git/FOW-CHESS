from game import Game
from move import Move
from QLearning import QLearningAgent
g = Game()
g.viewMoves()
b=g.board


#move = b.grid[4][0].pieceOccupying.viewLegalMoves(b)[0]
#print(f"Applying: {move}")
#b.apply_move(move)

# manually force a king capture
#amove = Move(5, 3, 0, 4, g.board.grid[5][3].pieceOccupying, True)
#print(f"testing: {amove}")
#g.board.apply_move(amove)
#print(g.board.checkWinner(amove))  # should print "white"
#b.printBoard()

s= g.board.copyBoard()
q=QLearningAgent()
#print("ORG")
#b.printBoard("White")
#b.printBoard("Black")

#bestMove=q.select_move(b,b.getLegalMoves("White"),"White")

#print("BEST MOVE IS", bestMove)
#print("COP")
#s.printBoard("White")
#s.printBoard("Black")
g.selfPlay()