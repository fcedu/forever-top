import sys
import os
import tkinter as tk

#----------------image---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path('qrcode.gif')

#----------------window---
root = tk.Tk()

# 从屏幕上移除主窗口
root.withdraw()

top = tk.Toplevel(root)
# top.overrideredirect(1)
top.title('丰橙学院');


# 因为主窗口看不到了，所以关闭 Toplevel同时需要注销主窗口
top.protocol('WM_DELETE_WINDOW', root.destroy)

# 通过该参数让窗口一直显示在最前面
top.attributes('-topmost', 'true')

canvas = tk.Canvas(top, bg='blue', height=240, width=210, highlightthickness=0)

# 不知道为啥只支持 gif
image_file = tk.PhotoImage(file=Logo)
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(fill='both')

# but = tk.Button(top, text='退出')
# but['command'] = root.deiconify
# but.pack()

root.mainloop()
