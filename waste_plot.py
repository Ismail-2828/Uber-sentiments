import matplotlib.pyplot as plt

# Time values (assuming equal time intervals)
time = range(0, 21, 2)

# Voltage data
wood_voltage = [0.00, 5.68, 11.36, 17.04, 22.72, 28.40, 34.08, 39.76, 45.44, 51.12, 56.80]
paper_voltage = [0.00, 5.48, 10.96, 16.44, 21.92, 27.40, 32.88, 38.36, 43.84, 49.32, 54.80]
nylon_voltage = [0.00, 5.50, 11.10, 16.56, 22.20, 27.80, 33.14, 38.56, 44.05, 50.23, 55.30]
charging_voltage = [1.0, 1.5, 2.0, 7.3, 9.0, 12.62, 13.32, 13.5, 13.5, 13.5, 13.5]

# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(time, wood_voltage, marker='o', linestyle='-', color='red', label='Wood')
plt.plot(time, paper_voltage, marker='s', linestyle='-', color='blue', label='Paper')
plt.plot(time, nylon_voltage, marker='*', linestyle='-', color='green', label='Nylon')
plt.plot(time, charging_voltage, marker='-', linestyle='-', color='black', label='Charging')

# Adding labels and title
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.title('Voltage vs Time')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
