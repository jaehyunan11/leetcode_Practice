class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = {1: big, 2: medium, 3: small}

    # Add to car -> occupy the big, medium, small spots
    # if slots are fully occupied then return False
    def addCar(self, carType: int):
        if self.slots[cartType] == 0:
            return False
        self.slots[carType] -= 1
        return True
# TIME : O(1)
# Space : O(1)