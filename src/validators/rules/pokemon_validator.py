from cerberus import Validator

pokemon_validator = Validator({
    "pokemon": {
        "type": "dict",
        "schema": {
            "name": { "type": "string", "required": True, "empty": False, "nullable": False },
            "attack": { "type": "integer", "required": True, "empty": False, "nullable": False }
        },
    }
})