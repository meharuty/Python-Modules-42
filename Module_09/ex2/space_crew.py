from enum import Enum
from pydantic import ValidationError
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validate_space_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Captain or Commander"
                )

        if self.duration_days > 365:
            experienced = sum(
                member.years_experience >= 5
                for member in self.crew
            )

            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions require at least 50% experienced crew"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2030, 5, 20, 10, 0),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="John Smith",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Pilot",
                    years_experience=15,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C002",
                    name="Jane Doe",
                    rank=Rank.CAPTAIN,
                    age=38,
                    specialization="Engineer",
                    years_experience=10,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C003",
                    name="Bob Lee",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Medic",
                    years_experience=2,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C004",
                    name="Alice Kim",
                    rank=Rank.CADET,
                    age=24,
                    specialization="Scientist",
                    years_experience=1,
                    is_active=True,
                ),
            ],
            budget_millions=500.0,
        )
        print("Valid mission created:")
        print(f"""Mission: {valid_mission.mission_name}
                ID: {valid_mission.mission_id}
                Destination: {valid_mission.destination}
                Duration: {valid_mission.duration_days} days
                Budget: ${valid_mission.budget_millions}M
                Crew size: {len(valid_mission.crew)}
              """)
    except ValidationError as e:
        print(e)

    print("===============================")
    try:
        invalid_mission = SpaceMission(
            mission_id="X1001",
            mission_name="Bad Mission",
            destination="Moon",
            launch_date=datetime(2030, 1, 1, 9, 0),
            duration_days=100,
            crew=[
                CrewMember(
                    member_id="C005",
                    name="Tom",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Pilot",
                    years_experience=3,
                    is_active=False,
                ),
            ],
            budget_millions=100.0,
        )
        print(invalid_mission)
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
