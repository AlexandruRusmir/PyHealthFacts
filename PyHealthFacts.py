import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class MainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        self.listing ={}

        for p in (WelcomePage, BMICalculator, RMRCalculator, MinimalWater):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.listing[page_name] = frame

        self.up_frame("WelcomePage")

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()



class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self["bg"] = '#e95c20'
        self.controller.title("PyHealthFacts")
        self.controller.geometry("850x480")
        self.controller.columnconfigure(index=0, weight=1)
        self.controller.columnconfigure(index=1, weight=1)
        self.controller.columnconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=0, weight=1)
        self.controller.rowconfigure(index=1, weight=1)
        self.controller.rowconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=3, weight=1)
        self.controller.resizable(False,False)
        self.controller.configure(bg='#e95c20')
        s = ttk.Style()
        s.configure('TFrame', background='#e95c20')

        widgets_frame = ttk.Frame(self, padding=(0,0, 0, 0))
        widgets_frame.grid(row=1, column=1, padx=0, pady=(10,40), sticky="nsew")
        widgets_frame.columnconfigure(index=0, weight=1)
        widgets_frame.columnconfigure(index=1, weight=1)

        title = ttk.Label(widgets_frame, text="Welcome to PyHealthFacts!",font="rockwell 24 bold",foreground="#011936", background="#e95c20")
        title.grid(row=0, column=0, pady=50, columnspan=2)

        button_bmi = tk.Button(widgets_frame, text="Body Mass Index", bg="#9ED9CC", font="rockwell 12 bold", padx=30, pady=5, fg="#011936", width = 21,
                              command = lambda: controller.up_frame("BMICalculator"))
        button_bmi.grid(row=1, column=0, padx=300, pady=20, columnspan=2)

        button_rmr = tk.Button(widgets_frame, text="Resting Metabolic Rate", bg="#9ED9CC", font="rockwell 12 bold", padx=30, pady=5, fg="#011936", width = 21,
                                command = lambda: controller.up_frame("RMRCalculator"))
        button_rmr.grid(row=2, column=0, padx=300, pady=20, columnspan=2)

        button_water = tk.Button(widgets_frame, text="Minimal water consumption", bg="#9ED9CC", font="rockwell 12 bold", padx=30, pady=5, fg="#011936", width = 21,
                                command = lambda: controller.up_frame("MinimalWater"))
        button_water.grid(row=3, column=0, padx=300, pady=20, columnspan=2)
        
        label_img = tk.Label(widgets_frame, bg="#e95c20")
        label_img.grid(row=4, column=0, columnspan=2)

class BMICalculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = '#e95c20'
        self.parent = parent
        self.controller = controller
        self.controller.title("PyHealthFacts")
        self.controller.option_add("*tearOff", False)
        self.controller.geometry("850x480")
        self.controller.columnconfigure(index=0, weight=1)
        self.controller.columnconfigure(index=1, weight=1)
        self.controller.columnconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=0, weight=1)
        self.controller.rowconfigure(index=1, weight=1)
        self.controller.rowconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=3, weight=1)
        self.controller.resizable(False,False)
        self.controller.configure(bg='#e95c20')

        s = ttk.Style()
        s.configure('TFrame', background='#e95c20')

        widgets_frame = ttk.Frame(self, padding=(0,0, 0, 0))
        widgets_frame.grid(row=1, column=1, padx=0, pady=(10,40), sticky="nsew")
        widgets_frame.columnconfigure(index=0, weight=1)
        widgets_frame.columnconfigure(index=1, weight=1)

        btn_back = tk.Button(self, text="Go Back to Main Page", bg="#9ED9CC", font="rockwell 10 bold italic", padx=20, pady=2, fg="#011936", relief=tk.GROOVE, width = 12,
                             command = lambda: controller.up_frame("WelcomePage"))
        btn_back.grid(row=0, column=0, pady=20,padx=5,columnspan=2, sticky="w")

        subtitle = ttk.Label(widgets_frame, text="BMI Calculator",font="rockwell 20 bold",foreground="#3E282B", background="#e95c20")
        subtitle.grid(row=0, column=0, pady=20, columnspan=2)

        info = ttk.Label(widgets_frame, text="Commonly accepted BMI ranges: underweight (<18.5), normal weight (18.5-25), overweight (25-30), and obese (>30).",
                          font="rockwell 11 italic",foreground="#3E282B", background="#e95c20")
        info.grid(row=1, column=0, pady=20, columnspan=2)
        
        # Data entry
        label_height = ttk.Label(widgets_frame, text="Height(in cm):",font="rockwell 14 bold",foreground="#011936", background="#e95c20")
        label_height.grid(row=2,column=0,sticky=tk.E,pady=(20,0))
        box_height = tk.Entry(widgets_frame, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        box_height.grid(row=2, column=1, sticky=tk.W,padx=20,pady=(20,0))

        label_weight = ttk.Label(widgets_frame, text="Weight(in kg):",font="rockwell 14 bold",foreground="#011936", background="#e95c20")
        label_weight.grid(row=3,column=0, sticky=tk.E)
        box_weight = tk.Entry(widgets_frame, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        box_weight.grid(row=3, column=1, pady=50, sticky=tk.W,padx=20)

        accentbutton = tk.Button(widgets_frame, text="Calculate BMI!", bg="#9ED9CC", font="rockwell 14 bold", padx=30, pady=5, fg="#011936",
                                 command = lambda: self.calc(box_height,box_weight))
        accentbutton.grid(row=4, column=0, padx=300, pady=20, columnspan=2)

    def calc(self, box_height, box_weight):
        height = box_height.get()
        weight = box_weight.get()

        show_method1 = getattr(messagebox, 'show{}'.format('warning'))
        if height == '':
            show_method1('Wrong Input', 'Please enter height(in cm)!')
        elif not height.isdigit():
            show_method1('Wrong Input','Please enter height as a numeric value(in cm)')
        elif weight == '':
            show_method1('Wrong Input','Please enter weight(in kg)!')
        elif not weight.isdigit():
            show_method1('Wrong Input','Please enter weight as a numeric value(in kg)')

        
        else:
            show_method = getattr(messagebox, 'show{}'.format('info'))
            bmi = int(weight)/int(height)/int(height)*10000
            message = str(round(bmi, 2))
            if bmi < 18.5:
                message += ' (underweight)'
            elif bmi < 25:
                message += ' (normal weight)'
            elif bmi < 30:
                message += ' ( overweight)'
            else:
                message += ' (obese)'
                
            show_method('Your BMI is:', message)

class RMRCalculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = '#e95c20'
        self.parent = parent
        self.controller = controller
        self.controller.title("PyHealthFacts")
        self.controller.option_add("*tearOff", False)
        self.controller.geometry("850x480")
        self.controller.columnconfigure(index=0, weight=1)
        self.controller.columnconfigure(index=1, weight=1)
        self.controller.columnconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=0, weight=1)
        self.controller.rowconfigure(index=1, weight=1)
        self.controller.rowconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=3, weight=1)
        self.controller.rowconfigure(index=4, weight=1)
        self.controller.rowconfigure(index=5, weight=1)
        self.controller.resizable(False,False)
        self.controller.configure(bg='#e95c20')

        s = ttk.Style()
        s.configure('TFrame', background='#e95c20')

        widgets_frame = ttk.Frame(self, padding=(0,0, 0, 0))
        widgets_frame.grid(row=1, column=1, padx=0, pady=(10,40), sticky="nsew")
        widgets_frame.columnconfigure(index=0, weight=1)
        widgets_frame.columnconfigure(index=1, weight=1)

        btn_back = tk.Button(self, text="Go Back to Main Page", bg="#9ED9CC", font="rockwell 10 bold italic", padx=20, pady=2, fg="#011936", relief=tk.GROOVE, width = 12,
                             command = lambda: controller.up_frame("WelcomePage"))
        btn_back.grid(row=0, column=0, pady=20,padx=5,columnspan=2, sticky="w")

        subtitle = ttk.Label(widgets_frame, text="RMR Calculator",font="rockwell 20 bold",foreground="#3E282B", background="#e95c20")
        subtitle.grid(row=0, column=0, pady=(0, 20), columnspan=2)

        # Data entry
        label_gender = ttk.Label(widgets_frame, text="Gender:",font="rockwell 14 bold",foreground="#011936", background="#e95c20")
        label_gender.grid(row=1,column=0,sticky=tk.E,pady=(20,0))
        Var1 = StringVar()
        gender_male = Radiobutton(widgets_frame, text = "Male", variable = Var1, value = 1, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        gender_male.grid(row=1, column=1, sticky=tk.W,padx=20,pady=(20,0))
        gender_female = Radiobutton(widgets_frame, text = "Female", variable = Var1, value = 2, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        gender_female.grid(row=2, column=1, sticky=tk.W,padx=20,pady=(0,0))

        
        label_age = ttk.Label(widgets_frame, text="Age(in years):",font="rockwell 14 bold",foreground="#011936", background="#e95c20")
        label_age.grid(row=3,column=0,sticky=tk.E,pady=(20,0))
        box_age = tk.Entry(widgets_frame, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        box_age.grid(row=3, column=1, sticky=tk.W,padx=20,pady=(20,0))
        
        label_height = ttk.Label(widgets_frame, text="Height(in cm):",font="rockwell 14 bold",foreground="#011936", background="#e95c20")
        label_height.grid(row=4,column=0,sticky=tk.E,pady=(20,0))
        box_height = tk.Entry(widgets_frame, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        box_height.grid(row=4, column=1, sticky=tk.W,padx=20,pady=(20,0))

        label_weight = ttk.Label(widgets_frame, text="Weight(in kg):",font="rockwell 14 bold",foreground="#011936", background="#e95c20")
        label_weight.grid(row=5,column=0, sticky=tk.E,pady=(20,0))
        box_weight = tk.Entry(widgets_frame, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        box_weight.grid(row=5, column=1, sticky=tk.W,padx=20,pady=(20,0))

        accentbutton = tk.Button(widgets_frame, text="Calculate RMR!", bg="#9ED9CC", font="rockwell 14 bold", padx=30, pady=5, fg="#011936",
                                 command = lambda: self.calcRMR(Var1, box_age, box_height, box_weight))
        accentbutton.grid(row=6, column=0, padx=300, pady=20, columnspan=2)

    def calcRMR(self, Var1, box_age, box_height, box_weight):
        gender = Var1.get()
        age = box_age.get()        
        height = box_height.get()
        weight = box_weight.get()

        show_method1 = getattr(messagebox, 'show{}'.format('warning'))
        if gender == '':
            show_method1('Wrong Input', 'Please select the gender!')
        elif age == '':
            show_method1('Wrong Input', 'Please enter age(in years)!')
        elif not age.isdigit():
            show_method1('Wrong Input','Please enter age as a numeric value(in years)')
        elif height == '':
            show_method1('Wrong Input', 'Please enter height(in cm)!')
        elif not height.isdigit():
            show_method1('Wrong Input','Please enter height as a numeric value(in cm)')
        elif weight == '':
            show_method1('Wrong Input','Please enter weight(in kg)!')
        elif not weight.isdigit():
            show_method1('Wrong Input','Please enter weight as a numeric value(in kg)')

        
        else:
            show_method = getattr(messagebox, 'show{}'.format('info'))
            if(gender == '1'):
                rmr = 9.99 * int(weight) + 6.25 * int(height) -4.92 * int(age) + 5
            else:
                rmr = 9.99 * int(weight) + 6.25 * int(height) -4.92 * int(age) - 161
            show_method('Your BMI is:', str(round(rmr, 2)) + ' calories per day')
        
class MinimalWater(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = '#e95c20'
        self.parent = parent
        self.controller = controller
        self.controller.title("PyHealthFacts")
        self.controller.option_add("*tearOff", False)
        self.controller.geometry("850x480")
        self.controller.columnconfigure(index=0, weight=1)
        self.controller.columnconfigure(index=1, weight=1)
        self.controller.columnconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=0, weight=1)
        self.controller.rowconfigure(index=1, weight=1)
        self.controller.rowconfigure(index=2, weight=1)
        self.controller.rowconfigure(index=3, weight=1)
        self.controller.resizable(False,False)
        self.controller.configure(bg='#e95c20')

        s = ttk.Style()
        s.configure('TFrame', background='#e95c20')

        widgets_frame = ttk.Frame(self, padding=(0,0, 0, 0))
        widgets_frame.grid(row=1, column=1, padx=0, pady=(10,40), sticky="nsew")
        widgets_frame.columnconfigure(index=0, weight=1)
        widgets_frame.columnconfigure(index=1, weight=1)

        btn_back = tk.Button(self, text="Go Back to Main Page", bg="#9ED9CC", font="rockwell 10 bold italic", padx=20, pady=2, fg="#011936", relief=tk.GROOVE, width = 12,
                             command = lambda: controller.up_frame("WelcomePage"))
        btn_back.grid(row=0, column=0, pady=20,padx=5,columnspan=2, sticky="w")

        subtitle = ttk.Label(widgets_frame, text="Minimal water consumption",font="rockwell 20 bold",foreground="#3E282B", background="#e95c20")
        subtitle.grid(row=0, column=0, pady=20, columnspan=2)

        info = ttk.Label(widgets_frame, text="Proper hydration is the most important health-related activity, together with deep sleep.",
                          font="rockwell 11 italic",foreground="#3E282B", background="#e95c20")
        info.grid(row=1, column=0, pady=(0, 0), columnspan=2)

        info1 = ttk.Label(widgets_frame, text="Mild dehydration can cause headaches, tiredness, inability to focus on tasks, and so on.",
                          font="rockwell 11 italic",foreground="#3E282B", background="#e95c20")
        info1.grid(row=2, column=0, pady=(40, 0), columnspan=2)
        
        # Data entry

        label_weight = ttk.Label(widgets_frame, text="Weight(in kg):",font="rockwell 14 bold",foreground="#011936", background="#e95c20")
        label_weight.grid(row=3,column=0, sticky=tk.E)
        box_weight = tk.Entry(widgets_frame, bg="#e95c20", fg="#011936", font="rockwell 14 bold", borderwidth=3)
        box_weight.grid(row=3, column=1, pady=50, sticky=tk.W,padx=20)

        accentbutton = tk.Button(widgets_frame, text="Get minimal water consumption!", bg="#9ED9CC", font="rockwell 14 bold", padx=30, pady=5, fg="#011936",
                                 command = lambda: self.calc(box_weight))
        accentbutton.grid(row=4, column=0, padx=300, pady=20, columnspan=2)

    def calc(self, box_weight):
        weight = box_weight.get()

        show_method1 = getattr(messagebox, 'show{}'.format('warning'))
        if weight == '':
            show_method1('Wrong Input','Please enter weight(in kg)!')
        elif not weight.isdigit():
            show_method1('Wrong Input','Please enter weight as a numeric value(in kg)')

        
        else:
            show_method = getattr(messagebox, 'show{}'.format('info'))
            show_method('Your water consumption should be:', str(round(int(weight)*0.04, 2)) + ' liters of water per day.')

            
if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()
