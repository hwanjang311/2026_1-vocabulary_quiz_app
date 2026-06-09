from __future__ import annotations

import random
import tkinter as tk
from tkinter import ttk, font

from vocabulary_quiz_app.quiz_logic import Word, check_answer, draw_word

class VocabularyQuizApp:
    def __init__(self, root: tk.Tk, words: list[Word]) -> None:
        self.all_words = words
        self.filtered_words: list[Word] = [] # 선택된 카테고리의 단어들
        self.rng = random.Random()
        self.current: Word | None = None
        self.checked = False
        self.score = 0
        self.total = 0
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="NanumGothic", size=12)
        root.title("Multi-Language Quiz")
        root.geometry("420x380")  # UI 추가로 높이를 조금 더 늘림 (340 -> 380)
        root.resizable(False, False)

        self.word_var = tk.StringVar(value="단어를 불러오는 중...")
        self.feedback_var = tk.StringVar(value="")
        self.score_var = tk.StringVar(value="Score: 0/0")

        # 언어 및 카테고리 선택 UI 프레임 추가
        selector_frame = ttk.Frame(root)
        selector_frame.pack(pady=(16, 4))
        
        # 1. 언어 선택 UI
        ttk.Label(selector_frame, text="언어:").pack(side=tk.LEFT, padx=4)
        languages = sorted(list({w.language for w in self.all_words}))
        
        self.lang_combobox = ttk.Combobox(selector_frame, values=languages, state="readonly", width=8)
        self.lang_combobox.set(languages[0] if languages else "영어")
        self.lang_combobox.pack(side=tk.LEFT, padx=4)
        self.lang_combobox.bind("<<ComboboxSelected>>", self.on_language_change)
        
        # 2. 카테고리 선택 UI
        ttk.Label(selector_frame, text="카테고리:").pack(side=tk.LEFT, padx=4)
        self.category_combobox = ttk.Combobox(selector_frame, state="readonly", width=12)
        self.category_combobox.pack(side=tk.LEFT, padx=4)
        self.category_combobox.bind("<<ComboboxSelected>>", self.on_category_change)

        # 초기 언어 설정에 맞춰 카테고리 목록 채우기
        self.update_category_combobox()

        # 하단 레이블 (영단어 -> 단어로 범용성 있게 수정)
        ttk.Label(root, text="단어").pack(pady=(12, 4))

        ###########################
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

        # 최초 목록 세팅 및 시작
        self.update_category_options()
        self.update_filtered_words()
        self.next_word()

    def update_category_options(self) -> None:
        """선택된 언어에 해당하는 카테고리만 골라 콤보박스 목록을 갱신합니다."""
        selected_lang = self.lang_combobox.get()
        # 선택된 언어의 단어들만 필터링해서 카테고리 추출
        lang_words = [w for w in self.all_words if w.language == selected_lang]
        categories = ["전체"] + sorted(list({w.category for w in lang_words}))
        
        self.category_combobox["values"] = categories
        self.category_combobox.set("전체")

    def update_filtered_words(self) -> None:
        """선택된 언어와 카테고리에 맞게 최종 단어 목록을 필터링합니다."""
        selected_lang = self.lang_combobox.get()
        selected_cat = self.category_combobox.get()
        
        # 1차 필터링: 언어 일치
        lang_words = [w for w in self.all_words if w.language == selected_lang]
        
        # 2차 필터링: 카테고리 일치
        if selected_cat == "전체":
            self.filtered_words = lang_words
        else:
            self.filtered_words = [w for w in lang_words if w.category == selected_cat]

    def reset_score(self) -> None:
        """점수를 초기화합니다."""
        self.score = 0
        self.total = 0
        self.score_var.set("Score: 0/0")

    def on_language_change(self, event: tk.Event) -> None:
        """언어가 변경되면 카테고리 목록을 새로고침하고 단어를 바꿉니다."""
        self.update_category_options()
        self.update_filtered_words()
        self.reset_score()
        self.next_word()

    def on_category_change(self, event: tk.Event) -> None:
        """카테고리가 변경되면 단어 목록을 필터링하고 새로 출제합니다."""
        self.update_filtered_words()
        self.reset_score()
        self.next_word()

    def next_word(self) -> None:
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

