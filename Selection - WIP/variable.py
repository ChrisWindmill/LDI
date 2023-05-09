from dataclasses import dataclass
from lexeme import Types

# Global variables dictionary
globalVariables = {}


@dataclass
class variable:
    name: str
    hasValue: bool = False
    immutable: bool = False
    strValue: str = ""
    intValue: int = 0
    floatValue: float = 0.0
    type: Types = Types.VALUE
    supertype: Types = Types.VALUE
    precedence: int = 0
    def __repr__(self):
        return self.strValue

    def update(self):
        if self.type == Types.INTEGER:
            self.strValue = str(self.intValue)
            self.floatValue = 0.0
        elif self.type == Types.FLOAT:
            self.strValue = str(self.floatValue)
            self.intValue = 0
        else:
            self.intValue = 0
            self.floatValue = 0.0
