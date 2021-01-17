from tkinter import *

# ------------ COLOR THEMES ------------ #
BLACK = "#222831"
YELLOW = "#FFD369"
GREY = "#393E46"
WHITE = "#EEEEEE"
FONT = 'Courier'
PADX = (10, 10)
PADY = (20, 20)

# ----------- Main Windows/Functionality ----------- # 
class MainWindow:

    def __init__(self, window):
        # main window set up. 
        self.window = window
        window.title('FitBit')
        window.config(padx=50, pady=20, bg=BLACK)
        # insert title image via canvas
        self.canvas = Canvas(width=270, height=100,
                             bg=BLACK, highlightthickness=0)
        # background photo for title 
        self.photo = PhotoImage(file="./main_title.png")
        self.image = self.photo  # prevent garbage collection of image
        self.canvas.create_image(135, 50, image=self.image)
        self.canvas.grid(column=1, row=0, padx=PADX, pady=(10, 50))

        # workout label
        self.workout_label = Label(text="WORKOUT", font=(
            FONT, 20, "normal"), fg=YELLOW, bg=BLACK)
        self.workout_label.grid(column=0, row=1, padx=PADX, pady=PADY)

        # entry box
        self.workout_entry = Entry(width=40, fg=YELLOW, bg=GREY)
        self.workout_entry.grid(column=1, row=1, padx=PADX, pady=PADY)

        # time label
        self.time_label = Label(text="SECONDS", font=(
            FONT, 20, "normal"), fg=YELLOW, bg=BLACK)
        self.time_label.grid(column=0, row=2, padx=PADX, pady=PADY)

        # time listbox, user can select # seconds to workout
        self.time_listbox = Listbox(
            height=4, fg=YELLOW, bg=GREY, selectbackground=BLACK)
        self.seconds = ["10", "20", "30", "60"]
        # insert seconds into listbox
        for item in self.seconds:
            self.time_listbox.insert(self.seconds.index(item), item)

        # bind listbox selection with function
        self.time_listbox.grid(column=1, row=2)
        self.workout_add = Button(
            text='Add', fg=GREY, width=20, bg=GREY, command=self.create_routine)
        self.workout_add.grid(column=0, row=3, padx=PADX, pady=PADY)
        self.workout_clear = Button(
            text='Clear All', fg=GREY, width=20, bg=GREY)
        self.workout_clear.grid(column=2, row=3, padx=PADX, pady=PADY)

        # routine display 
        self.routine = Label(text="ROUTINE", font=(
            FONT, 30, "normal"), fg=YELLOW, bg=BLACK)
        self.routine.grid(column=1, row=4, padx=PADX, pady=PADY)
        self.start_routine = Button(
            text='Start', fg=GREY, width=20, bg=GREY, command=self.open_timer)
        self.start_routine.grid(column=1, row=3, padx=PADX, pady=PADY)
        self.start_row = 4
        # save routine sets into list in order to call on later for timer
        self.routine_list = []

    def create_routine(self):
        #Generates routine in format of rows at bottom of window via "add" button 
        self.start_row += 1
        self.work_text = self.workout_entry.get()
        self.new_routine = Label(text=self.work_text.upper(), font=(
            FONT, 20, "normal"), fg=WHITE, bg=BLACK)
        self.new_routine.grid(column=0, row=self.start_row)
        self.sec = self.time_listbox.get(self.time_listbox.curselection())
        self.sec_set = Label(text=f"{self.sec} SECS", font=(
            FONT, 20, "normal"), fg=WHITE, bg=BLACK)
        self.sec_set.grid(column=2, row=self.start_row)
        self.routine_list.append((self.work_text, int(self.sec)))
        print(self.routine_list)
        self.workout_entry.delete(0, END)

    def open_timer(self):
        # launches timer window when "start" button hit
        self.newWindow = Toplevel(self.window)
        self.app = Timer(self.newWindow, self.routine_list)



class Timer(MainWindow):

    def __init__(self, root, routine_list):
        # display of timer/stop watch window 
        self.root = root
        self.routine_list = routine_list
        root.title('TIMER')
        root.config(bg=YELLOW, height=500, width=500, padx=20, pady=20)
        self.canvas = Canvas(self.root, width=400, height=400,
                             bg=YELLOW, highlightthickness=0)
        self.photo = PhotoImage(file="./stopwatch.png")
        self.image = self.photo  # prevent garbage collection of image
        self.canvas.create_image(200, 200, image=self.image)
        self.canvas.grid(column=1, row=1)
        self.title = Label(root, text="TIMER", font=(
            FONT, 40, 'normal'), fg=GREY, bg=YELLOW)
        self.title.grid(column=1, row=0, pady=(20, 20))
        self.timer = Label(root, text="00", font=(
            FONT, 60, 'normal'), bg=YELLOW, fg=GREY)
        self.timer.grid(column=1, row=1, pady=(210, 0))
        self.start = Button(root, text="START", fg=GREY,
                            width=10, height=5, bg=BLACK, command=self.start_timer)
        self.start.grid(column=0, row=2, pady=(10, 10))
        self.end = Button(root, text="END",fg=GREY,
                            width=10, height=5, bg=BLACK, command=self.end_timer)
        self.end.grid(column=3, row=2, pady=(10, 10))
    

    def start_timer(self):
        # "start" button begins timer 
        for routine in res:
            # extract values from tuple
            workout = routine[0]
            count = routine[1]
            self.title.config(text=workout)
            # send time to count_down for interactive timer
            self.count_down(count)

                        
    def count_down(self, count):
        # refreshes window every 1 second, decreases count by 1.  
        if count > 0:
            self.root.after(1000, self.count_down, count - 1)
            self.timer.config(text=count)
            

    def end_timer(self):
        # reset timer
        self.timer.config(text='00')
        self.title.config(text='TIMER')
            
        

        
