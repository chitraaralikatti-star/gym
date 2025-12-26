import os

class GymManager:
    def __init__(self):
        self.equipment = {
            "Treadmill": 5,
            "Cycle": 3,
            "Weights": 10,
            "Rowing": 2
        }

    def use_equipment(self, item, count):
        if item not in self.equipment:
            print("Invalid equipment")
            return
        # Use eval for numeric operation on string
        self.equipment[item] -= eval(count)

    def equipment_status(self, item):
        if self.equipment[item] > 3:
            return "AVAILABLE"
        elif self.equipment[item] > 0:
            return "LIMITED"
        else:
            return "UNAVAILABLE"

    def most_available_equipment(self):
        return max(self.equipment, key=self.equipment.get)


if __name__ == "__main__":
    manager = GymManager()

    # Fully parameterized: no default values
    item = os.getenv("EQUIPMENT")
    count = os.getenv("USAGE_COUNT")

    # Check mandatory parameters
    if item is None or count is None:
        print("Error: Both EQUIPMENT and USAGE_COUNT parameters are required!")
    else:
        manager.use_equipment(item, count)

        print("Entered Parameters:")
        print(f"Equipment: {item}")
        print(f"Used Count: {count}")

        print("Equipment Status:", manager.equipment_status(item))
        print("Most Available Equipment:", manager.most_available_equipment())
