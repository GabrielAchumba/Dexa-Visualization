import matplotlib.pyplot as plt

series1 = [
        0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            794.95,
            2718.7,
            2718.7,
            2718.7,
            2690.9,
            629.97,
            6.4994,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]

series2 = [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1132.8125,
        2718.75,
        2718.75,
        2718.75,
        2572.604221116478,
        609.7588554922129,
        35.545295686143994,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
        ]


x_values_series1 = [i * 360 for i in range(len(series1))]
x_values_series2 = [i * 360 for i in range(len(series2))]

#series2 = [value / 1000 for value in  series2]

plt.figure(figsize=(10, 5))
plt.plot(x_values_series1, series1, label="HFPT")
plt.plot(x_values_series2, series2, label="Dexa")

plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)