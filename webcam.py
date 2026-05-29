import tkinter as tk
import cv2
from PIL import Image, ImageTk

# تابع برای به‌روزرسانی تصویر در پنجره
def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        label.after(10, update_frame)

# راه‌اندازی وب‌کم
cap = cv2.VideoCapture(0)
# چون می‌خواهیم پنجره مربعی با ابعاد مشخص باشد، بهتر است رزولوشن وب‌کم
# را هم متناسب با آن تنظیم کنیم یا مطمئن شویم که نسبت تصویر وب‌کم
# با ابعاد پنجره ما سازگار است.
# برای مثال، اگر پنجره 400x400 باشد، تنظیم وب‌کم روی 400x400 مناسب است.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)


# ایجاد پنجره اصلی Tkinter
window = tk.Tk()
window.title("Webcam.mp4 - NONE Media Player")

# --- تنظیم ابعاد پنجره (مربعی و کوچک‌تر) ---
window_width = 390
window_height = window_width
window.geometry(f"{window_width}x{window_height}")

# غیرقابل تغییر اندازه کردن پنجره
window.resizable(False, False)

# --- تنظیم آیکون پنجره (همانند قبل) ---
try:
    icon_image = tk.PhotoImage(file='faratar.png')
    window.iconphoto(True, icon_image)
except tk.TclError:
    print("خطا: فایل آیکون 'faratar.png' یافت نشد یا فرمت آن پشتیبانی نمی‌شود.")

# ایجاد یک لیبل برای نمایش تصویر
label = tk.Label(window)
label.pack()

# شروع به‌روزرسانی تصویر
update_frame()

# اجرای حلقه اصلی Tkinter
window.mainloop()

# آزادسازی وب‌کم پس از اتمام برنامه
cap.release()
cv2.destroyAllWindows()

"""import tkinter as tk
import cv2
from PIL import Image, ImageTk

# تابع برای به‌روزرسانی تصویر در پنجره
def update_frame():
    # خواندن فریم از وب‌کم
    ret, frame = cap.read()
    if ret:
        # تبدیل تصویر از BGR (فرمت OpenCV) به RGB (فرمت Pillow)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # تبدیل آرایه NumPy به تصویر Pillow
        img = Image.fromarray(frame)
        # تبدیل تصویر Pillow به فرمت قابل فهم برای Tkinter
        imgtk = ImageTk.PhotoImage(image=img)
        # به‌روزرسانی تصویر در لیبل
        label.imgtk = imgtk
        label.configure(image=imgtk)
        # فراخوانی مجدد تابع برای فریم بعدی
        label.after(10, update_frame)

# راه‌اندازی وب‌کم
cap = cv2.VideoCapture(0)
# تنظیم رزولوشن وب‌کم (اختیاری)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ایجاد پنجره اصلی Tkinter
window = tk.Tk()
window.title("Webcam.mp4 - VLC Media Player")
# غیرقابل تغییر اندازه کردن پنجره
window.resizable(False, False)

# ایجاد یک لیبل برای نمایش تصویر
label = tk.Label(window).pack()

# شروع به‌روزرسانی تصویر
update_frame()

# اجرای حلقه اصلی Tkinter
window.mainloop()

# آزادسازی وب‌کم پس از اتمام برنامه
cap.release()
cv2.destroyAllWindows()"""
