from interfaces.vehicle import Vehicle


class VehicleImpl(Vehicle):
    def __init__(self, vehicle_id, size):
        self._vehicle_id = vehicle_id
        self._size = size

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def size(self):
        return self._size
