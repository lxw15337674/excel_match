import tkinter.messagebox
import tkinter as tk
from ReadAndWrite import *


class App(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("权力事项对比")
        self.master.minsize(600, 300)
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
        label2 = tk.Label(text="在第几列").grid(row=2, column=1, sticky='W')
        message2 = tk.Label(text="被匹配数据信息:").grid(row=3, sticky="w")
        label3 = tk.Label(text="从第几行开始").grid(row=4, column=1, sticky='W')
        label4 = tk.Label(text="在第几列").grid(row=5, column=1, sticky='W')
        message3 = tk.Label(text="结果写入:").grid(row=6, sticky="w")
        label5 = tk.Label(text="在第几列写入").grid(row=7, column=1, sticky='W')

        # self.nameInput = Entry(self, width=50)

        self.entry1 = tk.Entry()
        self.entry1.grid(row=1, column=2, pady=5)
        # self.mrbr = tk.StringVar()
        # entry1["textvariable"] = self.mrbr
        self.entry2 = tk.Entry()
        self.entry2.grid(row=2, column=2, pady=5)
        self.entry3 = tk.Entry()
        self.entry3.grid(row=4, column=2, pady=5)
        self.entry4 = tk.Entry()
        self.entry4.grid(row=5, column=2, pady=5)
        self.entry5 = tk.Entry()
        self.entry5.grid(row=7, column=2, pady=5)
        self.btn = tk.Button(text="提交", command=self.start).grid(row=8, column=1, columnspan=5,
                                                                 rowspan=5, padx=10, pady=10)

    def start(self):
        try:
            mrbr = int(self.entry1.get())  # match_read_begin_rows
            mrc = int(self.entry2.get())  # match_read_cols
            bmrbr = int(self.entry3.get())  # bematch_read_begin_rows
            bmrc = int(self.entry4.get())  # bematch_read_cols
            write_col = int(self.entry5.get())
        except:
            tk.messagebox.showerror("错误","输入框不能为空")
            return
        print(mrbr, mrc, bmrbr, bmrc, write_col)
        ril = []  # result_index_list
        rl = []  # result_list
        rml = []  # result_matching_list
        mlist = read_match_data(mrbr, mrc)
        bmlist = read_bemathch_data(bmrbr, bmrc)
        success_num = 0
        for a in mlist:
            # print(a)
            result_index, result, matching = match.match(a, bmlist)
            ril.append(result_index)
            rl.append(result)
            rml.append(matching)
            success_num += 1
            print("已成功匹配%s个" % success_num)
        write_data(ril, rl, mrbr, write_col, rml)

    # 设置窗口居中
    def center_window(self, width=600, height=400):
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # print(size)
        self.master.geometry(size)
