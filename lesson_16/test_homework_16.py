import pytest

from homework_16 import TeamLead

@pytest.mark.parametrize("name, salary, department, programming_language, team_size", [
    ("Oleh", 4000, "QA", "Python", 5)
])
def test_attributes_positive(name, salary, department, programming_language, team_size):
    lead = TeamLead(
        name=name,
        salary=salary,
        department=department,
        programming_language=programming_language,
        team_size=team_size
    )

    assert lead.name == name
    assert lead.salary == salary
    assert lead.department == department
    assert lead.programming_language == programming_language
    assert lead.team_size == team_size


class TypeErrorError:
    pass

def test_attributes_negative():
    with pytest.raises(TypeError, match='missing 1 required positional argument'):
        TeamLead("Oleh", 4000, "QA", "Python")