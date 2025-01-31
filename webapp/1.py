import os

# Проверяем значение переменной FLASK_APP
flask_app = os.getenv("FLASK_APP")
print(f"FLASK_APP: {flask_app}")

# Выводим все переменные среды
print("Все переменные среды:", dict(os.environ))
