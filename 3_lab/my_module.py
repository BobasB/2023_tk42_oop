class MyPetClabMain:
    # Не плутати таке присвоєння, ми через конструктор предаємо аргумент name який буде присвоєно атрибуту self.name 
    def __init__(self, name:str, surname:str, age:int=None, pets:list=[], dog_name:str=None, cat_name:str=None) -> None:
        self.name = name
        self.surname = surname
        # Ми можемо навіть згуповувати передані аргументи для того щоб створити потрібний атрибут
        self.full_name = f"{name} {surname}"
        self.age = age
        self.pets = pets if len(pets)>0 else "Заведи собі улюбленця!"
        self.pets_dog = dog_name if "Собака" in pets else None
        self.pets_fish = "Рибка" if "Рибка" in pets else None
        self.pets_cat = cat_name if "Кіт" in pets else None
    
    @property
    def full_name_property(self):
        return f"{self.name} {self.surname}"
