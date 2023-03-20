# Github Link - https://github.com/whosthemaan/A_Star_Path_Planning
# Youtube Link - https://youtu.be/AUeOfSFBoyg

from includes import *

if __name__ == '__main__':
    
    c = input("Enter Clearance of the Robot: ")
    c = int(c)

    r = input("Enter the Radius of the Robot: ") 
    r = int(r)
    
    robot_step_size = input("Enter Step size of the Robot: ")
    robot_step_size = int(robot_step_size)

    start_coordinates = input("Enter coordinates for Start Node: ")
    start_x, start_y = start_coordinates.split()
    start_x = int(start_x)
    start_y = int(start_y)
    
    s_theta = input("Enter Orientation of the robot at start node: ")
    start_theta = int(s_theta)
    
    if robot_radius_space(start_x, start_y, c, r):
        print("Start node is out of bounds")
        exit(-1)
        
    if not (start_theta%30)==0:
        print("Orientation has to be a multiple of 30")
        exit(-1)
		    
    goal_coordinates = input("Enter coordinates for Goal Node: ")
    goal_x, goal_y = goal_coordinates.split()
    goal_x = int(goal_x)
    goal_y = int(goal_y)
    
    g_theta = input("Enter Orientation of the robot at goal node: ")
    goal_theta = int(g_theta)
    
    if robot_radius_space(goal_x, goal_y, c, r):
        print("Goal node is out of bounds")
        exit(-1)
        
    if not (goal_theta%30)==0:
        print("Orientation has to be a multiple of 30")
        exit(-1)
    
    start_node = Node(start_x, start_y,start_theta, 0.0, -1,0)
    goal_node = Node(goal_x, goal_y,goal_theta, 0.0, -1, 0)
    all_nodes,flag = a_star(start_node, goal_node, robot_step_size, c, r)
    
    if (flag)==1:
        universal_path = backtrack(goal_node)
    else:
        print("Robot cannot explore with current robot radius and clearance, please try again!")
        exit(-1)

    animate(all_nodes, universal_path, c, r)


	



	











