import csv

# Define the field names
field_names = ['vech_lane1', 'vech_lane2', 'vech_lane3', 'vech_lane4', 'lane1_timer', 'lane2_timer', 'lane3_timer', 'lane4_timer']

# Specify the filename
file_name = 'traffic_data.csv'

# Dummy data
data = [
    {'vech_lane1': 'Car', 'vech_lane2': 'Bus', 'vech_lane3': 'Bicycle', 'vech_lane4': 'Motorcycle', 'lane1_timer': 10, 'lane2_timer': 15, 'lane3_timer': 8, 'lane4_timer': 12},
    {'vech_lane1': 'Truck', 'vech_lane2': 'Motorcycle', 'vech_lane3': 'Car', 'vech_lane4': 'Bicycle', 'lane1_timer': 12, 'lane2_timer': 8, 'lane3_timer': 10, 'lane4_timer': 15},
    {'vech_lane1': 'Bicycle', 'vech_lane2': 'Car', 'vech_lane3': 'Motorcycle', 'vech_lane4': 'Bus', 'lane1_timer': 8, 'lane2_timer': 10, 'lane3_timer': 12, 'lane4_timer': 15},
    # Add more rows as needed
]

# Write the header and dummy data to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    
    # Write the header row
    writer.writeheader()

    # Write the dummy data
    writer.writerows(data)

print(f'CSV file "{file_name}" has been created with dummy data.')
