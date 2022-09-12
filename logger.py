import matplotlib.pyplot as plt

class Logger:

    def __init__(self):
        self.values = []

    def log(self, value):
        self.values.append(value)

    def show(self):
        plt.plot(range(len(self.values)), self.values)
        plt.xlabel('time')
        plt.ylabel('value')
        plt.title('title')
        plt.show()
