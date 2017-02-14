#coding=utf-8
import Tkinter
class gui:
    def __init__(self):
        pass

    def main_window(self):
        main_window = Tkinter.Tk()
        li = ['C', 'python', 'php', 'html', 'SQL', 'java']
        movie = ['CSS', 'jQuery', 'Bootstrap']
        listb = Tkinter.Listbox(main_window)

        for item in li:
            # 第一个小部件插入数据
            listb.insert(0, item)
        listb.pack()
        # 将小部件放置到主窗口中
        main_window.mainloop()


gui=gui()
gui.main_window()