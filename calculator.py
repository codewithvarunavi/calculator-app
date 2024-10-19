import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Calculator")

        self.expression = ""

        # Entry widget to display the input and output
        self.input_field = tk.Entry(root, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:  # Move to the next row
                col_val = 0
                row_val += 1

    def create_button(self, text, row, column):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_field.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, result)
                self.expression = result
            except Exception as e:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
