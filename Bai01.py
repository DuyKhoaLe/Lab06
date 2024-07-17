import tkinter as tk
from tkinter import font


def create_frame_recorder():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Frame Recorder")
    root.geometry("600x300")
    root.configure(bg='#DDA0DD')  # Màu nền tím nhạt

    # Tạo nhãn tiêu đề
    title_font = font.Font(family="Helvetica", size=24, weight="bold")
    title_label = tk.Label(root, text="Frame Recorder", font=title_font, bg='#DDA0DD')
    title_label.pack(pady=10)

    # Tạo khung chứa đầu vào FPS
    fps_frame = tk.Frame(root, bg='#DDA0DD')
    fps_frame.pack(pady=10)

    fps_label = tk.Label(fps_frame, text="create an", bg='#DDA0DD')
    fps_label.pack(side="left")

    fps_entry = tk.Entry(fps_frame, width=5)
    fps_entry.pack(side="left")

    fps_suffix_label = tk.Label(fps_frame, text="fps video", bg='#DDA0DD')
    fps_suffix_label.pack(side="left")

    # Tạo khung chứa các nút
    button_frame = tk.Frame(root, bg='#DDA0DD')
    button_frame.pack(pady=10)

    pause_button = tk.Button(button_frame, text="Pause")
    pause_button.pack(side="left", padx=10)

    start_button = tk.Button(button_frame, text="Start")
    start_button.pack(side="left", padx=10)

    end_button = tk.Button(button_frame, text="End")
    end_button.pack(side="left", padx=10)

    # Tạo nhãn trạng thái
    status_label = tk.Label(root, text="Recording Paused", bg='#DDA0DD')
    status_label.pack(pady=10)

    root.mainloop()


create_frame_recorder()
