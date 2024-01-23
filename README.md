# NaoWay
The aim of this project is to implement an algorithm so that the NaO robot can score a goal with a yellow ball in the VREP simulation tool. 

The project is made up of different files:
- `naocrouch.py`, `moveto.py`, `reset_autonomous_life.py` and `square_walk.py` files, which contain functions for moving the robot in its environment;
- `detection_but.py`: file with a function for detecting the 4 edges of soccer goals
- `detection.py`: file with the yellow ball detection function. It measures the circularity of the detected yellow object to recognize the ball.
- `nao_simple_test.py`: file in which we have implemented yellow ball recognition. This code shows the filter applied to the camera to detect and recognize the yellow ball.
- `turn_body.py`: main file for the robot to score the goal. 

## `turn_body.py`
In order for the robot to score a goal, the robot has a precise gait.  

First of all, it will try to detect the yellow ball around it. If it doesn't detect it at the start of the simulation, it turns on himself (his head doesn't move). 

Then, once it has detected the ball, the robot moves towards it up to a certain distance. Once it has passed this distance, it moves back a few steps. This ensures a constant distance to the ball for all simulations. 

It then turns around the ball, always facing it (and therefore walking sideways). It repeats this action until it detects the four red edges of the goals. 

When it has detected them, it continues to move forward a little in the same way, and when he is lined up, moves in a straight line, straight ahead of it to advance towards the ball and score a goal.

## Run the code

To run the code and see the robot score, all you need to do is run the following code in your terminal once you are in the right folder and VREP is running :
```
python turn_body.py
```
## Description of `detection.py`

This python file has two functions :
- **detect_yellow_ball** : converts the image to HSV and applies a mask to the camera image. A cicularity calculation is also implemented to recognize a round object and displays the binarized image with the mask applied to the ball. Finally, it measures the ball's barycenter in order to trace the ball's contour.

- **distance_to_ball** : this function calculates the robot's distance from the ball it sees.

## Description of `detection.py`

For the robot to align itself on the axis in relation to the soccer cages, it needs to detect the 4 edges of the cages. The **detect_red_goal** function converts the camera image into HSV format and detects the color red. A counter counts exactly four red corners.

