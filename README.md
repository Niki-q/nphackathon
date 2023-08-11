# Проект хакатону "Голосовий інтерфейс з використанням FastAPI і Streamlit"

Цей проект є демонстрацією голосового веб-додатку, побудованого з використанням FastAPI та Streamlit. Додаток використовує технології голос-в-текст і текст-в-голос для створення гладкої і взаємодії.

## Огляд

Проект хакатону "Голосовий інтерфейс з використанням FastAPI і Streamlit" демонструє інтеграцію двох потужних технологій: [FastAPI](https://fastapi.tiangolo.com/) та [Streamlit](https://streamlit.io/). FastAPI використовується для створення надійного та ефективного бекенд-інтерфейсу API, а Streamlit використовується для побудови інтерактивного фронтенд-інтерфейсу.

### Особливості

- **Голос-в-Текст Перетворення:** Додаток дозволяє користувачам говорити в мікрофон, перетворюючи їхні слова в текст. Цей текст потім обробляється і може використовуватись для різних цілей в додатку.

- **Текст-в-Голос Перетворення:** Користувачі можуть вводити текст, а додаток перетворить його в [синтезовану мову](https://huggingface.co/spaces/robinhad/ukrainian-tts), зробивши взаємодію більш динамічною та захоплюючою.

- **Обробка в Реальному Часі:** Бекенд обробляє голосовий ввід та текстовий вивід в реальному часі, надаючи користувачам миттєвий зворотний зв'язок та плавний досвід.

## Учасники Команди

- **Костянтин Захорулько:** [GitHub](https://github.com/)
- **Дуднев Олександр:** [GitHub](https://github.com/)
- **Мітченко Антон:** [GitHub](https://github.com/)
- **Петриченко Нікіта:** [GitHub](https://github.com/Niki-q)


## Початок Роботи

Для запуску проекту локально, виконайте такі кроки:

1. Склонуйте репозиторій: `git clone https://github.com/your-username/voice-fastapi-streamlit.git`
2. Встановіть необхідні залежності: `pip install -r requirements.txt`
3. Запустіть бекенд FastAPI: `uvicorn main:app --host 0.0.0.0 --port 8000`
4. Запустіть фронтенд Streamlit: `streamlit run app.py`

Переконайтеся, що у вас підключений мікрофон та динаміки до системи для належної роботи голосових можливостей.

## Використані Технології

- [FastAPI](https://fastapi.tiangolo.com/): Сучасний, швидкий веб-фреймворк для створення API з використанням Python.
- [Streamlit](https://streamlit.io/): Відкрита бібліотека Python для створення веб-додатків для проектів з науки про дані та машинного навчання.
- [Ukrainian TTS Model](https://huggingface.co/spaces/robinhad/ukrainian-tts): Технологія перетворення тексту в синтезовану мову українською мовою.
- [Ukrainian Voices](https://huggingface.co/spaces/theodotus/ukrainian-voices): Моделі голосів для створення синтезованої мови на українській мові.

## Подальші Покращення

- Реалізувати аутентифікацію користувача та зберігання даних для створення персоналізованих голосових профілів.
- Розширити підтримку мов для більш точного перетворення голосу в текст та натуральної синтезованої мови.
- Додати додаткові можливості, такі як переклад мови та аналіз настрою.

## Внесок

Внесок до цього проекту вітається! Не соромтеся подавати запити на вдосконалення та зміни.

## Ліцензія

Цей проект ліцензовано на умовах [Ліцензії MIT](LICENSE).
