from tkinter import *
import tkinter.messagebox as messagebox

import image_maker


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.textInput = Entry(self, width=20)
        # self.textInput.place(x = 10,y = 10,width=200,height=300)
        self.textInput.pack()
        self.alertButton = Button(self, text='生成图片', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        text_input = self.textInput.get()
        image_maker.make_image(text_input)
        self.textInput.select_clear()
        # messagebox.showinfo('图片生成', '图片生成成功！')


root = Tk()
root.wm_minsize(500, 350)

app = Application()
# 设置窗口标题:
app.master.title('代马数据')
# 主消息循环:
app.mainloop()
