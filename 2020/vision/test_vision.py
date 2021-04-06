import cppimport
from hypothesis import given
from hypothesis import strategies as st

import vision_dynamic
import vision_greedy

vision_cc = cppimport.imp("vision_py")


@given(st.lists(st.integers(), min_size=1), st.integers(min_value=1))
def test_python_implementations_match(satisfactions, walker):
    if walker > 1 and len(satisfactions) < 2:
        # invalid input, we need to be able to move to do more than one step.
        return

    # the difference between a single walker and multiple walkers is trivial
    walkers = [walker]
    r1 = vision_greedy.solve(satisfactions, walkers)
    r2 = vision_dynamic.solve(satisfactions, walkers)
    assert r1 == r2


@given(
    # C++ solution is slow, so limit the size of the problem.
    st.lists(
        st.integers(min_value=-(2 ** 31), max_value=2 ** 31), min_size=1, max_size=4
    ),
    st.integers(min_value=1, max_value=4),
)
def test_cpp_matches_python(satisfactions, walker):
    if walker > 1 and len(satisfactions) < 2:
        # invalid input, we need to be able to move to do more than one step.
        return

    walkers = [walker]
    r1 = vision_dynamic.solve(satisfactions, walkers)
    r2 = vision_cc.solve(satisfactions, walkers)
    assert r1 == r2
