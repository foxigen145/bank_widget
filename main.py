from src.masks import get_mask_account
from src.masks import get_mask_card_number


def main() -> None:
    """Демо-пример работы функций маскирования."""
    print(get_mask_card_number(7000792289606361))  # Ожидаем: 7000 79** **** 6361
    print(get_mask_account(73654108430135874305))  # Ожидаем: **4305


if __name__ == "__main__":
    main()
