import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
plt.plot(months, revenue)
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.title("Monthly Revenue Growth")
plt.show()
