from dataclasses import dataclass


@dataclass
class LogMessage:
    create: str = 'New register has been created.'
    error: str = 'Error inserting record.'