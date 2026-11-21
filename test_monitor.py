
def test_status_healthy():
    cpu = 20
    ram = 50
    disk = 60

    if cpu > 80 or ram > 80 or disk > 90:
        status = "WARNING"
    else:
        status = "HEALTHY"

    assert status == "HEALTHY"


def test_status_warning():
    cpu = 95
    ram = 50
    disk = 60

    if cpu > 80 or ram > 80 or disk > 90:
        status = "WARNING"
    else:
        status = "HEALTHY"

    assert status == "WARNING"
