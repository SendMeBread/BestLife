import matplotlib.pyplot as plt
def kd_bar():
        data = {'Live':0, 'Die':10}
        live_die = list(data.keys())
        kdr = list(data.values())

        plt.bar(live_die, kdr, color='maroon', width=.5)
        plt.ylabel('Did they live?')
        plt.title('Live or die?')
        plt.show()
kd_bar()