import datetime
import pytz
import time
import tkinter as tk

# タイムゾーンのリスト
time_zones = {'Japan': 'Asia/Tokyo', 'US (Los Angeles)': 'America/Los_Angeles', 'UK': 'Europe/London'}

# GUIを作成
root = tk.Tk()
root.title('Digital Clock')

# タイムゾーンを選択するオプションメニューを作成
selected_tz = tk.StringVar(value=list(time_zones.keys())[0])
option_menu = tk.OptionMenu(root, selected_tz, *time_zones.keys())
option_menu.config(bg='black', fg='white', font=('Helvetica', 18), highlightthickness=0, activebackground='black', activeforeground='white')
option_menu.pack(side=tk.TOP, padx=10, pady=10)

# ラベルを作成して、デジタル時計を表示するための関数
label = tk.Label(root, font=('DS-Digital', 96), fg='#D4AF37', bg='black', relief=tk.RAISED)
label.pack()

# タイマー用の変数とラベルを作成
timer_value = tk.IntVar(value=0)
timer_label = tk.Label(root, font=('Helvetica', 18), fg='white', bg='black')
timer_label.pack(side=tk.TOP, pady=10)

# スタートボタンが押されたかどうかのフラグ
timer_running = False

def display_time():
    # 現在時刻を取得し、指定したタイムゾーンに変換
    now = datetime.datetime.now(pytz.timezone(time_zones[selected_tz.get()]))

    # デジタル時計を表示
    label.config(text=now.strftime('%H:%M:%S'))

    # 1秒待って時刻を更新
    label.after(1000, display_time)

def start_timer():
    global timer_value, timer_running
    if not timer_running:
        timer_value.set(60)
        timer_running = True
        update_timer()

def stop_timer():
    global timer_running
    timer_running = False

def update_timer():
    global timer_value, timer_running
    if timer_value.get() > 0 and timer_running:
        timer_value.set(timer_value.get() - 1)
        timer_label.config(text='Time left: {:02d}:{:02d}'.format(timer_value.get() // 60, timer_value.get() % 60))
        timer_label.after(1000, update_timer)
    else:
        timer_running = False
        timer_label.config(text='Time is up!', font=('Helvetica', 36, 'bold'))

# スタートボタンとストップボタンを作成して、タイマーを開始・停止する関数をバインド
timer_buttons_frame = tk.Frame(root)
timer_buttons_frame.pack(side=tk.TOP, padx=10, pady=10)

start_button = tk.Button(timer_buttons_frame, text='Start', font=('Helvetica', 18), bg='green', fg='white', command=start_timer, relief=tk.RAISED, activebackground='#7f7f7f')
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(timer_buttons_frame, text='Stop', font=('Helvetica', 18), bg='red', fg='white', command=stop_timer, relief=tk.RAISED, activebackground='#7f7f7f', state=tk.DISABLED)
stop_button.pack(side=tk.LEFT, padx=10)

def toggle_timer_buttons():
    if timer_running:
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
    else:
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

    timer_buttons_frame.after(100, toggle_timer_buttons)

toggle_timer_buttons()

display_time()
root.mainloop()