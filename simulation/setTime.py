
# Assuming you have two variables for vehicle counts in two lanes
lane1_vehicle_count = 75  # Replace with your actual counts
lane2_vehicle_count = 80  # Replace with your actual counts

# Determine the highest vehicle count
highest_vehicle_count = max(lane1_vehicle_count, lane2_vehicle_count)

# Set the default timer duration
timer_duration = 30  # Default duration for green light

# Check the conditions for updating the timer duration
if 60 < highest_vehicle_count < 100:
    timer_duration = 60
elif highest_vehicle_count >= 100:
    timer_duration = 60

# Print the selected timer duration
print(f"Set traffic light to green for {timer_duration} seconds")
# Code to control traffic light for timer_duration seconds goes here
