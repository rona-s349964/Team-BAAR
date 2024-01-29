import tkinter as tk
from tkinter import ttk

class ThemedCalculatorApp(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master if master else tk.Tk()  # Ensure master is not None
        self.master.title("Themed Calculator")
        
        self.result_var = tk.StringVar()

        self.result_entry = ttk.Entry(self, textvariable=self.result_var, font=("Arial", 16), justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        for i in range(1, 5):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = ttk.Button(self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            self._calculate()
        elif button_text == "C":
            self.result_var.set("")
        else:
            self.result_var.set(current_text + button_text)

    def _calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(str(result))
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    themed_calculator_app = ThemedCalculatorApp()
    themed_calculator_app.mainloop()
