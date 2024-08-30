# ------------------------------------------------------------------------------------------------------------------------

# import serial
# import pandas as pd
# import time

# # Set up the serial connection
# ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's COM port

# # Create a DataFrame to store the data
# data = []

# # Collect data for 2 seconds
# start_time = time.time()
# while time.time() - start_time <= 2:
#     if ser.in_waiting:
#         line = ser.readline().decode('utf-8').strip()  # Read the line from the serial port
#         print(line)  # Print the line (for debugging)
#         time_elapsed, sensor_value = line.split(",")  # Split the CSV string into two values
#         data.append([time_elapsed, sensor_value])

# # Close the serial connection
# ser.close()

# # Create a DataFrame and save it to Excel
# df = pd.DataFrame(data, columns=["Time (ms)", "Sensor Value"])
# df.to_excel("sensor_data.xlsx", index=False)  # Save the DataFrame to an Excel file

# --------------------------------------------------------------------------------------------------------------------

# continous data tracking
# import serial
# import pandas as pd
# import time

# # Set up the serial connection
# ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's COM port

# # Create a DataFrame to store the data
# data = []

# try:
#     print("Starting data collection. Press Ctrl+C to stop.")
#     while True:  # Run indefinitely
#         if ser.in_waiting:
#             line = ser.readline().decode('utf-8').strip()  # Read the line from the serial port
#             print(f"Raw data: '{line}'")  # Print the raw line for debugging

#             # Ensure the line contains data in the expected format
#             if ',' in line:
#                 try:
#                     # Split the CSV string into two values
#                     time_elapsed, sensor_value = line.split(",")
#                     data.append([time_elapsed, sensor_value])
#                 except ValueError as e:
#                     print(f"ValueError: {e} - Line: '{line}'")  # Print error and problematic line
#             else:
#                 print(f"Line does not contain a comma: '{line}'")

#         # Optional: Sleep for a short period to reduce CPU usage
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle stopping the script with Ctrl+C
#     print("Data collection stopped.")

# finally:
#     # Close the serial connection and save data
#     ser.close()

#     # Create a DataFrame and save it to Excel
#     df = pd.DataFrame(data, columns=["Time (ms)", "Sensor Value"])
#     df.to_excel("sensor_data.xlsx", index=False)  # Save the DataFrame to an Excel file
#     print(df)
#     print("Data saved to sensor_data.xlsx")

# -------------------------------------------------------------------------------------------------

# get all values without plotting

# import serial
# import pandas as pd
# import time

# # Set up the serial connection
# ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's COM port

# # Create a DataFrame to store the data
# data = []

# # Record the start time
# start_time = time.time()

# try:
#     print("Starting data collection for 4 seconds. Press Ctrl+C to stop.")
#     while True:  # Run indefinitely until stopped manually
#         if time.time() - start_time > 4:  # Check if 4 seconds have passed
#             break  # Exit the loop after 4 seconds

#         if ser.in_waiting:
#             line = ser.readline().decode('utf-8').strip()  # Read the line from the serial port
#             print(f"Raw data: '{line}'")  # Print the raw line for debugging

#             # Ensure the line contains data in the expected format
#             if ',' in line:
#                 try:
#                     # Split the CSV string into two values
#                     time_elapsed, sensor_value = line.split(",")
#                     data.append([time_elapsed, sensor_value])
#                 except ValueError as e:
#                     print(f"ValueError: {e} - Line: '{line}'")  # Print error and problematic line
#             else:
#                 print(f"Line does not contain a comma: '{line}'")

#         # Optional: Sleep for a short period to reduce CPU usage
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle stopping the script with Ctrl+C
#     print("Data collection stopped.")

# finally:
#     # Close the serial connection and save data
#     ser.close()

#     # Create a DataFrame and save it to Excel
#     df = pd.DataFrame(data, columns=["Time (ms)", "Sensor Value"])
#     df.to_excel("sensor_data.xlsx", index=False)  # Save the DataFrame to an Excel file
#     print(df)
#     print("Data saved to sensor_data.xlsx")

# plot the data into graph

import serial
import pandas as pd
import time
import matplotlib.pyplot as plt

# Set up the serial connection
ser = serial.Serial('COM4', 57600)  # Replace 'COM3' with your Arduino's COM port

# Create a DataFrame to store the data
data = []

# Record the start time
start_time = time.time()

try:
    print("Starting data collection for 4 seconds. Press Ctrl+C to stop.")
    while True:  # Run indefinitely until stopped manually
        if time.time() - start_time > 4:  # Check if 4 seconds have passed
            break  # Exit the loop after 4 seconds

        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()  # Read the line from the serial port
            print(f"Raw data: '{line}'")  # Print the raw line for debugging

            # Ensure the line contains data in the expected format
            if ',' in line:
                try:
                    # Split the CSV string into two values
                    time_elapsed, sensor_value = line.split(",")
                    data.append([float(time_elapsed), float(sensor_value)])
                except ValueError as e:
                    print(f"ValueError: {e} - Line: '{line}'")  # Print error and problematic line
            else:
                print(f"Line does not contain a comma: '{line}'")

        # Optional: Sleep for a short period to reduce CPU usage
        # time.sleep(0.01)

except KeyboardInterrupt:
    # Handle stopping the script with Ctrl+C
    print("Data collection stopped.")

finally:
    # Close the serial connection and save data
    ser.close()

    # Create a DataFrame and save it to Excel
    df = pd.DataFrame(data, columns=["Time (ms)", "Sensor Value"])
    df.to_excel("sensor_data.xlsx", index=False)  # Save the DataFrame to an Excel file
    print(df)
    print("Data saved to sensor_data.xlsx")

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df["Time (ms)"], df["Sensor Value"], marker='o', linestyle='-', color='b')
    plt.title("Sensor Data Over Time")
    plt.xlabel("Time (ms)")
    plt.ylabel("Sensor Value")
    plt.ylim(max(df["Sensor Value"])-10, max(df["Sensor Value"])+5)  # Set y-axis to start from 300
    plt.grid(True)
    plt.savefig("sensor_data_plot.png")  # Save the plot as a PNG file
    plt.show()  # Display the plot
