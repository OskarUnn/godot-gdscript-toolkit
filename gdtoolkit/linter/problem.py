import hashlib
from dataclasses import dataclass
from typing import Literal


@dataclass
class Problem:
    name: str
    description: str
    line: int
    column: int
    path: str
    severity: Literal["info", "minor", "major", "critical", "blocker"] = "info"

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "check_name": self.name,
            "fingerprint": self._generate_fingerprint(),
            "severity": self.severity,
            "location": {"path": self.path, "lines": {"begin": self.line}},
        }

    def _generate_fingerprint(self) -> str:
        fingerprint_data = f"{self.path}:{self.line}:{self.description}:{self.name}"
        return hashlib.md5(fingerprint_data.encode()).hexdigest()
