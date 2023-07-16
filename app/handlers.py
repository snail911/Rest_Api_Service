def get_declared_value(cargo_type: str):
    if cargo_type == "Glass":
        return 1000  # Пример значения объявленной стоимости для типа груза "Glass"
    elif cargo_type == "Other":
        return 500  # Пример значения объявленной стоимости для типа груза "Other"
    else:
        return 0  # Обработка недопустимого типа груза
