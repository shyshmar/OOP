class Graph:
    LIMIT_Y = [i for i in range(10)]

    def set_data(self, data):
        self.data = data

    def draw(self):
        return [i for i in self.data if i in self.LIMIT_Y]


graph1 = Graph()
graph1.set_data([i for i in range(-10, 20)])
graph1.draw()
