# A* Path Planning
Project by: Rohan Maan and Omkar Chittar

Libraries used:
1. cv2
2. numpy
3. math
4. heapq

## We can run the code using the following command:

    python3 A-star_path_planner.py

## Sample inputs:

Enter Clearance of the Robot: 2

Enter the Radius of the Robot: 2

Enter Step size of the Robot: 1

Enter coordinates for Start Node: 11 11

Enter Orientation of the robot at start node: 30

Enter coordinates for Goal Node: 238 588

Enter Orientation of the robot at goal node: 60
 
## Output
![image](https://user-images.githubusercontent.com/40595475/226489376-81d3bf6e-80c8-4421-b829-f5b633a6c3eb.png)

Note: If the radius of the robot and the clearance combined create hinderance in the path of the robot, it will stop the navigation and give an error. Please retry in that case. The sum of two cannot be greater than 4 to reach every coordinate of the given field.
