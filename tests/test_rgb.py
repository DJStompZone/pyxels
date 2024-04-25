import pytest

from pyxels.rgb import RGB


def test_from_hex():
    rgb = RGB.from_hex("#FF0000")
    assert rgb.red == 255
    assert rgb.green == 0
    assert rgb.blue == 0


def test_to_hex():
    rgb = RGB(255, 0, 0)
    assert rgb.to_hex() == "#ff0000"


def test_add():
    rgb1 = RGB(255, 0, 0)
    rgb2 = RGB(0, 255, 0)
    result = rgb1 + rgb2
    assert result.red == 255
    assert result.green == 255
    assert result.blue == 0


def test_sub():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(0, 255, 0)
    result = rgb1 - rgb2
    assert result.red == 255
    assert result.green == 0
    assert result.blue == 255


def test_mul():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(0, 255, 0)
    result = rgb1 * rgb2
    assert result.red == 0
    assert result.green == 255
    assert result.blue == 0


def test_truediv():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(1, 255, 1)
    result = rgb1 / rgb2
    assert result.red == 255
    assert result.green == 1
    assert result.blue == 255


def test_floordiv():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(1, 255, 1)
    result = rgb1 // rgb2
    assert result.red == 255
    assert result.green == 1
    assert result.blue == 255


def test_mod():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(1, 255, 1)
    result = rgb1 % rgb2
    assert result.red == 0
    assert result.green == 0
    assert result.blue == 0


def test_truediv_zero_division():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(0, 255, 0)
    with pytest.raises(ZeroDivisionError):
        _ = rgb1 / rgb2


def test_floordiv_zero_division():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(0, 255, 0)
    with pytest.raises(ZeroDivisionError):
        _ = rgb1 // rgb2


def test_mod_zero_division():
    rgb1 = RGB(255, 255, 255)
    rgb2 = RGB(0, 255, 0)
    with pytest.raises(ZeroDivisionError):
        _ = rgb1 % rgb2


def test_bitwise_and():
    rgb1 = RGB(250, 128, 64)
    rgb2 = RGB(15, 64, 128)
    result = rgb1 & rgb2
    assert result == RGB(250 & 15, 128 & 64, 64 & 128)


def test_bitwise_or():
    rgb1 = RGB(250, 128, 64)
    rgb2 = RGB(15, 64, 128)
    result = rgb1 | rgb2
    assert result == RGB(250 | 15, 128 | 64, 64 | 128)


def test_bitwise_xor():
    rgb1 = RGB(250, 128, 64)
    rgb2 = RGB(15, 64, 128)
    result = rgb1 ^ rgb2
    assert result == RGB(250 ^ 15, 128 ^ 64, 64 ^ 128)


def test_bitwise_invert():
    rgb = RGB(250, 128, 64)
    result = ~rgb
    assert result == RGB(~250 & 0xFF, ~128 & 0xFF, ~64 & 0xFF)


def test_set_lsb():
    rgb = RGB(254, 127, 63)
    bits = RGB(1, 0, 1)
    result = rgb.set_lsb(bits)
    assert result == RGB(255, 126, 63)


def test_get_lsb():
    rgb = RGB(255, 126, 63)
    result = rgb.get_lsb()
    assert result == RGB(1, 0, 1)


def test_blend():
    rgb1 = RGB(100, 100, 100)
    rgb2 = RGB(200, 200, 200)
    result = rgb1.blend(rgb2, 0.5)
    assert result == RGB(150, 150, 150)


def test_to_grayscale():
    rgb = RGB(255, 0, 0)
    result = rgb.to_grayscale()
    # Using weights: R=0.299, G=0.587, B=0.114
    grayscale_value = int(0.299 * 255)
    assert result == RGB(grayscale_value, grayscale_value, grayscale_value)


def test_distance():
    rgb1 = RGB(0, 0, 0)
    rgb2 = RGB(255, 255, 255)
    result = rgb1.distance(rgb2)
    expected_distance = ((255**2) * 3) ** 0.5
    assert result == expected_distance


def test_lighten():
    rgb = RGB(100, 100, 100)
    result = rgb.lighten(10)
    assert result == RGB(110, 110, 110)


def test_darken():
    rgb = RGB(100, 100, 100)
    result = rgb.darken(10)
    assert result == RGB(90, 90, 90)


def test_clamping_high_values():
    rgb = RGB(300, 300, 300)
    assert rgb == RGB(255, 255, 255)


def test_clamping_low_values():
    rgb = RGB(-10, -10, -10)
    assert rgb == RGB(0, 0, 0)


def test_blend_with_factor_greater_than_one():
    rgb1 = RGB(100, 100, 100)
    rgb2 = RGB(200, 200, 200)
    result = rgb1.blend(rgb2, 1.5)
    assert result == RGB(200, 200, 200)


def test_blend_with_negative_factor():
    rgb1 = RGB(100, 100, 100)
    rgb2 = RGB(200, 200, 200)
    result = rgb1.blend(rgb2, -0.5)
    assert result == RGB(100, 100, 100)


def test_invalid_hex_length():
    with pytest.raises(ValueError):
        RGB.from_hex("#FF")


def test_invalid_hex_characters():
    with pytest.raises(ValueError):
        RGB.from_hex("#GGGGGG")


def test_lighten_beyond_bounds():
    rgb = RGB(250, 250, 250)
    result = rgb.lighten(10)
    assert result == RGB(255, 255, 255)


def test_darken_beyond_bounds():
    rgb = RGB(5, 5, 5)
    result = rgb.darken(10)
    assert result == RGB(0, 0, 0)


def test_set_lsb_with_various_patterns():
    rgb = RGB(254, 254, 254)
    patterns = [(1, 0, 1), (0, 1, 0), (1, 1, 1), (0, 0, 0)]
    for red_lsb, green_lsb, blue_lsb in patterns:
        bits = RGB(red_lsb, green_lsb, blue_lsb)
        result = rgb.set_lsb(bits)
        assert result == RGB(254 | red_lsb, 254 | green_lsb, 254 | blue_lsb)


def test_get_lsb_for_all_possibilities():
    for i in range(256):
        rgb = RGB(i, i, i)
        result = rgb.get_lsb()
        assert result == RGB(i & 1, i & 1, i & 1)


def test_distance_with_known_values():
    rgb1 = RGB(0, 0, 0)
    rgb2 = RGB(0, 0, 255)
    result = rgb1.distance(rgb2)
    assert result == 255
