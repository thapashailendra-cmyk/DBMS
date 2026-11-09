import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [70, 85, 60, 90, 75]

plt.plot(days, Scores)
plt.show()

plt.plot(days,scores)
plt.title('My Quiz Score Tracker')
plt.xlabel('Days of the Week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0,100)
plt.show()

plt.plot(days,Scores, color='blue', marker='o', linestyle='dashed', linewidth=2)
plt.title('My Quiz Score Tracker')
plt.xlabel('Days of the Week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0,100)
plt.show()

plt.bar(days, Scores, color = 'orange')
plt.title('My Quiz Score Bar Chart')
plt.xlabel('Day of the Week')
plt.ylabel('Score')
plt.ylim(0,100)
plt.show()