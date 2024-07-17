import tkinter as tk
from tkinter import font

def create_antivirus_interface():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("AtarBals Modern Antivirus")
    root.geometry("800x500")
    root.configure(bg='#f0f0f0')  # Đổi màu nền chính sang xám nhạt

    # Tạo khung chính
    main_frame = tk.Frame(root, bg='#f0f0f0')
    main_frame.pack(fill='both', expand=True)

    # Tạo khung cho thanh bên
    sidebar_frame = tk.Frame(main_frame, bg='#1f3c88', width=200)  # Đổi màu thanh bên sang xanh đậm
    sidebar_frame.pack(side='left', fill='y')

    # Tạo các nhãn cho thanh bên
    sidebar_labels = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
    for label_text in sidebar_labels:
        label = tk.Label(sidebar_frame, text=label_text, bg='#1f3c88', fg='white', pady=10)
        label.pack(anchor='w', padx=10)

    # Tạo nút "Scan Now"
    scan_button = tk.Button(sidebar_frame, text="Scan Now", bg='#4caf50', fg='white')  # Đổi màu nút sang xanh lá
    scan_button.pack(anchor='w', padx=10, pady=20)

    # Tạo khung cho khu vực nội dung chính
    content_frame = tk.Frame(main_frame, bg='#f0f0f0')
    content_frame.pack(side='left', fill='both', expand=True, padx=20, pady=20)

    # Tạo nhãn tiêu đề
    title_font = font.Font(family="Helvetica", size=24, weight="bold")
    title_label = tk.Label(content_frame, text="Scan", font=title_font, bg='#f0f0f0')
    title_label.pack(pady=10)

    # Tạo nhãn phụ đề
    subtitle_label = tk.Label(content_frame, text="Premium will be free forever. You just need to click button.",
                              bg='#f0f0f0')
    subtitle_label.pack(pady=5)

    # Tạo khung chứa các nút chức năng
    button_frame = tk.Frame(content_frame, bg='#f0f0f0')
    button_frame.pack(pady=20)

    buttons = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
    for i, btn_text in enumerate(buttons):
        btn = tk.Button(button_frame, text=btn_text, bg='#FFCC33', fg='black')  # Đổi màu nút sang hồng đậm
        if i % 2 == 0:
            btn.grid(row=i // 2, column=0, padx=10, pady=10)
        else:
            btn.grid(row=i // 2, column=1, padx=10, pady=10)

    # Tạo nhãn trạng thái
    status_label = tk.Label(content_frame, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}",
                            fg='#0033FF', bg='#f0f0f0')  # Đổi màu chữ trạng thái sang hồng đậm
    status_label.pack(pady=20)

    root.mainloop()

create_antivirus_interface()
