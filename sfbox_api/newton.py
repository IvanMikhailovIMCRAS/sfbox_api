from typing import Optional

from pydantic import BaseModel, ValidationError, field_validator


class Newton(BaseModel):
    name: str = "isaac"
    method: Optional[str] = None  # SD
    DIIS: Optional[int] = None  # 1, 2 ..
    m: Optional[int] = None  # 32, 64 ..
    deltamax: Optional[int] = None  # 10
    tolerance: Optional[float] = 1e-7

    @field_validator("DIIS", "m", "deltamax")
    @classmethod
    def validate_temperature(cls, value):
        if value and value < 1:
            raise ValueError("Newton: some integer parameter < 1")
        return value


if __name__ == "__main__":
    input = {"DIIS": 1}
    try:
        newton = Newton(**input)
        for p in newton:
            if p[1]:
                print(f"newton : {newton.name} : {p[0]} : {str(p[1])}")
    except ValidationError as err:
        print(err.json(indent=4))
