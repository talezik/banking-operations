from src.masks import get_mask_card_number, get_mask_account

bank_card_number = input("Введите номер банковской карты")
bank_account_number = input("Введите номер банковского счёта")

if len(bank_card_number) == 16:
    print(f"Введён номер карты {get_mask_card_number(bank_card_number)}")
else:
    print("Неправильно введен номер банковской карты")

if len(bank_account_number) == 20:
    print(f"Введён номер счета {get_mask_account(bank_account_number)}")
else:
    print("Неправильно введен номер банковского счёта")
