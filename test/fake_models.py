from typing import Tuple

import numpy
import numpy as np
from bmipy import Bmi


class SomeException(Exception):
    pass


class FailingModel(Bmi):
    def __init__(self, exc):
        self.exc = exc

    def initialize(self, filename):
        raise self.exc

    def update(self):
        raise self.exc

    def finalize(self):
        raise self.exc

    def get_component_name(self):
        raise self.exc

    def get_input_var_names(self):
        raise self.exc

    def get_output_var_names(self):
        raise self.exc

    def get_start_time(self):
        raise self.exc

    def get_current_time(self):
        raise self.exc

    def get_end_time(self):
        raise self.exc

    def get_time_step(self):
        raise self.exc

    def get_time_units(self):
        raise self.exc

    def get_var_type(self, name):
        raise self.exc

    def get_var_units(self, name):
        raise self.exc

    def get_var_itemsize(self, name):
        raise self.exc

    def get_var_nbytes(self, name):
        raise self.exc

    def get_var_grid(self, name):
        raise self.exc

    def get_value(self, name, dest):
        raise self.exc

    def get_value_ptr(self, name):
        raise self.exc

    def get_value_at_indices(self, name, dest, inds):
        raise self.exc

    def set_value(self, name, src):
        raise self.exc

    def set_value_at_indices(self, name, inds, src):
        raise self.exc

    def get_grid_shape(self, grid, shape):
        raise self.exc

    def get_grid_x(self, grid, x):
        raise self.exc

    def get_grid_y(self, grid, y):
        raise self.exc

    def get_grid_z(self, grid, z):
        raise self.exc

    def get_grid_spacing(self, grid, spacing):
        raise self.exc

    def get_grid_origin(self, grid, origin):
        raise self.exc

    def get_grid_rank(self, grid):
        raise self.exc

    def get_grid_size(self, grid):
        raise self.exc

    def get_grid_type(self, grid):
        raise self.exc

    def get_var_location(self, name: str) -> str:
        raise self.exc

    def get_grid_node_count(self, grid: int) -> int:
        raise self.exc

    def get_grid_edge_count(self, grid: int) -> int:
        raise self.exc

    def get_grid_face_count(self, grid: int) -> int:
        raise self.exc

    def get_grid_edge_nodes(self, grid: int, edge_nodes: np.ndarray) -> np.ndarray:
        raise self.exc

    def get_grid_face_nodes(self, grid: int, face_nodes: np.ndarray) -> np.ndarray:
        raise self.exc

    def get_grid_nodes_per_face(self, grid: int, nodes_per_face: np.ndarray) -> np.ndarray:
        raise self.exc


class GridModel(FailingModel):
    def __init__(self):
        super(GridModel, self).__init__(SomeException('not used'))

    def get_output_var_names(self) -> Tuple[str]:
        return 'plate_surface__temperature',

    def get_var_grid(self, name):
        return 0


class UniRectGridModel(GridModel):
    def get_grid_type(self, grid):
        return 'uniform_rectilinear'

    def get_grid_rank(self, grid):
        return 3

    def get_grid_size(self, grid):
        return 24

    def get_grid_shape(self, grid: int, shape: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[2, 3, 4], dst=shape)
        return shape

    def get_grid_origin(self, grid, dest):
        numpy.copyto(src=[0.1, 1.1, 2.1], dst=dest)
        return dest

    def get_grid_spacing(self, grid, dest):
        numpy.copyto(src=[0.1, 0.2, 0.3], dst=dest)
        return dest


class Rect3DGridModel(GridModel):
    def get_grid_type(self, grid):
        return 'rectilinear'

    def get_grid_size(self, grid):
        return 24

    def get_grid_rank(self, grid: int) -> int:
        return 3

    def get_grid_shape(self, grid: int, shape: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[2, 3, 4], dst=shape)
        return shape

    def get_grid_x(self, grid: int, x: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[0.1, 0.2, 0.3, 0.4], dst=x)
        return x

    def get_grid_y(self, grid: int, y: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[1.1, 1.2, 1.3], dst=y)
        return y

    def get_grid_z(self, grid: int, z: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[2.1, 2.2], dst=z)
        return z


class Rect2DGridModel(Rect3DGridModel):
    def get_grid_size(self, grid):
        return 12  # 4*3

    def get_grid_rank(self, grid: int) -> int:
        return 2

    def get_grid_shape(self, grid: int, shape: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[3, 4], dst=shape)
        return shape

    def get_grid_z(self, grid: int, z: np.ndarray) -> np.ndarray:
        raise NotImplementedError('Do not know what z is')


class Structured3DQuadrilateralsGridModel(GridModel):
    # Grid shape:
    #    0
    #   / \
    #  /   \
    # 3     1
    #  \    /
    #   \  /
    #    2
    #
    def get_grid_type(self, grid):
        return 'structured_quadrilateral'

    def get_grid_rank(self, grid: int) -> int:
        return 3

    def get_grid_size(self, grid):
        return 4

    def get_grid_shape(self, grid, shape):
        numpy.copyto(src=[1, 2, 2], dst=shape)
        return shape

    def get_grid_x(self, grid, x):
        numpy.copyto(src=[1.1, 0.1, 1.1, 2.1], dst=x)
        return x

    def get_grid_y(self, grid: int, y: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[2.2, 1.2, 0.2, 2.2], dst=y)
        return y

    def get_grid_z(self, grid: int, z: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[1.1, 2.2, 3.3, 4.4], dst=z)
        return z


class Structured2DQuadrilateralsGridModel(GridModel):
    # Grid shape:
    #    0
    #   / \
    #  /   \
    # 3     1
    #  \    /
    #   \  /
    #    2
    #
    def get_grid_type(self, grid):
        return 'structured_quadrilateral'

    def get_grid_rank(self, grid: int) -> int:
        return 2

    def get_grid_size(self, grid):
        return 4

    def get_grid_shape(self, grid, shape):
        numpy.copyto(src=[2, 2], dst=shape)
        return shape

    def get_grid_x(self, grid, x):
        numpy.copyto(src=[1.1, 0.1, 1.1, 2.1], dst=x)
        return x

    def get_grid_y(self, grid: int, y: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[2.2, 1.2, 0.2, 2.2], dst=y)
        return y

    def get_grid_z(self, grid: int, z: np.ndarray) -> np.ndarray:
        raise NotImplementedError('Do not know what z is')


class UnstructuredGridBmiModel(GridModel):
    # Grid shape:
    #    0
    #   /|\
    #  / | \
    # 3  |  1
    #  \ |  /
    #   \| /
    #    2
    #
    def get_grid_type(self, grid):
        return 'unstructured'

    def get_grid_shape(self, grid, dest):
        raise NotImplementedError('Do not know what shape is')

    def get_grid_size(self, grid):
        return 4

    def get_grid_rank(self, grid: int) -> int:
        return 2

    def get_grid_node_count(self, grid: int) -> int:
        return 4

    def get_grid_edge_count(self, grid: int) -> int:
        return 5

    def get_grid_face_count(self, grid: int) -> int:
        return 2

    def get_grid_edge_nodes(self, grid: int, edge_nodes: np.ndarray) -> np.ndarray:
        numpy.copyto(src=(0, 3, 3, 1, 2, 1, 1, 0, 2, 0), dst=edge_nodes)
        return edge_nodes

    def get_grid_face_nodes(self, grid: int, face_nodes: np.ndarray) -> np.ndarray:
        numpy.copyto(src=(0, 3, 2, 0, 2, 1), dst=face_nodes)
        return face_nodes

    def get_grid_nodes_per_face(self, grid: int, nodes_per_face: np.ndarray) -> np.ndarray:
        numpy.copyto(src=(3, 3,), dst=nodes_per_face)
        return nodes_per_face

    def get_grid_x(self, grid: int, x: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[0.1, 0.2, 0.3, 0.4], dst=x)
        return x

    def get_grid_y(self, grid: int, y: np.ndarray) -> np.ndarray:
        numpy.copyto(src=[1.1, 1.2, 1.3, 1.4], dst=y)
        return y

    def get_grid_z(self, grid: int, z: np.ndarray) -> np.ndarray:
        raise NotImplementedError('Do not know what z is')


class DTypeModel(GridModel):
    def __init__(self):
        super().__init__()
        self.dtype = numpy.dtype('float32')
        self.value = numpy.array((1.1, 2.2, 3.3), dtype=self.dtype)

    def get_var_type(self, name):
        return str(self.dtype)

    def get_var_itemsize(self, name):
        return self.dtype.itemsize

    def get_var_nbytes(self, name):
        return self.dtype.itemsize * 3

    def get_value(self, name, dest):
        numpy.copyto(src=self.value, dst=dest)
        return dest

    def get_value_at_indices(self, name, dest, inds):
        numpy.copyto(src=self.value[inds], dst=dest)
        return dest

    def set_value(self, name, src):
        self.value[:] = src

    def set_value_at_indices(self, name, inds, src):
        self.value[inds] = src


class Float32Model(DTypeModel):
    pass


class Int32Model(DTypeModel):
    def __init__(self):
        super().__init__()
        self.dtype = numpy.dtype('int32')
        self.value = numpy.array((12, 24, 36), dtype=self.dtype)


class BooleanModel(DTypeModel):
    def __init__(self):
        super().__init__()
        self.dtype = numpy.dtype('bool')
        self.value = numpy.array((True, False, True), dtype=self.dtype)
