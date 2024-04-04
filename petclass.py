class Pet:

    vet_name = "Helping Paws Veterinary"

    def __init__(self,owner_first_name,owner_last_name,pet_id,pet_name,pet_type="dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def owners_firstname(self):
        return self.__owner_first_name
    
    def owners_lastname(self):
        return self.__owner_last_name
    
    def pet_id(self):
        return self.__pet_id
    
    def pet_name(self):
        return self.__pet_name
    
    def pet_type(self):
        return self.__pet_type

    def display_pet_info(self):
        return f" Owner's first name: {self.__owner_first_name}\n Owner's last name: {self.__owner_last_name}\n Pet ID: {self.__pet_id}\n Pet Name: {self.__pet_name}\n Pet Type: {self.__pet_type}"
    
    def check_property(self,attribute):
        print(hasattr(Pet,attribute))

def main():

    pet1 = Pet("Justin", "Morvay", "1", "Pixel")
    pet2 = Pet("Justin", "Morvay", "2", "Piper")

    print(pet1.display_pet_info())
    print(pet2.display_pet_info())
    pet1.check_property("owners_firstname")

main()