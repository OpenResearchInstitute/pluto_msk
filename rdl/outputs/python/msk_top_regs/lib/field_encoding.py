"""
peakrdl-python is a tool to generate Python Register Access Layer (RAL) from SystemRDL
Copyright (C) 2021 - 2023

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

This module is intended to distributed as part of automatically generated code by the
peakrdl-python tool. It provides the base types of field enumerations
"""
from enum import Enum
from typing import Optional
from collections import namedtuple
from json import JSONEncoder

SystemRDLEnumEntry = namedtuple('SystemRDLEnumEntry', ['int_value', 'name', 'desc'])

class SystemRDLEnum(Enum):
    """
    A Enumeration that can also hold the system RDL properties, notably the `name` and `desc
    """
    @property
    def _full_value(self) -> SystemRDLEnumEntry:
        """ The full field value (needed to some operation) """
        return super().value

    @property
    # pylint:disable-next=invalid-overridden-method
    def value(self) -> int:
        """ The integer value used to encode the field value """
        return super().value.int_value

    @property
    def rdl_name(self) -> Optional[str]:
        """
        The systemRDL name property for the encoding entry
        """
        return super().value.name

    @property
    def rdl_desc(self) -> Optional[str]:
        """
        The systemRDL name property for the encoding entry
        """
        return super().value.desc

    @classmethod
    def _missing_(cls, value): # type: ignore[no-untyped-def]

        if isinstance(value, int):
            # pylint:disable-next=protected-access,no-member
            int_mapping = {item.value: item._full_value for item in cls._member_map_.values()}
            if value not in int_mapping:
                raise ValueError(f'Enumeration has not integer value of {value}')
            return cls(int_mapping[value])

        return None

    def __str__(self) -> str:
        return self.name

class RegisterFieldJSONEncoder(JSONEncoder):
    """
    JSON Encoder that supports SystemRDLEnum
    """
    def default(self, o):   # type: ignore[no-untyped-def]
        if isinstance(o, SystemRDLEnum):
            return o.name
        # Let the base class default method raise the TypeError
        return super().default(o)
