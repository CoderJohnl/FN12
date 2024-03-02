def yosh_tekshirish(age):
    try:
        int_age = int(age)
        return int_age > 0
    except ValueError:
        return False

def tel_tekshirish(phone):
    return phone.startswith("+998") and len(phone) == 13 and phone[1:].isdigit()

def malumot_olish():
    while True:
        name = input("Ismingizni kiriting: ")
        lastname = input("Familiyangizni kiriting: ")
        age = input("Yoshingizni kiriting: ")
        if not yosh_tekshirish(age):
            print("Yoshni noto'g'ri kiritdingiz. Iltimos, qaytadan kiriting.")
            continue
        phone = input("Telefon raqamingizni kiriting (+998xx xxx-xx-xx shaklida): ")
        if not tel_tekshirish(phone):
            print("Telefon raqamini noto'g'ri kiritdingiz. Iltimos, qaytadan kiriting.")
            continue
        email = input("Email manzilingizni kiriting: ")
        address = input("Manzilingizni kiriting: ")
        return name, lastname, int(age), phone, email, address

def filega_yozih(user_info):
    with open("users_info.txt", "a") as file:
        file.write(",".join(map(str, user_info)) + "\n")

def main():
    while True:
        user_info = malumot_olish()
        filega_yozih(user_info)
        print("Ma'lumotlar faylga saqlandi.")
        again = input("Yana ma'lumot kiritasizmi? (ha/yo'q): ")
        if again.lower() != "ha":
            break

if __name__ == "__main__":
    main()
