from collections import deque

def is_palindrome(text: str) -> bool:
    # очищаємо рядок: нижній регістр + видалення пробілів
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    # створюємо deque і додаємо символи
    dq = deque(cleaned)

    # порівнюємо символи з обох кінців
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


# ---- Приклади використання ----
tests = [
    "Racecar",
    "A man a plan a canal Panama",
    "Hello",
    "Was it a car or a cat I saw",
    "No lemon, no melon"
]

for t in tests:
    print(f"{t!r} -> {is_palindrome(t)}")
