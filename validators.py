from guardrails.validators import ValidatingFunction
import re

@ValidatingFunction()
def no_pokemon(value: str):
    if re.search(r"\bpokemon\b", value, re.IGNORECASE):
        return "Blocked: contains banned word 'pokemon'."
    return value