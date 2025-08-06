import pandas as pd
import matplotlib.pyplot as plt

class DataTracker:
    def __init__(self, name, data_points):
        self.name = name
        self.data_points = data_points

    def add_data_point(self, date, value):
        self.data_points.append({'date': date, 'value': value})

    def visualize(self):
        df = pd.DataFrame(self.data_points)
        df['date'] = pd.to_datetime(df['date'])
        plt.figure(figsize=(10, 5))
        plt.plot(df['date'], df['value'], marker='o')
        plt.title(self.name)
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.grid(True)
        plt.show()

class MinimalistDataVisualizationTracker:
    def __init__(self):
        self.trackers = []

    def create_tracker(self, name):
        tracker = DataTracker(name, [])
        self.trackers.append(tracker)
        return tracker

    def visualize_all(self):
        for tracker in self.trackers:
            tracker.visualize()

tracker_app = MinimalistDataVisualizationTracker()

# example usage
sleep_tracker = tracker_app.create_tracker('Sleep Quality')
sleep_tracker.add_data_point('2022-01-01', 8)
sleep_tracker.add_data_point('2022-01-02', 7)
sleep_tracker.add_data_point('2022-01-03', 9)

exercise_tracker = tracker_app.create_tracker('Daily Exercise')
exercise_tracker.add_data_point('2022-01-01', 30)
exercise_tracker.add_data_point('2022-01-02', 20)
exercise_tracker.add_data_point('2022-01-03', 45)

tracker_app.visualize_all()