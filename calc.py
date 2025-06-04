import tkinter as tk

LARGE_FONT = ("Arial", 40, "bold")
SMALL_FONT = ("Arial", 16)
LIGHT_GRAY = "#F5F5F5"
WHITE = "#D0CAD1"
LEBEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()

        self.buttons_frame = self.create_buttons_frame()  # ✅ Buttons frame needs to be created before creating digit buttons

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.create_digit_buttons()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LEBEL_COLOR, padx=24, font=SMALL_FONT)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LEBEL_COLOR, padx=24, font=LARGE_FONT)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LEBEL_COLOR)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
