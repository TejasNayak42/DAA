from collections import defaultdict
class Graph:
    def __init__(self, subjects):
        self.subjects = subjects
        self.graph = defaultdict(list)

    def add_edge(self, subject1, subject2):
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)

    def graph_coloring(self):
        color_map = {}
        available_colors = set(range(1, len(self.subjects) + 1))
        for subject in self.subjects:
            used_colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])
            available_color = available_colors - used_colors
            if available_color:
                color_map[subject] = min(available_color)
            else:
                # If no available color, assign a new color
                color_map[subject] = len(available_colors) + 1
                available_colors.add(color_map[subject])
        return color_map

    def get_minimum_time_slots(self):
        color_map = self.graph_coloring()
        return max(color_map.values())


def main():
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = []
    students = {}

    for i in range(num_subjects):
        subject = input(f"Enter subject {i + 1}: ")
        subjects.append(subject)
        num_students = int(input(f"Enter the number of students for {subject}: "))
        student_list = []
        for j in range(num_students):
            student = input(f"Enter student {j + 1} for {subject}: ")
            student_list.append(student)
        students[subject] = student_list

    graph = Graph(subjects)

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        edge = input("Enter edge (subject1 subject2): ").split()
        graph.add_edge(edge[0], edge[1])

    minimum_time_slots = graph.get_minimum_time_slots()
    print(f"Minimum time slots needed: {minimum_time_slots}")

if __name__ == "__main__":
    main()
