import os
from gtts import gTTS
import pygame

from __future__ import annotations

import random
from dataclasses import dataclass

@dataclass(frozen=True)
class Word:
    term: str
    meaning: str
    category: str #카테고리 필드 추가
    language: str #언어 필드 추가


def normalize_answer(text: str) -> str:
    return " ".join(text.strip().lower().split())


def check_answer(word: Word, user_input: str) -> bool:
    return normalize_answer(user_input) == normalize_answer(word.meaning)


def draw_word(words: list[Word], rng: random.Random | None = None) -> Word:
    if not words:
        raise ValueError("Word list is empty")
    chooser = rng if rng is not None else random
    return chooser.choice(words)

# 단어 발음 재생 기능 추가
def play_pronunciation(word: Word) -> None:
    """단어의 언어에 맞춰 발음을 오디오로 재생합니다."""
    if not word:
        return

    # 언어 코드 매핑
    lang_code = "en" if "영어" in word.language else "ja"
    
    try:
        # pygame 오디오 믹서 초기화
        pygame.mixer.init()
        
        # 임시 오디오 파일 저장 경로
        tts_filename = "temp_pronunciation.mp3"
        
        # gTTS를 이용해 음성 파일 생성
        tts = gTTS(text=word.term, lang=lang_code)
        tts.save(tts_filename)
        
        # 오디오 재생
        pygame.mixer.music.load(tts_filename)
        pygame.mixer.music.play()
        
        # 재생이 끝날 때까지 대기 후 파일 해제 (동기화 거침)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        pygame.mixer.music.unload()
        
        # 사용한 임시 파일 삭제
        if os.path.exists(tts_filename):
            os.remove(tts_filename)
            
    except Exception as e:
        print(f"발음 재생 오류: {e}")
