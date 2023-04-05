from cerberus import Validator
from typing import Type
from src.errors.bad_request_exception import BadRequestException
from src.validators.interface.validator_interface import ValidatorInterface

class InputValidator(ValidatorInterface):

    def __init__(self, validator: Type[Validator]) -> None:
        self.validator = validator


    def validate(self, data):
        response = self.validator.validate(data)
        print(response)
        if response is False:
            raise BadRequestException(f"Bad request received, please correct the following errors:", self.validator.errors) 


