import matplotlib.pyplot as plt

def get_user_input():
    x_input = input("Enter 4 digits for X separated by space: ")
    y_input = input("Enter 4 digits for Y separated by space: ")

    x_values = [float(x) for x in x_input.split()]
    y_values = [float(y) for y in y_input.split()]

    return x_values, y_values

def plot_xy(x_values, y_values):
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of X against Y')
    plt.show()


user_x_values, user_y_values = get_user_input()

plot_xy(user_x_values, user_y_values)
