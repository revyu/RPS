# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
"""
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
"""


import numpy as np
from numpy import random as r
from typing import Type ,Union


def decode(x):
    _={"R":0,"P":1,"S":2}
    return _[x]

def encode(x):
    _={0:"R",1:"P",2:"S"}
    return _[x]

#choosed winner 
#decoded responsible in what form we obtain data
#return 1 if x win -1 ,if y win 0 if tie
def decide_winner(x,y,decoded=True):
    if decoded:
        winning_situations = [[0, 2], [2, 1], [1, 0]]
        if [x, y] in winning_situations:
            return 1
        elif x == y:
            return 0
        else:
            return -1
    else:
        x,y=decode(x),decode(y)
        winning_situations = [[0, 2], [2, 1], [1, 0]]
        if [x, y] in winning_situations:
            return 1
        elif x == y:
            return 0
        else:
            return -1
        


class bot():
    def __init__(self,strategy_) -> None:
        self.strategy=strategy_
        self.__history=[]
    
    def play(self):
        if self.strategy=="mrugesh":
            return self._mrugesh()
        elif self.strategy=="kris":
            return self._kris()

    def update_history(self,move):
        self.__history.append(move)

    def _mrugesh(self):
        last_ten=self.__history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[most_frequent]
    
    def _kris(self):
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[self.__history[-1]]
    
        

class player():
    def __init__(self) -> None:
        self.Q=np.zeros((9,3)) 
        self.STATES={
        (0, 0): 0,
        (0, 1): 1,
        (0, 2): 2,
        (1, 0): 3,
        (1, 1): 4,
        (1, 2): 5,
        (2, 0): 6,
        (2, 1): 7,
        (2, 2): 8
    }  
        self.state=0
        self.current_action=0
    
    def fit(self,opponent:Union["player",bot],nums_of_epochs=1000,epsilon=0.8,discount=0.3,alpha=0.7,alpha_decay=1,epsilon_decay=0.9999):
        
        current_action=0
        opponent.update_history(encode(current_action))
        current_opponent_action=decode(opponent.play())
        for i in range(nums_of_epochs):
            

            reward=decide_winner(current_action,current_opponent_action)
            
            next_state=self.STATES[(current_action,current_opponent_action)]


            self.Q[self.state,current_action]+=alpha * (reward + discount * self.Q[next_state, self.Q[next_state, :].argmax()] -self.Q[self.state, current_action])

            self.state=self.STATES[(current_action,current_opponent_action)]

            if epsilon>r.uniform(0,1):
                current_action=r.choice([0,1,2])
            else:
                current_action=np.argmax(self.Q[self.state, :])
            
            epsilon *= epsilon_decay
            alpha *= alpha_decay

            opponent.update_history(encode(current_action))
            current_opponent_action=decode(opponent.play())

    def play(self,opponent,num_games,verbose=False):
        results={"player":0,"opponent":0,"tie":0}
        
        for _ in range(num_games):
            
            my_action=np.argmax(self.Q[self.state, :])
            opponent_action=decode(opponent.play())

            opponent.update_history(encode(my_action))
            self.state=self.STATES[(my_action,opponent_action)]

            winner=decide_winner(my_action,opponent_action)

            if winner==1:
                results["player"]+=1
            elif winner==0:
                results["tie"]+=1
            else:
                results["opponent"]+=1

            if verbose:
                if winner==1:
                    print(f"P1:{my_action}, P2:{opponent_action} ; P1 wins ; winrateP1={(results['player']/(_+1)):3f}")

                if winner==0:
                    print(f"P1:{my_action}, P2:{opponent_action} ; P1 wins ; winrateP1={(results['player']/(_+1)):3f}")

                if winner==1:
                    print(f"P1:{my_action}, P2:{opponent_action} ; P1 wins ; winrateP1={(results['player']/(_+1)):3f}")

        print(f"{results}, winrate={(results['player']/(num_games)):3f}")

    
    def __str__(self):
        return self.Q





if __name__=="__main__":
    def func(Q=np.zeros((9,3))):
        return Q
    
    print(func())