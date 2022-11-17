import pytest
from Guass_Jordan_Elimination import *


@pytest.fixture
def ensure_2D(A):
    assert len(A) > 0, "Matrix needs to contain at least one row!"
    assert len(A[0]) > 0, "Cannot have an empty 2D array!"
    if len(A) > 1:
        for r in range(len(A) - 1):
            assert len(A[r]) == len(A[r + 1]), "Row lengths must be equal!"


@pytest.mark.parametrize("A, A_O", [([[0, 0, 0],[1, 1, 1], [0, 0, 0]], [[1, 1, 1], [0, 0, 0], [0, 0, 0]]), ([[1, 5, 1], [2, 11, 5]], [[1, 5, 1], [2, 11, 5]])])
def test_zeros_to_bottom(ensure_2D, A, A_O):
    assert zeros_to_bottom(A) == A_O


@pytest.mark.parametrize("A, r1, r2, A_O", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 0, [[7, 8, 9], [4, 5, 6], [1, 2, 3]])])
def test_swap(ensure_2D, A, r1, r2, A_O):
    assert type(r1) == int
    assert type(r2) == int
    assert swap(A, r1, r2) == A_O


@pytest.mark.parametrize("A, r, d", [([[0, 1, 1], [0, 0, 0]], 0, {'value': 1, 'col_idx': 1})])
def test_find_leading_entry(ensure_2D, A, r, d):
    assert type(r) == int
    assert find_leading_entry(A, r) == d


@pytest.mark.parametrize("A, r, s, O", [([[1, 2, 3], [0, 0, 1]], 1, 3, [0, 0, 3])])
def test_multiply_row(ensure_2D, A, r, s, O):
    assert type(r) == int
    assert type(s) == int
    assert multiply_row(A, r, s) == O


@pytest.mark.parametrize("A, r1, r2, O", [([[1, 2, 3], [2, 0, -1]], 0, 1, [3, 2, 2])])
def test_add_rows(ensure_2D, A, r1, r2, O):
    assert type(r1) == int
    assert type(r2) == int
    assert add_two_rows(A, r1, r2) == O


@pytest.mark.parametrize("A, row, r2, O", [([[1, 2, 3], [2, 0, -1]], [1, 2, 3], 1, [3, 2, 2])])
def test_add_rows_2(ensure_2D, A, row, r2, O):
    assert type(row) == list
    assert type(r2) == int
    assert add_two_rows(A, row, r2) == O


@pytest.mark.parametrize("A, A_O", [([[0, 1, 0],[0, 0, 1], [1, 0, 0]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]])])
def test_sort_rows(ensure_2D, A, A_O):
    assert sort_rows(A) == A_O


@pytest.mark.parametrize("A, c_i, f_r, A_O", [([[1, 4, 5], [2, 6, 7], [3, 8, 9]], 0, 0, [[3, 8, 9], [2, 6, 7], [1, 4, 5]])])
def test_get_top_row(ensure_2D, A, c_i, f_r, A_O):
    assert get_top_row(A, column_index=0, frontier_row=0) == A_O


@pytest.mark.parametrize("A, A_O", [([[1, 4, 1, 1, 0], [1, 2, 6, 2, 0], [1, 4, 4, 1, 0], [1, 2, 2, 2, 0]], [[1, 0, 0, 3, 0], [0, 1, 0, -0.5, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])])
def test_rref(ensure_2D, A, A_O):
    assert rref(A) == A_O

