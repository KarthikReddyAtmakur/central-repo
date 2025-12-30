import tkinter as tk

def press(v):
    entry1.insert(tk.END, v)

def cal():
    try:
        res = eval(entry1.get())
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, res)
    except:
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, "Error")

def clear():
    entry1.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#121212")   

entry1 = tk.Entry(
    root,
    font=("Arial", 22, "bold"),
    bg="#1f1f1f",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
entry1.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r = 1
c = 0

for i in buttons:
    cmd = cal if i == "=" else lambda x=i: press(x)

    if i == "=":
        bg = "#2e7d32"          
    elif i in "+-*/":
        bg = "#37474f"          
    else:
        bg = "#2b2b2b"          

    tk.Button(
        root,
        text=i,
        font=("Arial", 20, "bold"),
        bg=bg,
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        bd=0,
        width=5,
        height=2,
        command=cmd
    ).grid(
        row=r,
        column=c,
        padx=6,
        pady=6,
        columnspan=4 if i == "=" else 1
    )

    c += 1
    if c == 4:
        c = 0
        r += 1

tk.Button(
    root,
    text="C",
    font=("Arial", 20, "bold"),
    command=clear,
    bg="#c62828",
    fg="white",
    activebackground="#8e0000",
    bd=0,
    width=5,
    height=2
).grid(row=r, column=0, columnspan=4, padx=6, pady=6)

root.mainloop()