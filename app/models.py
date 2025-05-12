from enum import Enum  # Add this import at the top
from dataclasses import dataclass

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
