from uapi import UapiClient

def test_smoke():
    c = UapiClient("https://uapis.cn")
    assert hasattr(c, "clipzy_zai_xian_jian_tie_ban")
