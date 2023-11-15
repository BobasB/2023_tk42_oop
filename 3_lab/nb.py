import modules.example
import modules.my
from modules.my import MyPetClabModule

oo = MyPetClabModule("Богдан", "З головного файлу")
print(oo.surname)
