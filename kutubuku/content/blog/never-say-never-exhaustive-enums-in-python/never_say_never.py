from enum import Enum, auto
from typing import Never


def lab_processing_error(message: str) -> Never:
    raise RuntimeError(f"Lab processing error: {message}")


class LabStep(Enum):
    SAMPLE_PREPARATION = auto()
    DILUTION = auto()
    MIXING = auto()
    NORMALIZATION = auto()  # New step added


def liquid_handler(step: LabStep) -> str:
    match step:
        case LabStep.SAMPLE_PREPARATION:
            return "Prepare the sample..."
        case LabStep.DILUTION:
            return "Dilute the sample..."
        case LabStep.MIXING:
            return "Mix the sample..."
        case LabStep.NORMALIZATION:
            return "Normalize the sample..."
        case _:
            _: Never = step
            raise RuntimeError(f"The step is unhandled: {step}")
