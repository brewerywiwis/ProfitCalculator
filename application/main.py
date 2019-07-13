from tkinter import *

field = ["margin", "year", "principle", "button", "profit", "sep"]
node = {}


def cal():
    global node
    try:
        margin = float(node["margin"].get())
        year = float(node["year"].get())
        principle = float(node["principle"].get())
        node["profit"].set(principle * (margin ** year))
    except:
        node["profit"].set("Invalid Data")


def start():
    global field, node
    root = Tk()
    root.title("Profit Calculator")
    root.option_add("*Font", "consolas 20")
    for i, c in enumerate(field):
        if c == "button":
            Button(root, text="OK", command=cal).grid(row=i, column=1, sticky="news", pady=5, padx=50)
        elif c == "profit":
            node[c] = StringVar()
            Label(root, textvariable=node[c], bg="pink").grid(row=0, column=3, columnspan=3, rowspan=4, sticky="news",
                                                              padx=5, pady=5)
        elif c == "sep":
            Label(root, text="=>").grid(row=0, column=2, rowspan=4, sticky="ns", padx=10)
        else:
            Label(root, text=f"{c}:").grid(row=i, column=0, sticky=E)
            node[c] = StringVar()
            Entry(root, textvariable=node[c], width=20).grid(row=i, column=1, pady=5)
    return root


if __name__ == "__main__":
    root = start()
    root.mainloop()
