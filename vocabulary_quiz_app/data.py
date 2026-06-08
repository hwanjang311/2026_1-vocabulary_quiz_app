from __future__ import annotations
from vocabulary_quiz_app.quiz_logic import Word

# 카테고리 추가
WORDS: list[Word] = [
    # 과일 카테고리
    Word(term="apple", meaning="사과", category="과일"),
    Word(term="banana", meaning="바나나", category="과일"),
    Word(term="grape", meaning="포도", category="과일"),
    
    # 사물 카테고리
    Word(term="book", meaning="책", category="사물"),
    Word(term="chair", meaning="의자", category="사물"),
    Word(term="door", meaning="문", category="사물"),
    
    # 일상 카테고리
    Word(term="flower", meaning="꽃", category="일상"),
    Word(term="friend", meaning="친구", category="일상"),
    Word(term="music", meaning="음악", category="일상"),
    Word(term="school", meaning="학교", category="일상"),
    Word(term="summer", meaning="여름", category="일상"),
    Word(term="water", meaning="물", category="일상"),
]

