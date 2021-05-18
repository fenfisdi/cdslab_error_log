from datetime import datetime
from src.models import NewRegister, Register

class Log:
    
    @classmethod
    def create_register(cls, register: NewRegister):
        error = Register(**register.dict())
        error.create_date = datetime.now().strftime('%d/%m/%Y  %H:%M:%S')
        error.save()