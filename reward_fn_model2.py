def reward_function(params):
    # print("-------------- progress :: " + params['progress'])
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    absolute_steering_angle = abs(params['steering_angle']) 

    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    SPEED_THRESHOLD = 1

    marker_1 = 0.1 * track_width
    marker_2 = 0.20 * track_width
    marker_3 = 0.30 * track_width
    marker_4 = 0.40 * track_width
    marker_5 = 0.5 * track_width

    if all_wheels_on_track:
        if distance_from_center <= marker_1:
            reward = 3.0
        elif distance_from_center <= marker_2:
            reward = 2.5
        elif distance_from_center <= marker_3:
            reward = 1.5
        elif distance_from_center <= marker_4:
            reward = 1
        elif distance_from_center <= marker_5:
            reward = 0.5
        else:
            reward = 1e-3 # crashed
    else:
        reward = -1  #off track
        
    if speed < SPEED_THRESHOLD:
        reward = reward + 0.5
    else:
        reward = reward + 1.0
        
    ABSOLUTE_STEERING_ANGLE_THRESHOLD = 15 

    # if car is steering too much - penalize
    if absolute_steering_angle > ABSOLUTE_STEERING_ANGLE_THRESHOLD:
        reward *= 0.8
        
    # Reward for going faster when car is not turning
    if absolute_steering_angle < ABSOLUTE_STEERING_ANGLE_THRESHOLD and speed > SPEED_THRESHOLD:
        reward = reward + speed/4
        
    return float(reward)
