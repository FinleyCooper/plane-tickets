import json
from dataclasses import dataclass
from typing import Optional


@dataclass
class Seat:
    """Class for representing a seat in the plane"""

    _id: str
    passenger_id: Optional[str]
    passenger_information: Optional[str]
    _class: str
    plane_name: str

    def toJSON(self, sensitive_data: bool = False) -> str:
        """Returns a JSON representation of the Seat object"""

        def object_to_dict(obj):
            dictionary = obj.__dict__
            if not sensitive_data:
                dictionary.pop("passenger_id")
                dictionary["taken"] = bool(dictionary.pop("passenger_information"))

            return dictionary
            
        return json.dumps(self, default=object_to_dict)
