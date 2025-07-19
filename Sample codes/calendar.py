import tkinter as tk
import calendar

class CalendarApp:
    def __init__(self, master):
        self.master = master
        master.title("Calendar")
        master.geometry("250x140")
        master.config(background='grey')

        # Main window widgets
        self.cal_label = tk.Label(master, text="Calendar", bg='grey', font=("times", 28, "bold"))
        self.cal_label.grid(row=1, column=1, pady=5)

        self.year_label = tk.Label(master, text="Enter year", bg='dark grey')
        self.year_label.grid(row=2, column=1, pady=2)

        self.year_field = tk.Entry(master)
        self.year_field.grid(row=3, column=1, pady=5)

        self.show_button = tk.Button(master, text='Show Calendar', fg='Black', bg='Blue', command=self.show_calendar)
        self.show_button.grid(row=4, column=1, pady=5)

        self.exit_button = tk.Button(master, text='EXIT', fg='Black', bg='Blue', command=master.quit)
        self.exit_button.grid(row=5, column=1, pady=5) # Adjusted row for better spacing

        # Configure column to center widgets
        master.grid_columnconfigure(1, weight=1)

    def show_calendar(self):
        try:
            year = int(self.year_field.get())
            if not (1900 <= year <= 2100): # Basic validation for year range
                raise ValueError("Year out of typical range (1900-2100)")

            cal_gui = tk.Toplevel(self.master) # Use Toplevel for new window
            cal_gui.title(f"Calendar for {year}")
            cal_gui.config(background='grey')

            # Generate calendar for the year
            cal_content = calendar.calendar(year)

            # Use a Text widget for better display of large text
            cal_display = tk.Text(cal_gui, font="Consolas 10 bold", bg='lightgrey', fg='black', wrap='word')
            cal_display.insert(tk.END, cal_content)
            cal_display.config(state=tk.DISABLED) # Make text read-only
            cal_display.pack(expand=True, fill='both', padx=20, pady=20)

            # Center the new window
            cal_gui.update_idletasks()
            width = cal_gui.winfo_width()
            height = cal_gui.winfo_height()
            x = self.master.winfo_x() + (self.master.winfo_width() // 2) - (width // 2)
            y = self.master.winfo_y() + (self.master.winfo_height() // 2) - (height // 2)
            cal_gui.geometry(f'{width}x{height}+{x}+{y}')

        except ValueError as e:
            tk.messagebox.showerror("Invalid Input", f"Please enter a valid year. {e}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
