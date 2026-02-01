from homework_10_01 import TeamLead

def test_atr():
    tl = TeamLead(
        name="Максим",
        salary=4500,
        department="Web Dev",
        programming_language="Python",
        team_size=999
    )

    assert hasattr(tl, 'name')
    assert hasattr(tl, 'salary')
    assert hasattr(tl, 'department')
    assert hasattr(tl, 'programming_language')
    assert hasattr(tl, 'team_size')


test_atr()