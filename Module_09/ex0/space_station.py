from typing import Optional
from pydantic import BaseModel, Field
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
ID:                 {a.station_id}
Name:               {a.name}
Crew Size:          {a.crew_size}
Power Level:        {a.power_level:.1f}%
Oxygen Level:       {a.oxygen_level:.1f}%
Operational:        {a.is_operational}
Last Maintenance:   {a.last_maintenance:%Y-%m-%d %H:%M}
Notes:              {a.notes or 'None'}
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
    except ValueError:
        print(
            "Expected validation error:\n"
            "Input should be less than or equal to 20"
            )


if __name__ == "__main__":
    main()
