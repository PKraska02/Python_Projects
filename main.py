import Window_Screen as Screen
import tkinter as tk
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    width = 1280
    height = 800
    window = tk.Tk()
    #app_screen = Screen.Window_Screen(window, width, height)
    buttons = Screen.Buttons(window,width,height)
    #my_plan = Screen.MyPlanScreen(window,width,height)
    #add_exercise = Screen.AddExercise(window,width,height)
    #statistics = Screen.Statistics(window,width,height)
    window.mainloop()

