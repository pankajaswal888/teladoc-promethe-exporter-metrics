from enum import Enum  # For creating enumerated constants
from dataclasses import dataclass # For reducing boilerplate code in classes

class TaskStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    SUCCEEDED = "succeeded"

@dataclass
class Task:
    tool: str
    task: str
    status: TaskStatus
    duration: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            tool=data["tool"],
            task=data["task"],
            status=TaskStatus(data["status"].lower()),
            duration=data["duration"]
        )
