#!/usr/bin/python3
"""don’t need to manage exceptions if the object can’t be serialized
"""


def from_json_string(my_str):
    """ returns the JSON representation of an object (string)
"""

    import json
    return json.loads(my_str)
