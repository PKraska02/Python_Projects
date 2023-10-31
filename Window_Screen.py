import tkinter as tk
from tkinter import simpledialog
import Gym_Planner_DB as gym_db


# import datetime as dat
class Buttons:
    def __init__(self, window, width, height):
        self.window = window
        self.app_screen = Window_Screen(window, width, height)
        self.my_plan = MyPlanScreen(window, width, height)
        self.add_exercises = AddExercise(window, width, height)
        self.statistics = Statistics(window, width, height)
        self.app_screen.__init__(window,width,height)
        ###############################################################################
        # WINDOW_SCREEN BUTTONS
        ###############################################################################
        # Label Settings
        self.label = tk.Label(window, text="Gym Planner", bg="Black", fg="White", font=("Arial", 64))
        self.label.grid(row=0, column=5, columnspan=4, sticky="nsew")
        ###############################################################################
        # MAIN BUTTONS
        ###############################################################################
        # Plan_Button Settings
        self.plan_button = tk.Button(window, text="My Plan", command=self.Show_MyPlan, bg="Gray",
                                     font=("Arial", 16))
        self.plan_button.grid(row=3, column=1, columnspan=4, sticky="nsew")

        # Add_Train_Session Settings
        self.add_exercise = tk.Button(window, text="Add Exercise", command=self.Show_AddExercises,
                                      bg="Gray",
                                      font=("Arial", 16))
        self.add_exercise.grid(row=3, column=6, columnspan=2, sticky="nsew")

        ###############################################################################
        # Statistics_Button
        ###############################################################################
        self.stats_button = tk.Button(window, text="Your Training Statistics", command=self.statistics.Show_Statistics,
                                      bg="Gray",
                                      font=("Arial", 16))
        self.stats_button.grid(row=3, column=10, columnspan=3, sticky="nsew")
        ###############################################################################
        # MY_PLAN_SCREEN BUTTONS
        ###############################################################################
        # Back_button Settings
        self.back_button = tk.Button(window, text="Back", command=self.Hide_MyPlan, bg="Gray", font=("Arial", 16))
        #self.back_button.grid(row=6, column=2, columnspan=3, sticky="nsew")

        # Add_Plan_Button Settings
        self.add_plan_button = tk.Button(window, text="Add Plan", command=self.my_plan.Add_Plan, bg="Gray",
                                         font=("Arial", 16))
        # Save Button
        self.save_button = tk.Button(window, text="Save", command=self.add_exercises.Save_Train_Session, bg="Gray",
                                     font=("Arial", 16))
        ###############################################################################
        ###############################################################################
        # ADD_EXERCISE BUTTONS
        ###############################################################################
        # Back_button Settings
        self.back_button2 = tk.Button(window, text="Back", command=self.Hide_AddExercises, bg="Gray",
                                      font=("Arial", 16))
        #self.back_button2.grid(row=6, column=2, columnspan=3, sticky="nsew")


    ###############################################################################
    # WINDOW SCREEN BUTTONS MANAGEMENT
    ###############################################################################
    def Show_Window(self):
        self.label.grid(row=0, column=5, columnspan=4, sticky="nsew")
        self.plan_button.grid(row=3, column=1, columnspan=4, sticky="nsew")
        self.add_exercise.grid(row=3, column=6, columnspan=2, sticky="nsew")
        self.stats_button.grid(row=3, column=10, columnspan=3, sticky="nsew")

    def Hide_Window(self):
        self.label.grid_remove()
        self.plan_button.grid_remove()
        self.add_exercise.grid_remove()
        self.stats_button.grid_remove()

    ###############################################################################
    # MY PLAN BUTTONS MANAGEMENT
    ###############################################################################
    def Show_MyPlan(self):
        self.Hide_Window()
        self.my_plan.Show_Plan(self.back_button)

    def Hide_MyPlan(self):
        self.my_plan.Hide_Plan(self.back_button)
        self.Show_Window()

    ###############################################################################
    # ADD EXERCISE BUTTONS MANAGEMENT
    ###############################################################################
    def Show_AddExercises(self):
        self.Hide_Window()
        self.add_exercises.show_add_train_session(self.back_button2,self.save_button)

    def Hide_AddExercises(self):
        self.add_exercises.hide_add_train_session(self.back_button2,self.save_button)
        self.Show_Window()

    ###############################################################################
    # STATISTICS BUTTONS MANAGEMENT
    ###############################################################################


class Window_Screen:
    def __init__(self, window, width, height):
        # Window Settings
        self.window = window
        self.window.title("Gym Planner")
        # Rows and columns flex config
        for i in range(8):  # for rows 0-7
            window.rowconfigure(i, weight=1)
        for i in range(14):  # For column 0-13
            window.columnconfigure(i, weight=1)
        self.window.geometry(f"{width}x{height}")
        self.window.configure(bg="red")

    ###################################################################################
    # My Plan
    ###################################################################################


class MyPlanScreen:
    def __init__(self, window, width, height):
        self.window = window
        # Plan Instance
        self.plan = gym_db.Training_Plan()
        # Exercise List
        self.exercise_list = tk.Listbox(window)

    def Show_Plan(self, button):
        button.grid(row=6, column=2, columnspan=3, sticky="nsew")
        self.exercise_list.delete(0, tk.END)
        exercises = self.plan.create_training_dataframe()
        unique_exercises = exercises["Training day"]

        # Dodaj ćwiczenia do listy
        for exercise in unique_exercises:
            self.exercise_list.insert(tk.END, exercise)

        # Wyświetl listę ćwiczeń
        self.exercise_list.grid(row=3, column=7, columnspan=3, sticky="nsew")

    def Hide_Plan(self, button):
        self.exercise_list.grid_remove()
        button.grid_remove()

    def Read_Plan(self, button):
        # Wczytaj zawartość planu treningowego z pliku tekstowego
        try:
            with open("Training_Plan.txt", "r") as file:
                plan_content = file.read().lower()
        except FileNotFoundError:
            plan_content = "File with training plan does not exist!."

        button.plan_text.delete("1.0", tk.END)

        # Show Plan
        button.plan_text.insert(tk.END, plan_content)

    def Add_Plan(self):
        pass

    ##############################################################################################################
    # Add Exercise
    ##############################################################################################################


class AddExercise:
    def __init__(self, window, width, height):
        self.window = window
        # Plan Instance
        self.plan = gym_db.Training_Plan()

    def show_add_train_session(self,button,button2):
        # Read new data
        button.grid(row=6, column=2, columnspan=3, sticky="nsew")
        date = simpledialog.askstring("Data", "Podaj datę (RRRR-MM-DD):")
        day = simpledialog.askinteger("Dzień", "Podaj dzień treningu (1-7):")
        exercise_name = simpledialog.askstring("Ćwiczenie", "Podaj nazwę ćwiczenia:")
        series_value = simpledialog.askinteger("Seria", "Podaj liczbę serii:")
        repetition_value = simpledialog.askstring("Powtorzenia", "Podaj liczbe powtorzen(odzielone przecinkiem")
        weights = simpledialog.askstring("Ciężary", "Podaj ciężary (oddzielone przecinkiem):")

        # Add to Database
        new_exercise = gym_db.Exercise(date, day, exercise_name, series_value, repetition_value, weights)
        self.plan.add_exercise(new_exercise)
        new_df = self.plan.create_training_dataframe()
        update_df = self.plan.add_to_dataframe(new_df)
        button2.grid(row=4, column=2, columnspan=3, sticky="nsew")
        # Wyświetl dane sesji treningowej
        print("Data:", date)
        print("Dzień:", day)
        print("Ćwiczenie:", exercise_name)
        print("Liczba serii:", series_value)
        print("Liczba powtorzen", repetition_value)
        print("Ciężary:", weights)
        print(update_df)

    def hide_add_train_session(self, button,save_button2):
        button.grid_remove()
        save_button2.grid_remove()

    def Save_Train_Session(self):
        self.plan.save_data_csv()

    #################################################################################################################
    # Statistics
    #################################################################################################################


class Statistics:
    def __init__(self, window, width, height):
        pass

    def Show_Statistics(self):
        pass
