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

This module provides a set of "dummy" callbacks that provide the most basic of operations
"""
from array import array as Array
import asyncio

from ..lib.utility_functions import get_array_typecode

# many of the functions in this file do not use all the arguments, this is because they are stub
# functions
# pylint: disable=unused-argument


def dummy_read(addr: int, width: int, accesswidth: int) -> int:
    """
    Callback to simulate the operation of the package, everytime the read is called, it return
    an integer value of 0

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits

    Returns:
        value inputted by the used
    """
    return int(0)


def dummy_write(addr: int, width: int, accesswidth: int, data: int) -> None:
    """
    Callback to simulate the operation of the package, everytime the write is called, it will
    print the content

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        data: value to be written to the register

    Returns:
        None
    """
    # pylint: disable-next=bad-builtin
    print(f'0x{data:X} written to 0x{addr:X}')


def dummy_read_block(addr: int, width: int, accesswidth: int, length:int) -> list[int]:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        length: number of array entries

    Returns:
        an array with the correct type (based on width) populated with 0's

    """
    return [0 for x in range(length)]


def dummy_read_block_legacy(addr: int, width: int, accesswidth: int, length:int) -> Array:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        length: number of array entries

    Returns:
        an list with the correct type (based on width) populated with 0's

    """
    return Array(get_array_typecode(width=width), [0 for x in range(length)])


def dummy_write_block(addr: int, width: int, accesswidth: int,  data: list[int]) -> None:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        data: number of array entries

    Returns:
        None

    """
    # pylint: disable=unnecessary-pass
    pass


def dummy_write_block_legacy(addr: int, width: int, accesswidth: int,  data: Array) -> None:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        data: number of array entries

    Returns:
        None

    """
    # pylint: disable=unnecessary-pass
    pass


async def async_dummy_read(addr: int, width: int, accesswidth: int) -> int:
    """
    async Callback to simulate the operation of the package, everytime the read is called, it
    return an integer value of 0

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits

    Returns:
        value inputted by the used
    """
    await asyncio.sleep(0)
    return dummy_read(addr, width, accesswidth)


async def async_dummy_write(addr: int, width: int, accesswidth: int, data: int) -> None:
    """
    Callback to simulate the operation of the package, everytime the write is called, it will
    print the content

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        data: value to be written to the register

    Returns:
        None
    """
    await asyncio.sleep(0)
    return dummy_write(addr, width, accesswidth, data)


async def async_dummy_read_block(addr: int,
                                 width: int,
                                 accesswidth: int,
                                 length: int) -> list[int]:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        length: number of array entries

    Returns:
        an array with the correct type (based on width) populated with 0's

    """
    await asyncio.sleep(0)
    return dummy_read_block(addr, width, accesswidth, length)


async def async_dummy_read_block_legacy(addr: int,
                                        width: int,
                                        accesswidth: int,
                                        length: int) -> Array:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        length: number of array entries

    Returns:
        an List with the correct type (based on width) populated with 0's

    """
    await asyncio.sleep(0)
    return dummy_read_block_legacy(addr, width, accesswidth, length)


async def async_dummy_write_block(addr: int,
                                  width: int,
                                  accesswidth: int, data: list[int]) -> None:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        data: number of array entries

    Returns:
        None

    """
    await asyncio.sleep(0)
    return dummy_write_block(addr, width, accesswidth, data)


async def async_dummy_write_block_legacy(addr: int,
                                         width: int,
                                         accesswidth: int, data: Array) -> None:
    """
    Callback to simulate the operation of the package, everytime the read_block is called, it
    return an integer value of array of o's

    Args:
        addr: Address to write to
        width: Width of the register in bits
        accesswidth: Minimum access width of the register in bits
        data: number of array entries

    Returns:
        None

    """
    await asyncio.sleep(0)
    return dummy_write_block_legacy(addr, width, accesswidth, data)
