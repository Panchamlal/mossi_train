"""
Unit and regression test for the molssi_train_math python program .
"""

# Import package, test suite, and other packages as needed
import molssi_train as md_uf
import pytest
import sys

@pytest.mark.parametrize("num_list, expected_mean", [
    ([1,2,3,4,5], 3),
    ([0,2,4,6], 3),
    ([1,2,3,4], 2.5),
])

def test_many_inputs(num_list, expected_mean):
    assert md_uf.mean(num_list) == expected_mean

def test_mean():
    num_list = [1,2,3,4,5]
    observed = md_uf.mean(num_list)
    expected = 3.0

    assert expected == observed


def test_mean_wrong_type():
    test_input = 'this is not a list'

    with pytest.raises(TypeError):
        md_uf.mean(test_mean)
