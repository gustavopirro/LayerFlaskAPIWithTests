from cerberus import Validator

pokemon_id_validator = Validator({
    "pokemonOne": {
        "type": "dict",
        "schema": {
            "name": { "type": "string", "required": True, "empty": False, "nullable": False }
        },
    },
    "pokemonTwo": {
        "type": "dict",
        "schema": {
            "name": { "type": "string", "required": True, "empty": False, "nullable": False }
        },
    }
})