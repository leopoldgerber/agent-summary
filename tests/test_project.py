def test_project_packages_can_be_imported() -> None:
    import agents
    import app

    assert agents is not None
    assert app is not None
