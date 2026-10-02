from enums import Size
from interfaces.parking_space import ParkingSpace
from interfaces.vehicle import Vehicle


class ParkingSpaceImpl(ParkingSpace):
    def __init__(self, parking_space_id: str, size: Size):
        self.space_id = parking_space_id
        self.size = size
        self._vehicle = None

    @property
    def is_available(self) -> bool:
        return self._vehicle is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        return self.is_available and vehicle.size.value <= self.size.value

    def park(self, vehicle: Vehicle) -> None:
        if not self.can_fit(vehicle):
            raise ValueError("Vehicle cannot be parked here")

        self._vehicle = vehicle

    def retrieve(self) -> Vehicle:
        if self._vehicle is None:
            raise ValueError("Parking space is empty")

        vehicle = self._vehicle
        self._vehicle = None
        return vehicle