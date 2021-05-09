import numpy as np
import numpy.typing as npt


def norm_vector(v: npt.ArrayLike) -> np.ndarray: ...


def norm_matrix(R: npt.ArrayLike) -> np.ndarray: ...


def norm_angle(a: npt.ArrayLike) -> np.ndarray: ...


def norm_axis_angle(a: npt.ArrayLike) -> np.ndarray: ...


def norm_compact_axis_angle(a: npt.ArrayLike) -> np.ndarray: ...


def perpendicular_to_vectors(a: npt.ArrayLike, b: npt.ArrayLike) -> np.ndarray: ...


def perpendicular_to_vector(a: npt.ArrayLike) -> np.ndarray: ...


def angle_between_vectors(a: npt.ArrayLike, b: npt.ArrayLike, fast: bool = ...) -> float: ...


def vector_projection(a: npt.ArrayLike, b: npt.ArrayLike) -> np.ndarray: ...


def random_vector(random_state: np.random.RandomState = ..., n: int = ...) -> np.ndarray: ...


def random_axis_angle(random_state: np.random.RandomState = ...) -> np.ndarray: ...


def random_compact_axis_angle(random_state: np.random.RandomState = ...) -> np.ndarray: ...


def random_quaternion(random_state: np.random.RandomState = ...) -> np.ndarray: ...


def check_skew_symmetric_matrix(V: npt.ArrayLike, tolerance: float = ..., strict_check: bool = ...) -> np.ndarray: ...


def check_matrix(R: npt.ArrayLike, tolerance: float = ..., strict_check: bool = ...) -> np.ndarray: ...


def check_axis_angle(a: npt.ArrayLike) -> np.ndarray: ...


def check_compact_axis_angle(a: npt.ArrayLike) -> np.ndarray: ...


def check_quaternion(q: npt.ArrayLike, unit: bool = ...) -> np.ndarray: ...


def check_quaternions(Q: npt.ArrayLike, unit: bool = ...) -> np.ndarray: ...
