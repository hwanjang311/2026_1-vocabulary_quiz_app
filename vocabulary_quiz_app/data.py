from __future__ import annotations

from vocabulary_quiz_app.quiz_logic import Word

WORDS: list[Word] = [
    Word(term="apple", meaning="사과"),
    Word(term="book", meaning="책"),
    Word(term="chair", meaning="의자"),
    Word(term="door", meaning="문"),
    Word(term="flower", meaning="꽃"),
    Word(term="friend", meaning="친구"),
    Word(term="music", meaning="음악"),
    Word(term="school", meaning="학교"),
    Word(term="summer", meaning="여름"),
    Word(term="water", meaning="물"),

    # 일본어 데이터
    Word(term="りんご (リンゴ)", meaning="사과", category="과일", language="일본어"),
    Word(term="バナナ", meaning="바나나", category="과일", language="일본어"),
    Word(term="本 (ほん)", meaning="책", category="사물", language="일본어"),
    Word(term="椅子 (いす)", meaning="의자", category="사물", language="일본어"),
    Word(term="友達 (ともだち)", meaning="친구", category="일상", language="일본어"),
    Word(term="水 (みず)", meaning="물", category="일상", language="일본어"),
]
