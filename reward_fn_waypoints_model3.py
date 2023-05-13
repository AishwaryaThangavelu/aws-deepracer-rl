def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]

    #racing line
    left_lane = [40,41,42,43,44,45,91,92]
    center_lane = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,30,31,32,33,34,35,36,37,38,39,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,85,86,87,88,89,90]#Fill in the waypoints
    right_lane = [25,26,27,28,29,76,77,78,79,80,81,82,83,93,94,95,96,97,98,99,100,101]

    #Speed
    fast = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,30,31,32,33,34,35,36,37, 25,26,27,28,29,30,31,32,51,52,53,54,61,62,63,64,65,66,67,68,69,70, 46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,85,86,87,88,89,90] #3
    moderate = [25,26,27,28,29,38,39,40,41,42,76,77,78,79,80,95,96,97,98,99,100,101] #2
    slow = [22,23,24,43,44,45,81,82,83,93,94] #1

    reward = 40

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in fast:
        if params["speed"] > 1.5 :
            reward += 10
        else:
            reward -= 10

    elif params["closest_waypoints"][1] in moderate:
        if params["speed"] > 1 and params["speed"] <= 1.5 :
            reward += 10
        else:
            reward -= 10

    elif params["closest_waypoints"][1] in slow:
        if params["speed"] <= 1 :
            reward += 10
        else:
            reward -= 10

    return float(reward)