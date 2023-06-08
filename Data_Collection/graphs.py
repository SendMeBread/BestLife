import matplotlib.pyplot as plt
data = {'Live':0, 'Die':10}
live_die = list(data.keys())
kdr = list(data.values())
fig = plt.figure(figsize=(10,5))
plt.bar(live_die, kdr, color='maroon', width=.5)
plt.ylabel('Did they live?')
plt.title('Live or die?')
plt.show()