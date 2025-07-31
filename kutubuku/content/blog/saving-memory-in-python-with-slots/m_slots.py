from dataclasses import dataclass


@dataclass(slots=True)
class Measurement:
    sample_id: int
    timestamp: str
