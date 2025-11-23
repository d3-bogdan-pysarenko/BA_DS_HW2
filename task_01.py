import time
from queue import Queue


class RequestProcessor:
    def __init__(self):
        self.queue = Queue()
        self.request_id = 0

    def generate_request(self):
        """Генерує нову заявку і додає її в чергу."""
        self.request_id += 1
        request = f"Заявка #{self.request_id}"
        print(f"[CREATE] Створено: {request}")
        self.queue.put(request)

    def process_request(self):
        """Обробляє заявку, якщо вона є в черзі."""
        if not self.queue.empty():
            request = self.queue.get()
            print(f"[PROCESS] Обробка: {request}")
            time.sleep(0.5)  # імітація тривалості обробки
        else:
            print("[INFO] Черга порожня — немає заявок для обробки.")


def main():
    processor = RequestProcessor()

    print("Система обробки заявок запущена. Натисніть Ctrl+C для виходу.\n")

    try:
        while True:
            processor.generate_request()
            processor.process_request()
            time.sleep(1)   # затримка між циклами
    except KeyboardInterrupt:
        print("\nПрограму завершено користувачем.")


if __name__ == "__main__":
    main()
