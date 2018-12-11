# IMPORT APPROPIATE LIBRARIES
import random

# CREATING THE AGENT CLASS
class Agent:
    #Constructor of Agent
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)  #randomly selects a starting position from 0-99 for x.axis
        self.y = random.randint(0,99)  #randomly selects a starting position from 0-99 for y-axis
        self.environment = environment #used as food for the agents, as used in def eat(self)
        self.store = 0                 #creates the food stores for the agents used in def eat(self)
        self.agents = agents           #used for the sharing_with_neighbour definition
    
    #Defining movement patterns
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100 #if random number is <0.05, add 1 to the y-axis of the agent
        else:
            self.y = (self.y - 1) % 100 #if random number is >0.05, subtract 1 from the y-axis of the agent

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100 #if random number is <0.05, add 1 to the x-axis of the agent
        else:
            self.x = (self.x - 1) % 100 #if random number is >0.05, subtract 1 from the x-axis of the agent
    
    #Defining eating patterns
    def eat(self): 
        if self.environment[self.y][self.x] > 10:   #if the environment has more than 10
            self.environment[self.y][self.x] -= 10  #deduct 10 from the environment
            self.store += 10                        #and add 10 to the agent's store of food
        else:
            self.store += self.environment[self.y][self.x]  #if the store is equal to the environment's value
            self.environment[self.y][self.x] = 0            #deplete the environment's value so it equals 0
        
        #If self-stores (of food) become too big, make the agents puke it back into the environment
        if self.store>=10000:                               #if the self.stores are more than or equal to 10,000:
            self.environment[self.y][self.x] += 60          #add 60 back to the environment and;
            self.store=0                                    #reset the store of the agent to 0 again


# NOTE: "self.environment[self.y][self.x] += 60" is set to 60 in order for the environment to eventually be depleted.
# Otherwise the animation will continuously run if it is set to the same as the self.store of 10,000.
# This allows for a stopping condition to be reached once the environment reaches 0.


    #Defining sharing of food eaten between close-by Agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:           #if the distance between self and agents is less than the neighbourhood defined in the model;
                sum = self.store + agent.store  #add the two agent's food stores together
                ave = round(sum/ 2)             #divide and average the two stores. Round is used to display no decimal places in the animation
                self.store = ave                #and give the two agents the same averaged food stores
                agent.store = ave
                
    #Calculate the distance between Agents using Pythagoras' theorem
    def distance_between(self, agent):
        return (((self.x - agent.x) **2) + ((self.y - agent.y)
                 **2))**0.5
