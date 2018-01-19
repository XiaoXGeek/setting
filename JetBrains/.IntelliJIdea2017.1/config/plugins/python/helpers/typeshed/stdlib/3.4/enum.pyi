# FIXME: Stub incomplete, ommissions include:
# * the metaclass
# * _sunder_ methods with their transformations

import sys
from typing import List, Any, TypeVar, Union

class Enum:
    def __new__(cls, value: Any) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __dir__(self) -> List[str]: ...
    def __format__(self, format_spec: str) -> str: ...
    def __hash__(self) -> Any: ...
    def __reduce_ex__(self, proto: Any) -> Any: ...

    name = ...  # type: str
    value = ...  # type: Any

class IntEnum(int, Enum):
    value = ...  # type: int

_T = TypeVar('_T')

def unique(enumeration: _T) -> _T: ...

if sys.version_info >= (3, 6):
    _auto_null = ...  # type: Any

    class auto:
        value = ...  # type: Any

    class Flag(Enum):
        def __contains__(self: _T, other: _T) -> bool: ...
        def __repr__(self) -> str: ...
        def __str__(self) -> str: ...
        def __bool__(self) -> bool: ...
        def __or__(self: _T, other: _T) -> _T: ...
        def __and__(self: _T, other: _T) -> _T: ...
        def __xor__(self: _T, other: _T) -> _T: ...
        def __invert__(self: _T) -> _T: ...

    # All `type: ignore` comments below due to IntFlag making the function signatures more permissive.
    class IntFlag(int, Flag):  # type: ignore
        def __or__(self: _T, other: Union[int, _T]) -> _T: ...  # type: ignore
        def __and__(self: _T, other: Union[int, _T]) -> _T: ...  # type: ignore
        def __xor__(self: _T, other: Union[int, _T]) -> _T: ...  # type: ignore
        __ror__ = __or__
        __rand__ = __and__
        __rxor__ = __xor__
