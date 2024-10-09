import tkinter as tk
import random
from uu import decode
cur_boxes = 1

class RandomWindow(tk.Tk):
    def __init__(self):
        global cur_boxes
        tk.Tk.__init__(self)
        self.title("Find the Flag")
        self.geometry("200x100")

        self.attributes('-topmost', True)
        self.attributes('-toolwindow', True)
        self.protocol("WM_DELETE_WINDOW", self.do_nothing)

        self.ok_button = tk.Button(self, text=cur_boxes, command=self.create_new_box, font=("Helvetica", 16))
        self.ok_button.pack(pady=20)

        self.close_button = tk.Button(self, text=decode("41434d2d46372d54312d48342d4639"), command=self.quit)
        self.close_button.pack(pady=10)

        cur_boxes += 1


    def create_new_box(self):
        global cur_boxes

        new_x = random.randint(0, self.winfo_screenwidth() - 200)
        new_y = random.randint(0, self.winfo_screenheight() - 100)

        original_x = self.winfo_x()
        original_y = self.winfo_y()

        RandomWindow().geometry(f"300x100+{new_x}+{new_y}")
        self.geometry(f"300x100+{original_x}+{original_y}")

    def do_nothing(self):
        # Function to do nothing on window close
        pass

def decode(theAnswer):
    for c in theAnswer:
        ar = c
    answer = bytes.fromhex(theAnswer).decode('utf-8')
    return answer

if __name__ == "__main__":

    app = RandomWindow()
    app.mainloop()