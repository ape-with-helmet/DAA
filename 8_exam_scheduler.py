#design an application for the university to schedule an exam. Given a list of different subjects and students who are enrolled in many subjhects, many subjects would have common students of the same batch, some backlogged students etc.
#Find the solutions to the following:
#a. Obtain the schedule for the exam so that no two exams with a common student are scheduled at the same time.
#b. How many minimum slots are needed to schedule all exams

from collections import defaultdict
class Graph:
    def __init__(self,subjects):
        self.subjects=subjects
        self.graph=defaultdict(list)
    def add_edge(self,subject1,subject2):
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)
    def graph_coloring(self):
        color_map={}
        available_colors=set(range(1,len(self.subjects)+1))
        for subject in self.subjects:
            used_colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])
                available_color=available_colors-used_colors
                if available_color:
                    color_map[subject]=min(available_color)
                else:
                    color_map[subject]=len(available_colors)+1
                    available_colors.add(color_map[subject])
        return color_map
    def get_minimum_time_slots(self):
        color_map=self.graph_coloring()
        return max(color_map.values())

#Example usage
subjects=['math','phy','chem','bio']
students = {
    'math':['alice','bob','charlie'],
    'phy':['alice','charlie','david'],
    'chem':['bob','charlie','eve'],
    'bio':['alice','david','eve']
}
graph=Graph(subjects)
graph.add_edge('math','phy')
graph.add_edge('math','chem')
graph.add_edge('phy','chem')
graph.add_edge('phy','bio')
minimum_time_slots=graph.get_minimum_time_slots()
print(f"Minimum time slots needed: {minimum_time_slots}")