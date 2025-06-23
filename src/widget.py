from masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    """
    # Разделяем название и номер
    parts = info.rsplit(' ', 1)
    if len(parts) != 2:
        raise ValueError("Неверный формат ввода")

    name, number = parts

    # Определяем тип и применяем соответствующую маску
    if len(number) == 16:
        return f"{name} {get_mask_card_number(number)}"
    elif len(number) >= 4:
        return f"{name} {get_mask_account(number)}"
    else:
        raise ValueError("Неверный формат номера")


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.
    """
    from datetime import datetime

    # Парсим дату
    date_obj = datetime.fromisoformat(date_str.rstrip('Z').split('T')[0])
    return date_obj.strftime("%d.%m.%Y")