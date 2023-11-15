class MyPetClabModule:
    participants = 0
    # Не плутати таке присвоєння, ми через конструктор предаємо аргумент name який буде присвоєно атрибуту self.name 
    def __init__(self, name:str, surname:str, age:int=None, pets:set={}, dog_name:str=None, cat_name:str=None) -> None:
        self.name = name
        self.surname = surname
        # Ми можемо навіть згуповувати передані аргументи для того щоб створити потрібний атрибут
        self.full_name = f"{name} {surname}"
        self.age = age
        # ми зробили цю змінну через сет бо хочемо мати унікальну колекцію даних
        self.pets = pets if len(pets)>0 else "Заведи собі улюбленця!"
        self.pets_dog = self.check_breed("Собака", pets, dog_name)
        self.pets_fish = self.check_breed("Рибка", pets, "")
        self.pets_cat = self.check_breed("Кіт", pets, cat_name)
        MyPetClabModule.participants += 1
    
    @property
    def full_name_property(self):
        return f"{self.name} {self.surname}"

    @property
    def pets_amount(self):
        return len(self.pets) if not isinstance(self.pets, str) else None
    
    def add_new_pet(self, breed:str, name:str):
        if not isinstance(self.pets, str):
            self.pets.add(breed)
        else:
            self.pets = {breed}
        
        if breed == "Кіт":
            self.pets_cat = name
        elif breed == "Собака":
            self.pets_dog = name
        elif breed == "Рибка":
            self.pets_fish = name
    
    def remove_pets(self, breed:str):
        print(f"Дуже шкода що вже немає нашого улюбленця {breed}!")
        if not isinstance(self.pets, str):
            self.pets.remove(breed)
        else:
            print(f"У тебе не було домашнього улюбленця {breed}! {self.pets}")
    
    @staticmethod
    def invite_friend(name:str):
        print(f"{name} приходи до нашого клубу. Ми тобі будемо раді!")

    @staticmethod
    def check_breed(breed:str, pets:set, name:str):
        if breed in pets:
            return name
        return None
    
    @classmethod
    def create_default_user(cls, ):
        print("Стврюється дефолтний користувач!")
        return cls("Користувач", "За замовчуванням")

    @classmethod
    def create_user_with_bithrday(cls, name, surname, birthdate):
        try:
            # Вираховуємо вік та виводимо результат
            from datetime import datetime
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d')

            # Отримуємо поточну дату
            current_date = datetime.now()

            # Визначаємо різницю в роках між поточною датою та датою народження
            age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
            print(f"Ваш вік: {age} років")
            return cls(name, surname, age)
        except ValueError:
            m = "Неправильний формат дати. Введіть дату у форматі 'рік-місяць-день'."
            print(m)
            raise ValueError(m)
        

if __name__ == "__main__":
    print("Тут ми будемо створювати обєкти, але вони будуть доступними тільки тут при прямому виклику даного файлу.")
    obj = MyPetClabModule("Богдан", "Модуль")
    print(f'{obj.surname}')