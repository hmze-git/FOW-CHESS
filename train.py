from QLearning import QLearningAgent
from game import Game
from board import Board
import random
import matplotlib.pyplot as plt
def train(numEpochs):
    agent = QLearningAgent()
    weightHistory = []
    winRates=[]
    lossRates=[]
    drawRates=[]
    temporalDiffGameHistory=[]

    
    totalResults = {"White": 0, "Black": 0, "Draw": 0}
    midTrainResults = {"White": 0, "Black": 0, "Draw": 0}
    
    for epoch in range(numEpochs):
        gameRun = Game()
        result, temporalDiffOverTime = gameRun.selfPlay(agent)
        averageTD= sum((temporalDiffOverTime))/len(temporalDiffOverTime)
        temporalDiffGameHistory.append(averageTD)
        totalResults[result] += 1
        midTrainResults[result] += 1
        weightHistory.append(agent.weights.copy())
        agent._epsilon = max(0.05,agent._epsilon * 0.995) # epsilon decay over time to reduce exploration

       
        #The agent always plays as white
        if (epoch + 1) % 10 == 0:
            total = sum(midTrainResults.values())
            drawRate = midTrainResults['Draw'] / total 
            winRate = midTrainResults['White'] / total 
            loseRate = midTrainResults['Black'] / total 
            winRates.append(winRate)
            lossRates.append(loseRate)
            drawRates.append(drawRate)
    
    print(f"\nTotal results over {numEpochs} epochs:")
    print(f"White={totalResults['White']} Black={totalResults['Black']} Draws={totalResults['Draw']}")
    print(f"Draw rate: {totalResults['Draw']/numEpochs*100:.0f}%")
    print(f"Final weights: {agent._weights}")
    plotWeightResults(weightHistory)
    plotWinRates(winRates,lossRates,drawRates)
    plotTemporalDiff(temporalDiffGameHistory)
    return agent

def plotWeightResults(weightHistory):

    xlabels=[
        "See King",
        "Visibility",
        "Mobility",
        "Capturability",
        "King Protection"
    ]
    # flip epcohs and features to take one feature at a time and plot its value over training
    weightsFlipped= list(zip(*weightHistory))
    for i,weights in enumerate(weightsFlipped):
        plt.plot(weights,label=xlabels[i])
    plt.xlabel("Epochs")
    plt.ylabel("Weight Value")
    plt.title("Feature Weights During Training")
    plt.legend()
    plt.savefig("weight_history.png")
    plt.close()

def plotWinRates(winRates,lossRates,drawRates):

    x= [ i*10 for i in range(len(winRates))]

    plt.plot(x,winRates,label="Win Rate")
    plt.plot(x,lossRates,label="Loss Rate")
    plt.plot(x,drawRates,label="Draw Rate")

    plt.xlabel("Aggregate Game Results vs Random Agent")
    plt.ylabel("Rate")
    plt.title("Win/Loss/Draw Rates During Random Agent Play")
    plt.legend()
    plt.savefig("win_rates.png")
    plt.close()

def plotTemporalDiff(temporalDiffGameHistory):
    x= [ i for i in range(len(temporalDiffGameHistory))]
    plt.plot(x,temporalDiffGameHistory,label="Average Temporal Difference Per Game")
    plt.xlabel("Epochs")
    plt.ylabel("Average Temporal Difference")
    plt.title("Average Temporal Difference Per Game During Training")
    plt.legend()
    plt.savefig("temporal_diff_history.png")
    plt.close()