import tkinter as tk


class App(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("权力事项对比")
        self.master.minsize(600, 200)
        self.master.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
        self.create_widgets()

    def create_widgets(self):
        # mrbr = 1  # match_read_begin_rows
        # mrc = 2  # match_read_cols
        # bmrbr = 4  # bematch_read_begin_rows
        # bmrc = 2  # bematch_read_cols
        # write_col = 5
        message1 = tk.Label(text="匹配数据信息:").grid(row=0, sticky="w")
        label1 = tk.Label(text="从第几行开始:").grid(row=1, column=1, sticky='W')
        label2 = tk.Label(text="需要匹配数据在第几列").grid(row=2, column=1, sticky='W')
        message2 = tk.Label(text="被匹配数据信息:").grid(row=3, sticky="w")
        label3 = tk.Label(text="需要被匹配数据从第几行开始").grid(row=4, column=1, sticky='W')
        label4 = tk.Label(text="需要被匹配数据在第几列").grid(row=5, column=1, sticky='W')

        entry1 = tk.Entry().grid(row=1, column=2,pady=5)
        entry2 = tk.Entry().grid(row=2, column=2,pady=5)
        entry3 = tk.Entry().grid(row=4, column=2,pady=5)
        entry4 = tk.Entry().grid(row=5, column=2,pady=5)

        btn = tk.Button(text="提交").grid(row=6, column=1, columnspan=5,
                                             rowspan=5, padx=10, pady=10)

        # message1 = tk.Label(text="需要匹配数据信息:").pack()
        # label1 = tk.Label(text="从第几行开始:").pack()
        # label2 = tk.Label(text="需要匹配数据在第几列").pack()
        # message2 = tk.Label(text="需要被匹配数据信息:").pack()
        # label3 = tk.Label(text="需要被匹配数据从第几行开始").pack()
        # label4 = tk.Label(text="需要被匹配数据在第几列").pack()
        #
        # entry1 = tk.Entry().pack()
        # entry2 = tk.Entry().pack()
        # entry3 = tk.Entry().pack()
        # entry4 = tk.Entry().pack()
        #
        # btn = tk.Button(text="提交").pack()

    # 设置窗口居中
    def center_window(self, width=600, height=400):
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # print(size)
        self.master.geometry(size)


myapp = App()
myapp.center_window(600, 250)
myapp.mainloop()
