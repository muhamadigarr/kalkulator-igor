import tkinter as tk

class RobotCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Calculator")
        self.master.geometry("400x500")
        self.master.config(bg="#2C3E50")  # Warna latar belakang utama

        self.expression = ""
        
        # Entry untuk menampilkan hasil
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ECF0F1", fg="#2C3E50")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Tombol-tombol kalkulator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click(x)
            btn = tk.Button(master, text=button, padx=30, pady=20, font=("Arial", 18),
                            command=action, bg="#3498DB", fg="white", activebackground="#2980B9")
            btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(1, 5):
            master.grid_rowconfigure(i, weight=1)

    def click(self, button):
        if button == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
                print(f"Error: {e}")
        elif button == 'C':
            self.expression = ""
        else:
            self.expression += button
        
        self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = RobotCalculator(root)
    root.mainloop()
