import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(padx=10, pady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root)
frame.pack()

row = col = 0
for b in buttons:
    if b == '=':
        tk.Button(frame, text=b, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(frame, text=b, width=5, height=2, command=lambda x=b: click(x)).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1
tk.Button(root, text="Clear", width=20, height=2, command=clear).pack(pady=10)
root.mainloop()