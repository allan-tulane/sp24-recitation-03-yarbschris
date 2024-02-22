from main import *



## Feel free to add your own tests here.
def test_quadratic_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3

    # test with zero
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(10)) == 0*10
    assert quadratic_multiply(BinaryNumber(20), BinaryNumber(0)) == 20*0

    # test with large numbers
    assert quadratic_multiply(BinaryNumber(321), BinaryNumber(654)) == 321*654
    assert quadratic_multiply(BinaryNumber(950), BinaryNumber(999)) == 950*999

    # test with edge cases
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(0)) == 1*0
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0*0