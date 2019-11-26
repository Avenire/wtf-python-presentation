from goose_typing.set_theme_v3 import set_theme


# ...where is your God now set_theme_v3?
def test_virtual_abstract_class():
    # YOLO
    from collections import Mapping
    @Mapping.register
    class TotallyNotADict:
        pass

    assert set_theme(TotallyNotADict())


# But, for real:
def test_abc_type_is_a_lie_in_python():
    # YOLO
    from collections import Mapping
    class TotallyNotAMapping:
        pass
    Mapping.register(TotallyNotAMapping)
    assert isinstance(TotallyNotAMapping(), Mapping)
