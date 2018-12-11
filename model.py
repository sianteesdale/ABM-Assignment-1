"""
NOTE: Before running the animation, run the following code in the console to
ensure the animation will be ran in a pop-out window:
    %matplotlib qt
Failure to do so will result in the animation not being displayed.

"""

# IMPORT APPROPIATE LIBRARIES
import matplotlib.pyplot #Used for plotting
import matplotlib.animation #Used for animations
import agentframework #Contains functions for the 'Agent' class
import csv #Used to read in csv files


# SETTING UP THE VARIABLES
# With [] being empty lists that will be filled 
agents = []
environment = []
num_of_agents = 10 #define how many agents will be shown
num_of_iterations = 1000 #define how many iterations (loops)
neighbourhood = 20 #define distance for agents to interact together


# READ IN THE ENVIRONMENT
#Create a new text file to input the environment
f = open('in.txt', newline='')
#Read in the csv with environment data
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []                    #create an empty list for rowlist to enter information into
    for value in row:
        rowlist.append(value)       #add the value to a rowlist
    environment.append(rowlist)     #add the environment to the rowlist
#And close the text file
f.close()


# MAKING THE AGENTS
#Append the agents to the environment above and the agentframework
for i in range(num_of_agents):      #run the for-loop for the number of agents defined
    agents.append(agentframework.Agent(environment,agents))


# SET UP THE MODEL
#Set-up the dimensions of the figure
fig = matplotlib.pyplot.figure(figsize=(14, 14))

#Creating the model for the animation
def update(frame_number):
    global carry_on
    fig.clear()  
    matplotlib.pyplot.imshow(environment)  #display the environment
    #Make the agents move, eat and share food stores with neighbours for the number of iterations defined
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 
    #Plot the agents and annotate their individual food stores        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker="*", c="white", s=500)
        matplotlib.pyplot.annotate(agents[i].store, (agents[i].x,agents[i].y), fontsize=15, 
                                   color="orange", weight="bold", va="bottom", ha="right")
    #Setting up the x and y axis limits, plotting the title and turning the axis off
    matplotlib.pyplot.ylim(0,99)
    matplotlib.pyplot.xlim(0,99) 
    matplotlib.pyplot.title("Agent Based Model - Sheep", fontsize='xx-large')
    matplotlib.pyplot.axis('off')
#Creating the stopping condition, whereby if the environment is emptied, the animation stops
    total=0
    for row in range(99):
        for value in range(99):
           total += environment[row][value]
    if total <= 0:
        carry_on = False
        print('Stopping condition')
#Defining carry_on
carry_on = True

#Loops animation until 'num_of_iterations' and carry_on is met
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			
        a = a + 1

# SETTING UP THE ANIMATION AND DISPLAY MODEL        
#Create the animation and display using matplotlib library
animation = matplotlib.animation.FuncAnimation(fig, update, 
                                               frames=gen_function)
#Show the animation
matplotlib.pyplot.show()
