''' This file has all the functions '''
import matplotlib.pyplot as plt


def bar_plot(bar_plot_data: dict, xlabel: str, ylabel: str, title: str):
    """Pass dict variable having keys to plot on x-axis and pass values to plot on y-axis"""
    # initialisation
    x_axis_keys = list(bar_plot_data.keys())
    y_axis_values = list(bar_plot_data.values())
    fig = plt.figure()

    # creating the bar plot
    plt.bar(x_axis_keys, y_axis_values)
    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.xticks(x_axis_keys)
    plt.rcParams["figure.figsize"] = (80, 5.5)
    # show plot
    plt.show()


def bar_plot_prj2_1(bar_plot_data: dict, xlabel: str, ylabel: str, title: str):
    """Pass dict variable having keys to plot on x-axis and pass values to plot on y-axis.
    This function has x labels sorting specific to Part 2 of Python Data Prj 2"""
    # initialisation
    x_axis_keys = list(bar_plot_data.keys())
    y_axis_values = list(bar_plot_data.values())
    x_axis_keys2 = [0]*len(x_axis_keys)
    y_axis_values2 = [0]*len(x_axis_keys)

    for index, key in enumerate(x_axis_keys):
        if key == "<= 1L":
            x_axis_keys2[0] = "<= 1L"
            y_axis_values2[0] = y_axis_values[index]
        elif key == "1L to 10L":
            x_axis_keys2[1] = "1L to 10L"
            y_axis_values2[1] = y_axis_values[index]
        elif key == "10L to 1Cr":
            x_axis_keys2[2] = "10L to 1Cr"
            y_axis_values2[2] = y_axis_values[index]
        elif key == "1Cr to 10Cr":
            x_axis_keys2[3] = "1Cr to 10Cr"
            y_axis_values2[3] = y_axis_values[index]
        else:
            x_axis_keys2[4] = "> 10Cr"
            y_axis_values2[4] = y_axis_values[index]

    fig = plt.figure()

    # creating the bar plot
    plt.bar(x_axis_keys2, y_axis_values2)
    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.xticks(x_axis_keys)

    # show plot
    plt.show()


def bar_plot_prj_2_3(bar_xaxis: list, bar_yaxis: list, xlabel: str, ylabel: str, title: str):
    """Pass dict variable having keys to plot on x-axis and pass values to plot on y-axis"""
    # initialisation
    fig = plt.figure()

    # creating the bar plot
    plt.bar(bar_xaxis, bar_yaxis)
    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    # show plot
    plt.show()


def bar_group_plot(top_business_activity: dict, registration_yearwise: dict,
                   xlabel: str, ylabel: str, title: str):
    '''Pass dict variable'''
    # initialisation
    y_values_activity = top_business_activity.values()
    y_values_registration = registration_yearwise.values()

    fig = plt.figure()
    width = 0.2
    x_values = []
    for i in range(12, 17):
        x_values.append(i)
    x_values2 = []
    for i in range(1, 11):
        x_values2.append(i)
    # creating the bar plot
    plt.bar(x_values, y_values_activity, width)
    plt.bar(x_values2, y_values_registration, width)

    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(top_business_activity.keys())
    plt.tight_layout()
    plt.xticks(x_values, registration_yearwise.keys)
