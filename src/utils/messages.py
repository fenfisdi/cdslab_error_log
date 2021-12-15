from dataclasses import dataclass


@dataclass
class LogMessage:
    created: str = 'Error log will be reported'
