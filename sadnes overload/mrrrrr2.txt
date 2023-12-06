#!/usr/bin/env python
import rospy
from get_ar_pos.msg import PointArray


class PlanPath:
    def __init__(self):
        rospy.init_node('path_planner', anonymous=True)
        rospy.Subscriber('/goal_points', PointArray, self.path_planning_callback)
        
        r = rospy.Rate(10)
        r.sleep()
        
        rospy.spin()
        
    def path_planning_callback(self, msg):
        counter = 0
        for goal in msg.points:
            X_goal, Y_goal, Z_goal = goal.x, goal.y, goal.z
            print("Goal {}: (X, Y, Z) = ({:.2f}m, {:.2f}m, {:.2f}m)".format(counter, X_goal, Y_goal, Z_goal))
            counter += 1

        
if __name__ == '__main__':
    PlanPath()
  
  
