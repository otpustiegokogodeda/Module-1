import os

kontakty = "contacts.txt"

def zagruzit_kontakt():
    contacts = []
    if os.path.exists(kontakty):
        with open(kontakty, "r", encoding="utf-8") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

def sochranit_kontakt(contacts):
    with open(kontakty, "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

def choroshi_li_telefon(phone):
    return phone.isdigit() and len(phone) == 12

def choroshi_li_email(email):
    return "@" in email and "." in email

def dobovlenie_kontakta():
    name = input("Введите имя: ").strip()
    phone = input("Введите телефон (12 цифр): ").strip()
    email = input("Введите email: ").strip()
    
    if not name or not choroshi_li_telefon(phone) or not choroshi_li_email(email):
        print("❌ Неверные данные. Попробуйте снова.")
        return
    
    contacts = zagruzit_kontakt()
    contacts.append({"name": name, "phone": phone, "email": email})
    sochranit_kontakt(contacts)
    print("✅ Контакт успешно добавлен!")

def naiti_kontakt():
    query = input("Введите имя или телефон для поиска: ").strip()
    contacts = zagruzit_kontakt()
    results = [c for c in contacts if query in (c['name'], c['phone'])]
    if results:
        for contact in results:
            print(contact)
    else:
        print("❌ Контакт не найден.")

def udolit_kontakt():
    query = input("Введите имя или телефон для удаления: ").strip()
    contacts = zagruzit_kontakt()
    new_contacts = [c for c in contacts if query not in (c['name'], c['phone'])]
    if len(new_contacts) == len(contacts):
        print("❌ Контакт не найден.")
    else:
        sochranit_kontakt(new_contacts)
        print("✅ Контакт удалён!")

def obnovit_kontakt():
    query = input("Введите имя или телефон для обновления: ").strip()
    contacts = zagruzit_kontakt()
    for contact in contacts:
        if query in (contact['name'], contact['phone']):
            name = input("Введите новое имя: ").strip()
            phone = input("Введите новый телефон (12 цифр): ").strip()
            email = input("Введите новый email: ").strip()
            
            if not name or not choroshi_li_telefon(phone) or not choroshi_li_email(email):
                print("❌ Неверные данные. Попробуйте снова.")
                return
            
            contact.update({"name": name, "phone": phone, "email": email})
            sochranit_kontakt(contacts)
            print("✅ Контакт обновлён!")
            return
    print("❌ Контакт не найден.")

def posmotret_kontakty():
    contacts = sorted(zagruzit_kontakt(), key=lambda c: c['name'])
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("❌ Список контактов пуст.")

def osnovanie():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Удалить контакт")
        print("4. Обновить контакт")
        print("5. Просмотреть контакты")
        print("6. Выйти")
        
        choice = input("Введите номер действия: ").strip()
        
        if choice == "1":
            dobovlenie_kontakta()
        elif choice == "2":
            naiti_kontakt()
        elif choice == "3":
            udolit_kontakt()
        elif choice == "4":
            obnovit_kontakt()
        elif choice == "5":
            posmotret_kontakty()
        elif choice == "6":
            print("👋 Программа завершена. До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
osnovanie()