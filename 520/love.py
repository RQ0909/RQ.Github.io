import tkinter as tk
from tkinter import messagebox
import pygame
import requests
import tempfile
import os

class ConfessionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("❤️ 表白 ❤️")
        self.geometry("600x400")
        self.configure(bg="#FFD7C4")

        pygame.mixer.init()  # 初始化音频模块
        self.music_url = "https://music.163.com/song/media/outer/url?id=415792881.mp3"  # 你可以换成其他mp3链接
        self.music_tmp_path = None  # 临时文件路径

        self.messages = [
            "我没有随随便便爱你，会认真，会隆重，会握紧你的手，会给你很多拥抱和偏爱，你是例外，也是首选，你永远胜过别人至少在我这里，我远比你现象的更需要你，享受炙热的新鲜感，也能经得住时间的打磨，慢慢又长长的爱，周而复始",
            "我们总以为，只要心是向着对方的，就无需过多言语。但实际上，沉默并不能让问题消失，反而会让误解在黑暗中滋生。每一次的欲言又止，每一次的默默承受，都像是在感情的堤坝上凿开了一个小孔，随着时间的推移，小孔逐渐扩大，最终导致感情的决堤",
            "与你相遇是我一生最美的意外。",
            "我愿意用一生的时间，陪你走过每一个春夏秋冬。",
            "那些曾经一起度过的美好时光，那些甜蜜的誓言和承诺，在争吵和冷漠面前，似乎都变得不堪一击。我们忘记了当初是如何被对方吸引，忘记了那些让我们心动的瞬间。我们开始互相指责，互相伤害，却忘了最初的我们，是多么渴望给对方幸福。",
            "遇见你，是我最美的幸运。",
            "也许，在一段感情中，我们都太过于自我，太过于关注自己的感受，而忽略了对方的需求。我们总是希望对方能够理解自己，却忘记了理解是相互的。我们需要学会换位思考，站在对方的角度去看待问题，去感受对方的喜怒哀乐。",
            "爱情是一场漫长的修行，需要我们用一生去学习和经营。愿每一个在爱情中挣扎过、痛苦过的人，都能够找到属于自己的幸福。愿我们都能够在爱情中学会成长，学会珍惜，学会理解和包容。因为只有这样，我们才能真正拥有一段健康、美好的恋爱，才能在爱情的道路上走得更远、更稳。",
            "我的世界因你而精彩。",
            "愿余生都是你。"
        ]

        self.create_widgets()
        self.play_music()  # 初始化完成后自动播放音乐

    def create_widgets(self):
        # 标题
        title_label = tk.Label(
            self,
            text="❤️ 我有话想对你说 ❤️",
            font=("楷体", 30, "bold"),
            fg="#FF69B4",
            bg="#FFF0F5",
            relief="groove",
            bd=6
        )
        title_label.pack(pady=25)

        # 消息显示区域（初始隐藏）
        self.message_label = tk.Label(
            self,
            text="请点击下方按钮表白",
            font=("隶书", 22),
            fg="#8A2BE2",
            justify="center",
            bg="#FFD7C4",
            wraplength=520,  # 自动换行
            height=4
        )
        self.message_label.pack_forget()  # 初始隐藏

        # 按钮区域（初始隐藏）
        self.btn_frame = tk.Frame(self, bg="#FFD7C4")  # 改为实例变量
        self.btn_frame.pack_forget()  # 初始隐藏

        # 表白开始按钮（开场显示）
        self.start_btn = tk.Button(
            self,
            text="表白开始",
            command=self.start_confession,
            font=("幼圆", 24),
            fg="white",
            bg="#FF69B4",
            relief="ridge",
            bd=5,
            width=15
        )
        self.start_btn.pack(pady=50)

        # 原表白按钮（在按钮区域内）
        confess_btn = tk.Button(
            self.btn_frame,
            text="点我表白",
            command=self.show_message,
            font=("幼圆", 18),
            fg="white",
            bg="#BA55D3",
            relief="ridge",
            bd=3,
            width=12
        )
        confess_btn.grid(row=0, column=0, padx=10)

        # 再来一句按钮
        again_btn = tk.Button(
            self.btn_frame,
            text="再来一句",
            command=self.show_message,
            font=("幼圆", 18),
            fg="white",
            bg="#FF69B4",
            relief="ridge",
            bd=3,
            width=12
        )
        again_btn.grid(row=0, column=1, padx=10)

        # 弹窗表白按钮
        popup_btn = tk.Button(
            self.btn_frame,
            text="弹窗表白",
            command=self.popup_confess,
            font=("幼圆", 18),
            fg="white",
            bg="#FFB6C1",
            relief="ridge",
            bd=3,
            width=12
        )
        popup_btn.grid(row=0, column=2, padx=10)

        # 播放音乐按钮
        music_btn = tk.Button(
            self.btn_frame,
            text="播放音乐",
            command=self.play_music,
            font=("幼圆", 18),
            fg="white",
            bg="#20B2AA",
            relief="ridge",
            bd=3,
            width=12
        )
        music_btn.grid(row=0, column=3, padx=10)

        # 退出按钮
        tk.Button(
            self,
            text="关闭",
            command=self.destroy,
            font=("幼圆", 16),
            fg="white",
            bg="#8A2BE2",
            relief="ridge",
            bd=3,
            width=10
        ).pack(pady=10)

        # 底部祝福语
        footer = tk.Label(
            self,
            text="愿你每天都被爱包围~",
            font=("楷体", 14),
            fg="#FF69B4",
            bg="#FFD7C4"
        )
        footer.pack(side="bottom", pady=8)

    def start_confession(self):
        """点击'表白开始'后显示主界面内容"""
        self.start_btn.pack_forget()  # 隐藏开场按钮
        self.message_label.pack(pady=20)  # 显示消息区域
        self.btn_frame.pack(pady=10)  # 显示按钮区域

    def show_message(self):
        """随机展示一条表白语句"""
        import random
        message = random.choice(self.messages)
        self.message_label.config(text=message)

    def popup_confess(self):
        """弹窗随机表白"""
        import random
        message = random.choice(self.messages)
        messagebox.showinfo("表白", message)

    def play_music(self):
        """在线播放音乐（先下载到本地临时文件再播放）"""
        try:
            print("开始播放音乐...")  # 新增调试日志
            # 如果有上一次的临时文件，先删除
            if self.music_tmp_path and os.path.exists(self.music_tmp_path):
                try:
                    os.remove(self.music_tmp_path)
                except Exception:
                    pass
            # 下载mp3到临时文件
            response = requests.get(self.music_url, stream=True)
            response.raise_for_status()
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                for chunk in response.iter_content(chunk_size=4096):
                    tmp_file.write(chunk)
                self.music_tmp_path = tmp_file.name
            # 播放本地临时文件
            pygame.mixer.music.load(self.music_tmp_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"播放音乐失败：{e}")  # 打印错误到控制台
            messagebox.showerror("错误", f"播放音乐失败：{e}")


if __name__ == "__main__":
    app = ConfessionApp()
    app.mainloop()