#!/usr/bin/env python3
import rospy
import numpy as np

from get_ar_pos.msg import PointArray
from trajectory import get_trajectory
from trajectory import plot_trajectory
class PlanPath:
    def __init__(self):
        rospy.init_node('path_planner', anonymous=True)
        print('aaaaa')
        self.path = []
        rospy.Subscriber('/goal_points', PointArray, self.path_planning_callback)
        print('bbbbbbb')
        
        rate = rospy.Rate(1)
        rate.sleep()
        #print('grrrrr')
        plot_trajectory(self.path, 75)
        #print('wwwwww')
        
        
    def path_planning_callback(self, msg):
        #print('meow')
        targets = [(0.0,0.0)]
        counter = 0
        for goal in msg.points:
            X_goal, Y_goal, Z_goal = goal.x, goal.y, goal.z
            print("Goal {}: (X, Y, Z) = ({:.2f}m, {:.2f}m, {:.2f}m)".format(counter, X_goal, Y_goal, Z_goal))
            counter += 1
            if goal.x == 0.0 and goal.y == 0.0:
                continue
            else:
                targets.append((goal.x, goal.y))
                   
        dist_arrays = self.create_dist_array(targets)
        order = self.tsp_dp(dist_arrays)
        print("Order is:")
        print(order)
        optimized_targets = self.recover_targets(targets, order)
        interval = 75
        self.path = get_trajectory(optimized_targets, interval)
        
        
    def recover_targets(self,  targets, order):
        optimized_targets = []
        for i in order:
            optimized_targets.append(targets[i])
        return optimized_targets
        
    def distance(self, point1, point2):
        return np.linalg.norm(np.array(point1) - np.array(point2))
        
    def create_dist_array(self, targets):
        dist_arrays = []
        for i_point in targets:
            dist_arr = []
            for j_point in targets:
                dist_arr.append(self.distance(i_point, j_point))
            dist_arrays.append(dist_arr)
        return dist_arrays
        
    def tsp_dp(self,dist_arr):
        # BEGIN SOLUTION
        n = len(dist_arr)
        dp = {}
        prev = {}
        def tsp_helper(S, i):
        
            if (S, i) in dp:
                return dp[(S, i)]
            if S == frozenset():
                return dist_arr[0][i] # Return to the starting city
                
            min_cost = float('inf')
            prev_city = None
            
            for city in S:
                cost = dist_arr[i][city] + tsp_helper(S.difference({city}), city)
                min_cost, prev_city = min((min_cost, prev_city) , (cost, city))
                dp[(S, i)] = min_cost
                prev[(S, i)] = prev_city
            return min_cost
        best_distance = tsp_helper(frozenset(range(1, n)), 0)
        
        # Backtracking to reconstruct tour
        S = frozenset(range(1, n))
        city = 0 # start at the origin
        tour = [0]
        # print(prev)
        
        while S:
            city = prev[(S, city)]
            tour.append(city)
            S = S.difference({city})
        return tour + [0]
    
        
if __name__ == '__main__':
    PlanPath()

