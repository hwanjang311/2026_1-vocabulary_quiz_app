from __future__ import annotations
from vocabulary_quiz_app.quiz_logic import Word

# 영어와 일본어 모두 언어와 카테고리가 분류된 데이터 리스트
WORDS: list[Word] = [
    # 1. 영어 - 과일 카테고리
    Word(term="apple", meaning="사과", category="과일", language="영어"),
    Word(term="banana", meaning="바나나", category="과일", language="영어"),
    Word(term="grape", meaning="포도", category="과일", language="영어"),
    
    # 2. 영어 - 사물 카테고리
    Word(term="book", meaning="책", category="사물", language="영어"),
    Word(term="chair", meaning="의자", category="사물", language="영어"),
    Word(term="desk", meaning="책상", category="사물", language="영어"),
    
    # 3. 영어 - 일상 카테고리
    Word(term="friend", meaning="친구", category="일상", language="영어"),
    Word(term="water", meaning="물", category="일상", language="영어"),
    Word(term="school", meaning="학교", category="일상", language="영어"),

    # 일본어 추가
    # 1. 일본어 - 과일 카테고리
    Word(term="りんご", meaning="사과", category="과일", language="일본어"),
    Word(term="バナナ", meaning="바나나", category="과일", language="일본어"),
    Word(term="ぶどう", meaning="포도", category="과일", language="일본어"),
    
    # 2. 일본어 - 사물 카테고리
    Word(term="本 (ほん)", meaning="책", category="사물", language="일본어"),
    Word(term="椅子 (いす)", meaning="의자", category="사물", language="일본어"),
    Word(term="机 (つくえ)", meaning="책상", category="사물", language="일본어"),
    
    # 3. 일본어 - 일상 카테고리
    Word(term="友達 (ともだち)", meaning="친구", category="일상", language="일본어"),
    Word(term="水 (みず)", meaning="물", category="일상", language="일본어"),
    Word(term="学校 (がっこう)", meaning="학교", category="일상", language="일본어"),
]

