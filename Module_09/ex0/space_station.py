from typing import Optional
from pydantic import BaseModel, Field
from pydantic import ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    a = SpaceStation(
                    station_id='ISS001',
                    name="International Space Station",
                    crew_size=6,
                    power_level=85.5,
                    oxygen_level=92.3,
                    last_maintenance=datetime.now(),
                    )
    print("Valid station created:")
    print(f"""
    ID: {a.station_id}
    Name: {a.name}
    Crew Size: {a.crew_size}
    Power Level: {a.power_level}%
    Oxygen Level: {a.oxygen_level}%
    Last Maintenance: {a.last_maintenance:%Y-%m-%d %H:%M}
""")
    try:
        b = SpaceStation(
                    station_id='ISS001',
                    name="International Space Station",
                    crew_size=50,
                    power_level=85.5,
                    oxygen_level=92.3,
                    last_maintenance=datetime.now(),
                    )
        print(b)
    except ValidationError as e:
        print("Expected validation error:\n", e)


if __name__ == "__main__":
    main()
