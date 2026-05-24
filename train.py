from QLearning import QLearningAgent
from game import Game
from board import Board
import random
def train(numEpochs):
    agent = QLearningAgent()
    weightHistory = []
    winRate=[]
    lossRate=[]
    drawRate=[]

    
    totalResults = {"White": 0, "Black": 0, "Draw": 0}
    midTrainResults = {"White": 0, "Black": 0, "Draw": 0}
    
    for epoch in range(numEpochs):
        gameRun = Game()
        result = gameRun.selfPlay(agent, epoch)
        totalResults[result] += 1
        windowResults[result] += 1
        weightHistory.append(agent.weights.copy())
       
        
        if (epoch + 1) % 10 == 0:
            total = sum(midTrainResults.values())
            drawRate = midTrainResults['Draw'] / total * 100
            print(f"Epoch {epoch+1}: White={windowResults['White']} Black={windowResults['Black']} Draws={windowResults['Draw']} | DrawRate={drawRate:.0f}%")
            print(f"Weights: {[f'{w:.4f}' for w in agent._weights]}")
            windowResults = {"White": 0, "Black": 0, "Draw": 0}
    
    print(f"\nTotal results over {numEpochs} epochs:")
    print(f"White={totalResults['White']} Black={totalResults['Black']} Draws={totalResults['Draw']}")
    print(f"Draw rate: {totalResults['Draw']/numEpochs*100:.0f}%")
    print(f"Final weights: {agent._weights}")
    return agent