from enum import Enum
from .tensor_shape import TensorShape

class DataType(Enum):
    bool = 0
    int8 = 1
    int16 = 2
    int32 = 3
    int64 = 4
    float16 = 5
    float32 = 6
    float64 = 7

    string = 11

    int8_ref = 21
    int16_ref = 22
    int32_ref = 23
    int64_ref = 24
    float16_ref = 25
    float32_ref = 26
    float64_ref = 27


class Tensor:
    def __init__(self, name, shape, dtype=DataType.float32):
        self._name = name
        self._shape = shape
        self._dtype = dtype

    @property
    def name(self):
        return self._name

    @property
    def shape(self):
        return self._shape

    @property
    def dtype(self):
        return self._dtype

