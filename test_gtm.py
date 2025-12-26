import pytest
from gym import GymManager

# Fully parameterized test cases as strings
@pytest.mark.parametrize(
    "item, count",
    [
        ("Treadmill", "1"),
        ("Cycle", "2"),
        ("Weights", "3"),
        ("Rowing", "1"),
    ]
)
def test_gym(item, count):
    manager = GymManager()

    print("\nEntered Parameters:")
    print(f"Equipment: {item}")
    print(f"Used Count: {count}")

    manager.use_equipment(item, count)
    status = manager.equipment_status(item)
    most_available = manager.most_available_equipment()

    print(f"Equipment Status: {status}")
    print(f"Most Available Equipment: {most_available}")
