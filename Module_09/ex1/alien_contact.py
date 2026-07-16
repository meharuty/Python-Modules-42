from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) must include a received message"
                )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area",
            contact_type=ContactType.RADIO,
            signal_strength=8.4,
            duration_minutes=27,
            witness_count=5,
            message_received="Hello 42",
            is_verified=False
        )
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
    except ValueError as e:
        print("Validation error:", e)

    print("======================================")
    try:
        b = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Mars Base",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=20,
            witness_count=1,   # Invalid: needs at least 3
            message_received=None,
            is_verified=False
        )
        print(b)

    except ValueError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
