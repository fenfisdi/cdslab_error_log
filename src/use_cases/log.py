from uuid import uuid1

from src.models import NewRegister, Register


class CreateLog:

    @classmethod
    def handle(cls, error: NewRegister):
        error_log = Register(
            uuid=uuid1(),
            application=error.application,
            code=error.code,
            message=error.message,
            reported_at=error.date
        )
        error_log.save()
