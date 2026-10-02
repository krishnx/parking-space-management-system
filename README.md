# Parking Space Management System

A Python-based parking space management system that allocates parking spaces to vehicles based on their size. The system follows object-oriented design principles with clear interface definitions and implementations.

## Features

- **Three Size Categories**: Support for SMALL, MEDIUM, and LARGE parking spaces and vehicles
- **Smart Space Allocation**: Vehicles are assigned the smallest suitable space to prevent unnecessary consumption of larger spaces
- **Vehicle Tracking**: System maintains a mapping of parked vehicles to their allocated spaces
- **Retrieval Management**: Easily retrieve vehicles from their parked spaces

## Design Architecture

### Interfaces (Abstract Classes)

#### `Vehicle` Interface
Defines the contract for vehicle objects with:
- `vehicle_id`: Unique identifier for the vehicle
- `size`: Size category (SMALL, MEDIUM, or LARGE)

#### `ParkingSpace` Interface
Defines the contract for parking spaces with methods:
- `can_fit(vehicle)`: Check if a vehicle can fit in this space
- `park(vehicle)`: Park a vehicle in this space
- `retrieve()`: Remove and return the parked vehicle

#### `ParkingSpaceManagementSystem` Interface
Defines the contract for the management system with methods:
- `park(vehicle) -> str`: Park a vehicle and return the parking space ID
- `retrieve(vehicle_id) -> Vehicle`: Retrieve a parked vehicle by its ID

### Implementations

- **`VehicleImpl`**: Concrete implementation of the Vehicle interface
- **`ParkingSpaceImpl`**: Concrete implementation of the ParkingSpace interface
- **`ParkingManagementSystem`**: Concrete implementation of the ParkingSpaceManagementSystem interface
- **`Size`**: Enum defining available space sizes (SMALL=1, MEDIUM=2, LARGE=3)

## Space Allocation Strategy

The system implements a greedy allocation strategy:
1. Finds all spaces that can fit the vehicle (space size >= vehicle size)
2. Selects the space with the smallest size
3. This ensures larger spaces are reserved for larger vehicles

### Example
- Vehicle (SMALL) will use SMALL space if available, not MEDIUM or LARGE
- Vehicle (MEDIUM) will use MEDIUM space if available, or LARGE if MEDIUM is full
- Vehicle (LARGE) will only use LARGE spaces

## Project Structure

```
parking-space-management-system/
├── interfaces/
│   ├── __init__.py
│   ├── vehicle.py
│   ├── parking_space.py
│   └── parking_space_management_system.py
├── enums.py
├── vehicle.py
├── parking_space.py
├── parking_space_management_system.py
├── main.py
├── Makefile
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.9 or higher
- Make (for using Makefile commands)

### Running the System

Using the Makefile:

```bash
# Run the parking system
make run

# Run with verbose output
make run-verbose

# Run tests (future enhancement)
make test

# Clean up temporary files
make clean

# Format code
make format

# Lint code
make lint

# View help
make help
```

Or run directly:

```bash
python3 main.py
```

### Expected Output
```
Parking vehicle V1 (SMALL): S1
Parking vehicle V2 (MEDIUM): M1
Parking vehicle V3 (LARGE): L1
Parking vehicle V4 (SMALL): S2

Retrieving vehicle V1: V1
Retrieving vehicle V2: V2

Parking V1 again: S1
All operations completed successfully!
```

## Usage Example

```python
from enums import Size
from vehicle import VehicleImpl
from parking_space import ParkingSpaceImpl
from parking_space_management_system import ParkingManagementSystem

# Create parking spaces
spaces = [
    ParkingSpaceImpl("S1", Size.SMALL),
    ParkingSpaceImpl("S2", Size.SMALL),
    ParkingSpaceImpl("M1", Size.MEDIUM),
    ParkingSpaceImpl("L1", Size.LARGE),
]

# Create management system
system = ParkingManagementSystem(spaces)

# Create vehicles
car1 = VehicleImpl("CAR001", Size.SMALL)
car2 = VehicleImpl("CAR002", Size.MEDIUM)

# Park vehicles
space_id_1 = system.park(car1)  # Returns "S1"
space_id_2 = system.park(car2)  # Returns "M1"

# Retrieve vehicles
retrieved_car1 = system.retrieve("CAR001")
```

## Available Commands

### Makefile Commands

| Command | Description |
|---------|-------------|
| `make help` | Display all available commands |
| `make run` | Run the parking system |
| `make test` | Run tests (placeholder for future tests) |
| `make clean` | Remove temporary files and cache |
| `make format` | Format code using black |
| `make lint` | Lint code using flake8 |
| `make install` | Install development dependencies |

## Error Handling

The system raises `ValueError` exceptions in the following scenarios:
- Attempting to park a vehicle that's already parked
- No suitable parking space available for a vehicle
- Attempting to retrieve a vehicle that's not parked
- Attempting to park in an already occupied space

## Design Principles

- **Interface Segregation**: Clear separation between abstract interfaces and implementations
- **Single Responsibility**: Each class has a single, well-defined responsibility
- **Dependency Inversion**: High-level modules depend on abstractions, not concrete implementations
- **Encapsulation**: Internal state is properly encapsulated with public properties

## Future Enhancements

- Multi-level parking structures
- Reserved parking spaces (VIP, disabled, etc.)
- Time-based charging system
- Vehicle type restrictions (bikes, motorcycles, buses)
- Parking availability API
- Real-time space occupancy dashboard
- Unit tests with pytest
- Integration tests

## License

This project is provided as-is for educational purposes.