import pytest
from django.db import connection, transaction


@pytest.mark.django_db(transaction=True)
def test_postgres_rolls_back_an_interrupted_operation() -> None:
    assert connection.vendor == "postgresql"
    with connection.cursor() as cursor:
        cursor.execute("CREATE TEMPORARY TABLE setup_probe (value integer NOT NULL)")
    try:
        with pytest.raises(RuntimeError, match="interrupted"):
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO setup_probe VALUES (1)")
                raise RuntimeError("interrupted")
        with connection.cursor() as cursor:
            cursor.execute("SELECT count(*) FROM setup_probe")
            assert cursor.fetchone() == (0,)
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO setup_probe VALUES (2)")
        with connection.cursor() as cursor:
            cursor.execute("SELECT value FROM setup_probe")
            assert cursor.fetchone() == (2,)
    finally:
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE setup_probe")
