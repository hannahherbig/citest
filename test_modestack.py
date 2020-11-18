from modestack import ModeStack


def test_modestack():
    stack = ModeStack()
    # assert stack.mode() is None
    stack.push(5)
    assert stack.mode() == 5
    stack.push(1)
    assert stack.mode() == 5
    stack.push(1)
    assert stack.mode() == 1
    assert stack.pop() == 1
    assert stack.mode() == 5
    assert stack.pop() == 1
    assert stack.mode() == 5
    assert stack.pop() == 5
    # assert stack.mode() is None
