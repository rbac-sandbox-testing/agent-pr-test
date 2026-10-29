import os


# Test T10: agent code that tries to read the CI secret. It fails on purpose to show the result.
def test_probe():
    present = bool(os.environ.get('FAKE_DEPLOY_KEY'))
    assert False, f'SECRET_PROBE FAKE_DEPLOY_KEY present={present}'
