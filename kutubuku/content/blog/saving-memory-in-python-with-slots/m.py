from dataclasses import dataclass


@dataclass
class Measurement:
    sample_id: int
    timestamp: str
