import pytest

pytestmark = pytest.mark.django_db

from ..models import Actor

def test_str():
    actor = Actor.objects.create(
        full_name = "Testy McTesterson"
    )

    assert actor.__str__() == "Testy McTesterson"
    assert str(actor) == "Testy McTesterson"
