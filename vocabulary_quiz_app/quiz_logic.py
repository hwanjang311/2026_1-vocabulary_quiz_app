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
