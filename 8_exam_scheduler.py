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
        color map={}
        available_colors=set(range(1,len(self.subjects)+1))
        for subject in self.subjects:
            used colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color map:
                    