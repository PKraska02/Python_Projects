import pandas as pd
import datetime as dat

class Exercise:
    def __init__(self,date,day_number, exercise_name, series_value, repetitions, weights):
        #if not isinstance(date, dat.datetime):
        #    raise ValueError("Date must be a datetime.datetime object")
        #else:
        self.date = date
        self.day_number = day_number
        self.exercise_name = exercise_name
        self.series_value = series_value
        self.repetitions = repetitions
        self.weights = weights


class Training_Plan:
    def __init__(self):
        self.trainings = []

    def add_exercise(self, exercise):
        self.trainings.append(exercise)

    def create_training_dataframe(self):
        data = {
            "Date": [],
            "Training day" : [],
            "Exercise name": [],
            "SeriesValue": [],
            "Number of repetitions": [],
            "Weight for each repetition": []
        }
        return data

    def add_to_dataframe(self, data):
        for training in self.trainings:
            data["Date"].append(training.date)
            data["Training day"].append(training.day_number)
            data["Exercise name"].append(training.exercise_name)
            data["SeriesValue"].append(training.series_value)
            data["Number of repetitions"].append(training.repetitions)
            data["Weight for each repetition"].append(training.weights)

        df = pd.DataFrame(data)
        df.set_index("Date", inplace=True)
        return df

    def save_data_csv(self, filename="My_Plan.csv"):
        try:
            df = self.add_to_dataframe(self.create_training_dataframe())
            df.to_csv(filename, index=False)
        except FileNotFoundError:
            print(f"Plik {filename} nie istnieje.")
            return None

    def load_from_csv(self, filename="My_Plan.csv"):
        try:
            df = pd.read_csv(filename)
            return df
        except FileNotFoundError:
            print(f"Plik {filename} nie istnieje.")
            return None

