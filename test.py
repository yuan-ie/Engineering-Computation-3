# Test area for Yuan
# Test for matrix multiplication and dot product

from lalib.MyMatrix import MyMatrix
from lalib.operations import dot
import argparse

def argprse():
    parser = argparse.ArgumentParser(description="choose test case 1 to 7")
    parser.add_argument('case', type=int, choices=[1,2,3,4,5,6,7,8,9,10,11,12,13], help="an integer between 1 to 6")

    args = parser.parse_args()
    return args.case

def case_1():
	# matrix size 2x3
    a = MyMatrix([[1,2,3],
            		[4,5,6]])
    # matrix size 3x2
    b = MyMatrix([[1,4],
            		[2,5],
            		[3,6]])
    c = a*b

def case_2():
	# matrix size 3x5
    a = MyMatrix([[6,23,5,76,23],
            		[9,12,8,6,87],
                    [5,34,21,56,3]])
    # matrix size 5x3
    b = MyMatrix([[1,1,1],

            		[2,1,2],
            		[3,3,1],
                    [1,4,4],
                    [5,1,5]])
    c = a*b # [[258, 371, 476], [498, 156, 500], [207, 329, 333]]
    # dot(a,b)
    
def case_3():
	# matrix size 3x5
    a = MyMatrix([[6,23,5,-76,23],
            		[9,12,-8,6,87],
                    [5,-34,21,56,-3]])
    # matrix size 5x3
    b = MyMatrix([[1,-1,1],

            		[-2,2,2],
            		[3,3,-3],
                    [-4,4,4],
                    [5,-5,5]])
    c = a*b #[[394, -364, -152], [372, -420, 516], [-103, 229, 83]]
    
def case_4():
	# matrix size 2x3
    a = MyMatrix([1,2,3])
    b = 6
    c = a*b
    
    
def case_5():
	# matrix size 1x3
    a = MyMatrix([1,2,3])

    # matrix size 3x2
    b = MyMatrix([[1,1],
            		[2,2],
            		[3,3]])
    c = a*b
    # dot(a,b)

def case_6():
	# matrix size 1x3
    a = MyMatrix([1,2,3])

    # matrix size 3x1
    b = MyMatrix([[4],
            		[5],
            		[6]])
    c = a*b
    # dot(a,b) # 32


def case_7():
     # matrix size 3x1
    a = MyMatrix([[4],
            		[5],
            		[6]])
    
    # matrix size 1x3
    b = MyMatrix([1,2,3])
    c = a*b
    # dot(a,b)

def case_8():
     # matrix size 3x1
    a = MyMatrix([[4],
            		[5],
            		[6]])
    
    # matrix size 1x3
    b = MyMatrix([[4],
            		[5],
            		[6]])
    c = a*b
    # dot(a,b) # 77

def case_9():
	# matrix size 1x3
    a = MyMatrix([1,2,3])

    # matrix size 3x1
    b = MyMatrix([1,2,3])
    c = a*b
    # dot(a,b) # 14

def case_10():
     # matrix size 3x1
    a = MyMatrix([[4],
            		[5],
            		[6]])
    
    # matrix size 1x3
    b = MyMatrix([1,2,3,4])
    c = a*b
    # dot(a,b)

def case_11():
     # matrix size 3x1
    a = MyMatrix([[4],
            		[5],
            		[6]])
    
    # matrix size 1x3
    b = "s"
    c = a*b
    # dot(a,b)

def main():
    case = argprse()
    
    # test out different cases for the dot product module
    if case == 1:
        case_1()
    if case == 2:
        case_2()
    if case == 3:
        case_3()
    if case == 4:
        case_4()
    if case == 5:
        case_5()
    if case == 6:
        case_6()
    if case == 7:
        case_7()
    if case == 8:
        case_8()
    if case == 9:
        case_9()
    if case == 10:
        case_10()
    if case == 11:
        case_11()
main()
