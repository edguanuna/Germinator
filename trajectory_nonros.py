#!/usr/bin/env python


import math
import numpy as np

import matplotlib.pyplot as plt

def plot_trajectory(waypoints, interval):
    # Extracting x, y and theta values from the waypoints
    x_vals = [point[0] for point in waypoints]
    y_vals = [point[1] for point in waypoints]
    theta_vals = [point[2] for point in waypoints]
    
    # Plotting the trajectory
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, '-o', label='Trajectory')
    
    # Plotting the start and end points
    plt.scatter(x_vals[0], y_vals[0], color='green', s=100, zorder=5, label='Start')
    plt.scatter(x_vals[-1], y_vals[-1], color='red', s=100, zorder=5, label='End')
    for seed_point in range(interval, len(x_vals), interval):
        plt.scatter(x_vals[seed_point], y_vals[seed_point], color='orange', s=100, zorder=5, label='Seed')
    # Plotting orientation arrows along the trajectory
    for x, y, theta in waypoints:
        plt.arrow(x, y, 0.05 * np.cos(theta), 0.05 * np.sin(theta), head_width=0.01, head_length=0.005, fc='blue', ec='blue')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Robot Trajectory')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

def bezier_curve(p0, p1, p2, p3, t):
    """Calculate a point on a cubic Bezier curve defined by p0, p1, p2, and p3 at parameter t."""
    return (1-t)**3 * p0 + 3*(1-t)**2 * t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3

def generate_bezier_waypoints(x1, y1, theta1, x2, y2, theta2, offset=1.0, num_points=10):
    # 1. Calculate direction vector based on yaw
    direction_start = np.array([np.cos(theta1), np.sin(theta1)])
    direction_end = np.array([-np.cos(theta2), -np.sin(theta2)])  # Opposite direction for the end point

    # 2. Determine control points based on yaw and offset
    control1 = np.array([x1, y1]) + offset * direction_start
    control2 = np.array([x2, y2]) + offset * direction_end

    # 3. Sample points along the Bezier curve
    t_values = np.linspace(0, 1, num_points)
    waypoints = [bezier_curve(np.array([x1, y1]), control1, control2, np.array([x2, y2]), t) for t in t_values]

    # 4. Determine orientation at each point
    thetas = []
    for i in range(len(waypoints) - 1):
        dx = waypoints[i + 1][0] - waypoints[i][0]
        dy = waypoints[i + 1][1] - waypoints[i][1]
        thetas.append(np.arctan2(dy, dx))
    thetas.append(thetas[-1])  # Repeat last orientation for the last waypoint

    waypoints_with_theta = [(waypoints[i][0], waypoints[i][1], thetas[i]) for i in range(len(waypoints))]

    return waypoints_with_theta
    
def generate_yaw_from_targets(initial_yaw, targets):
    yaw_of_targets = [initial_yaw]
    for desired_point in range(len(targets) - 2):
        at_point = targets[desired_point]
        next_point = targets[desired_point + 1]
        dx = next_point[0] - at_point[0]
        dy = next_point[1] - at_point[1]
        yaw_of_targets.append(np.arctan2(dy, dx))
    yaw_of_targets.append(initial_yaw)
    print(yaw_of_targets)
    return yaw_of_targets
    
def get_trajectory(targets, interval):
    yaw_of_targets = generate_yaw_from_targets(np.pi/2, targets)
    trajectory = []
    # For testing
    for desired_point in range(len(targets) - 1):
        at_point = targets[desired_point]
        at_point_yaw = yaw_of_targets[desired_point]
        next_point = targets[desired_point + 1]
        next_point_yaw = yaw_of_targets[desired_point + 1]
        temp_trajectory = generate_bezier_waypoints(at_point[0], at_point[1], at_point_yaw, next_point[0], next_point[1], next_point_yaw, offset=0.15, num_points=interval)
        trajectory += temp_trajectory
    return trajectory

    # TSP w/ NEAREST NEIGHBORS !!
def distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return np.linalg.norm(np.array(point1) - np.array(point2))

def nearest_neighbor(current_node, unvisited_nodes):
    """Find the nearest neighbor to the current node from the unvisited nodes."""
    min_distance = float('inf')
    nearest_node = None

    for node in unvisited_nodes:
        dist = distance(current_node, node)
        if dist < min_distance:
            min_distance = dist
            nearest_node = node

    return nearest_node

def nearest_neighbor_tsp(coordinates):
    """Solve the traveling salesperson problem using the nearest neighbor algorithm."""
    start_node = coordinates[0]
    unvisited_nodes = set(coordinates[1:])  # Set of unvisited nodes
    current_node = start_node
    tsp_path = [start_node]

    while unvisited_nodes:
        nearest = nearest_neighbor(current_node, unvisited_nodes)
        tsp_path.append(nearest)
        current_node = nearest
        unvisited_nodes.remove(nearest)

    tsp_path.append(start_node)  # Return to the starting node to complete the cycle

    return tsp_path


if __name__ == '__main__':
    
    targets = [(0.0,0.0), (0.2, 0.2), (0.4, 0.4), (0.6,0.1),(0.0,0.0)]

    tsp_path = nearest_neighbor_tsp(targets)
    print("Nearest Neighbor TSP Path:", tsp_path)

    interval = 50
    # trajectory = get_trajectory(tsp_path, interval)
    trajectory = get_trajectory(targets, interval)
    
    
    plot_trajectory(trajectory, interval)
