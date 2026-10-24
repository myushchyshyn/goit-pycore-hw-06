from collections import UserDict


class Field:
    """Базовий клас для полів запису."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Ім'я контакту. Обов'язкове поле."""

    def __init__(self, value):
        if not value or not str(value).strip():
            raise ValueError("Name is required.")
        super().__init__(value)


class Phone(Field):
    """Номер телефону. Має містити рівно 10 цифр."""

    def __init__(self, value):
        if not (isinstance(value, str) and len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    """Запис контакту: ім'я та список телефонів."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Замінює old_phone на new_phone. Піднімає ValueError, якщо старого номера немає."""
        new = Phone(new_phone)
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[index] = new
                return
        raise ValueError(f"Phone {old_phone} not found.")

    def find_phone(self, phone: str):
        """Повертає об'єкт Phone або None, якщо номер не знайдено."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Адресна книга: зберігає записи за іменем."""

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str) -> None:
        self.data.pop(name, None)
