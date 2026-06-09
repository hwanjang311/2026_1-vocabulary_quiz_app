from __future__ import annotations

import random
import tkinter as tk
from tkinter import ttk, font

from vocabulary_quiz_app.quiz_logic import Word, check_answer, draw_word

class VocabularyQuizApp:
    def __init__(self, root: tk.Tk, words: list[Word]) -> None:
        self.all_words = words  # 전체 단어 보관
        self.filtered_words: list[Word] = []  # 선택된 카테고리의 단어들
        self.rng = random.Random()
        self.current: Word | None = None
        self.checked = False
        self.score = 0
        self.total = 0

        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="NanumGothic", size=12)

        root.title("Vocabulary Quiz")
        root.geometry("420x340")  # UI 추가로 인해 높이를 조금 늘림 (280 -> 340)
        root.resizable(False, False)

        self.word_var = tk.StringVar(value="단어를 불러오는 중...")
        self.feedback_var = tk.StringVar(value="")
        self.score_var = tk.StringVar(value="Score: 0/0")

        # 카테고리 선택 UI 추가 
        category_frame = ttk.Frame(root)
        category_frame.pack(pady=(16, 4))
        
        ttk.Label(category_frame, text="카테고리 선택:").pack(side=tk.LEFT, padx=4)
        
        # 중복 없는 카테고리 목록 추출 후 '전체' 옵션 추가
        categories = ["전체"] + sorted(list({w.category for w in self.all_words}))
        
        self.category_combobox = ttk.Combobox(category_frame, values=categories, state="readonly", width=12)
        self.category_combobox.set("전체")
        self.category_combobox.pack(side=tk.LEFT, padx=4)
        self.category_combobox.bind("<<ComboboxSelected>>", self.on_category_change)

        ttk.Label(root, text="영단어").pack(pady=(12, 4))
        ttk.Label(root, textvariable=self.word_var, font=("NanumGothic", 24)).pack()

        self.answer_entry = ttk.Entry(root, font=("NanumGothic", 14))
        self.answer_entry.pack(pady=12, ipadx=6, ipady=4)

        buttons = ttk.Frame(root)
        buttons.pack(pady=6)
        self.check_button = ttk.Button(buttons, text="채점", command=self.check_current)
        self.check_button.pack(side=tk.LEFT, padx=6)
        ttk.Button(buttons, text="다음", command=self.next_word).pack(
            side=tk.LEFT, padx=6
        )

        ttk.Label(root, textvariable=self.feedback_var).pack(pady=8)
        ttk.Label(root, textvariable=self.score_var).pack()

        # 최초 단어 목록 세팅 및 시작
        self.update_filtered_words()
        self.next_word()

    def update_filtered_words(self) -> None:
        """선택된 카테고리에 맞게 단어 목록을 필터링합니다."""
        selected = self.category_combobox.get()
        if selected == "전체":
            self.filtered_words = self.all_words
        else:
            self.filtered_words = [w for w in self.all_words if w.category == selected]

    def on_category_change(self, event: tk.Event) -> None:
        """카테고리가 변경되면 스코어를 리셋하고 새로운 단어를 출제합니다."""
        self.update_filtered_words()
        self.score = 0
        self.total = 0
        self.score_var.set("Score: 0/0")
        self.next_word()

    def next_word(self) -> None:
        # 필터링된 단어가 없을 경우 예외 처리
        if not self.filtered_words:
            self.word_var.set("단어 없음")
            return
            
        self.current = draw_word(self.filtered_words, self.rng)
        self.word_var.set(self.current.term)
        self.answer_entry.delete(0, tk.END)
        self.feedback_var.set("")
        self.checked = False
        self.check_button.state(["!disabled"])
        self.answer_entry.focus()

    def check_current(self) -> None:
        if self.current is None or self.checked:
            return
        self.checked = True
        self.total += 1
        user_input = self.answer_entry.get()
        if check_answer(self.current, user_input):
            self.score += 1
            self.feedback_var.set("정답입니다!")
        else:
            self.feedback_var.set(f"오답입니다. 정답: {self.current.meaning}")
        self.score_var.set(f"Score: {self.score}/{self.total}")
        self.check_button.state(["disabled"])
