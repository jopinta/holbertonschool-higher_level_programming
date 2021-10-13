#!/usr/bin/python3
"""don’t need to manage exceptions if the object can’t be serialized
"""


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)
"""

    import json
    return json.dumps(my_obj)
