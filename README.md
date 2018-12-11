# Agent Based Model

This repository is made for an assignment at the University of Leeds for the module *Programming for Social Sciences*. The ABM is created using Python and is simulating the characteristics of sheep in a field.

To use this code, all files within this repository must be downloaded.
- model.py - has the base model required for the ABM
- agentframework.py - defines the class Agent for the model
- in.txt - has the relevant environment data for the ABM

When running the code in some Python applications, the following piece of code may be used to make the animation run in a pop-out window:
**%matplotlib qt**

That line of code must be ran in the console, as it will not work within the script. A note of this has been made at the bottom of the model if forgotten.

## What is an Agent-Based Model?
ABMs are generally iterative models. They run by allowing the agents to do their thing for a time step repeatedly (for example, representing someone doing a day's activities) until some number of time steps (iterations) have run, or some stopping condition has been reached. System-level patterns emerge from the complex interactions of the multiple, relatively simple, behaviours of the agents in the model.

My Model
The ABM simulates the randomised movement of sheep eating grass in the field, with the grass being the environment.

Within the ABM, the following variables can be altered as required:

- num_of_iterations (the number of times the animation loops)
- num_of_agents (the number of sheep)
- neighbourhood (how close the agents can be together)

The ABM displays a number next to each agent; this number represents the agents current store of food (i.e. grass). The agents share their food storage when within a certain distance away (defined by the neighbourhood value). You can observe this by watching their annotated store numbers becoming the same with any nearby agents.

The ABM is designed to continue until a stopping condition is met. This condition has been set to when the environment has been emptied. The quickest way to test this is to set the num_of_iterations to a large number (e.g. 1000) and wait for the environment to turn a dark blue. The agents will stop moving and Stopping condition will be seen in the IPython console.
