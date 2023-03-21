# A* Path Planning
Project by:  **Rohan Maan(rmaan, 119061770) and Omkar Chittar(ochittar, 119193556)**

Libraries used:
1. cv2
2. numpy
3. math
4. heapq

## Assumptions of A* Path Planning

1. Considering Euclidean Distance as the Heuristic function
2. A threshold of 1.5 unit of distance from the goal is considered as goal reached

<p align="center">
<img src="https://user-images.githubusercontent.com/40595475/226610891-f5fa8f53-f09c-4273-9f91-ad29ce2cead3.png" alt= “” width="600" height="300">
</p>
<p align="center"> Fig1. Field Dimensions </p>

### Action Set

   1. Euclidean distance threshold is 0.5 unit(for x,y)
    
   2. Theta threshold is 30 degrees
    
<p align="center">
<img src="https://user-images.githubusercontent.com/40595475/226612898-0d5a1491-eb62-4128-bd0b-6cd2abe435b7.png" alt= “” width="300" height="300">
</p>
<p align="center"> Fig2. Action Set </p>

## Run Command

    python3 a_star_Rohan#1_Omkar#2.py

## Sample inputs:

    Enter Clearance of the Robot: 2

    Enter the Radius of the Robot: 2

    Enter Step size of the Robot: 1

    Enter coordinates for Start Node: 11 11

    Enter Orientation of the robot at start node: 30

    Enter coordinates for Goal Node: 238 588

    Enter Orientation of the robot at goal node: 60
 
## Output

<p align="center">
<img src="https://user-images.githubusercontent.com/40595475/226656046-b709b392-96e1-4342-9464-f5dbdea0ee51.gif" >
</p>

Note: If the radius of the robot and the clearance combined create hinderance in the path of the robot, it will stop the navigation and give an error. Please retry in that case. The sum of two cannot be greater than 4 to reach every coordinate of the given field.
