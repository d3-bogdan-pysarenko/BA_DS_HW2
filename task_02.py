from collections import deque

def is_it_palindrome(text: str) -> bool:
    # stripping and normalizing string
    cleaned_row = "".join(ch.lower() for ch in text if ch.isalnum())

    # adding symbols into created dequeue
    my_dequeue = deque(cleaned_row)

    # comparing symbols from the both sides
    while len(my_dequeue) > 1:
        if my_dequeue.popleft() != my_dequeue.pop():
            return False

    return True


# ---- Testing time ----
tests = [
    "Racecar",
    "A man a plan a canal Panama",
    "Hello",
    "Was it a car or a cat I saw",
    "No lemon, no melon"
]

for t in tests:
    print(f"{t!r} -> {is_it_palindrome(t)}")
