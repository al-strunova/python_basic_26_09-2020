class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self):
        self.equipment = {}

    def add_equipment(self, *equipments):
        for each in equipments:
            if type(each).__name__ in self.equipment:
                self.equipment[type(each).__name__].append(each.__dict__)
            else:
                self.equipment[type(each).__name__] = [each.__dict__]

    def print_equipment_list(self):
        for eq_type, values in self.equipment.items():
            print("\n" + "*" * 3)
            print(f"Equipment: {eq_type}")
            print(f"Number of items: {len(values)}")
            for item in range(len(values)):
                print(f"#{item + 1} item characteristics: {values[item]}")


class OfficeEquipment:
    def __init__(self, e_label, e_speed, e_condition):
        self.e_label = e_label
        self.e_speed = e_speed
        self.e_condition = e_condition


class Printer(OfficeEquipment):
    def __init__(self, e_label, e_speed, e_condition, e_noise_level):
        super().__init__(e_label, e_speed, e_condition)
        self.e_noise_level = e_noise_level


class Scanner(OfficeEquipment):
    def __init__(self, e_label, e_speed, e_condition, e_color_depth):
        super().__init__(e_label, e_speed, e_condition)
        self.e_color_depth = e_color_depth


class Shredder(OfficeEquipment):
    def __init__(self, e_label, e_speed, e_condition, e_security_level):
        super().__init__(e_label, e_speed, e_condition)
        self.e_security_level = e_security_level


# Add items manually
equipment1 = Shredder("shr_01_01", 100, "bad", "not secure")
equipment2 = Shredder("shr_01_02", 1000, "great", "secure")
equipment3 = Scanner("sca_01_01", 1500, "great", 400)
equipment4 = Printer("shr_01_01", 1000, "good", "quiet")
storage_01 = Storage()
storage_01.add_equipment(equipment1, equipment2, equipment3, equipment4)
storage_01.print_equipment_list()

# Ask user to add items:
storage_02 = Storage()
print("\n" + "=" * 20)
while True:
    try:
        print("\nAdding a new item to a storage:\n")
        item_type = input("Enter '1' if you want to add Shredder, '2' if you want to add Scanner, "
                          "'3' if you want to add Printer. Please type ENTER if you want to STOP > ")
        if not item_type:
            break
        elif not item_type.isdigit():
            raise OwnError("Entered value is not a number")
        elif int(item_type) not in [1, 2, 3]:
            raise OwnError("Entered value is not 1, 2 or 3")
    except OwnError as err:
        print(err)
    else:
        label = input("Enter its label: ")
        speed = input("Enter its speed: ")
        condition = input("Enter its condition: ")
        if item_type == "1":
            security_level = input("Enter its security level: ")
            storage_02.add_equipment(Shredder(label, speed, condition, security_level))

        if item_type == "2":
            color_depth = input("Enter its color depth: ")
            storage_02.add_equipment(Scanner(label, speed, condition, color_depth))

        if item_type == "3":
            noise_level = input("Enter its noise level: ")
            storage_02.add_equipment(Printer(label, speed, condition, noise_level))
storage_02.print_equipment_list()
