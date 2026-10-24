from address_book import AddressBook, Record, Phone

book = AddressBook()
john = Record("John")
john.add_phone("1234567890")
john.add_phone("5555555555")
book.add_record(john)
jane = Record("Jane")
jane.add_phone("9876543210")
book.add_record(jane)

assert str(john) == "Contact name: John, phones: 1234567890; 5555555555"
john_found = book.find("John")
john_found.edit_phone("1234567890", "1112223333")
assert str(john_found) == "Contact name: John, phones: 1112223333; 5555555555"
assert john_found.find_phone("5555555555").value == "5555555555"
assert john_found.find_phone("0000000000") is None
john_found.remove_phone("5555555555")
assert str(john_found) == "Contact name: John, phones: 1112223333"
john_found.add_phone("5555555555")

book.delete("Jane")
assert book.find("Jane") is None and book.find("John") is not None

for bad in ["123", "12345abcde", "12345678901"]:
    try:
        Phone(bad)
        raise SystemExit(f"accepted bad phone {bad}")
    except ValueError:
        pass
try:
    Record("")
    raise SystemExit("accepted empty name")
except ValueError:
    pass

print("ALL HW6 TESTS PASSED")
