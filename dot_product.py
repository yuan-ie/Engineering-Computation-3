def dot(arg1: MyMatrix, arg2: MyMatrix) -> float:
    '''
    Args:
            arg1 (MyMatrix): Object of type MyMatrix
            arg2 (MyMatrix): Object of type MyMatrix

        Raises:
            Exception: dot product between only two vectors of equal length
            Exception: dot product between column vector and row vector (in this order) returns matrix
            Exception: dot product between row vector and column vector (in this order) returns scalar
        Returns:
            Matrix (type MyMatrix) or scalar
    '''
    
    def dot_product(vec1: MyMatrix, vec2: MyMatrix):
        '''performs dot product of vectors'''

        # initialize result to 0
        result = 0
        # go through each column
        for j in range(vec1.cols):
            result = result + (vec1.mat[j] * vec2.mat[j])
        return result
        
    def flip_vector():
        tmpVec1 = arg1
        tmpVec2 = arg2
         # if the first vector is a nx1 vector, flip the vector
        if arg1.rows != 1:
            flipped1 = [None for _ in range(arg1.rows)]
            for y in range(arg1.rows):
                flipped1[y] = arg1[y,0]
            tmpVec1 = MyMatrix(flipped1)
        # if the second vector is a nx1 vector, flip the vector
        if arg2.rows != 1:
            flipped2 = [None for _ in range(arg2.rows)]
            for x in range(arg2.rows):
                flipped2[x] = arg2[x,0]
            tmpVec2 = MyMatrix(flipped2)
        result = dot_product(tmpVec1,tmpVec2)
        return result
    
    
    # if one of the inputs are not MyMatrix type, raise an error
    if (isinstance(arg1, MyMatrix) is False) or (isinstance(arg2, MyMatrix) is False):
        raise LaLibError("One of the inputs is not a MyMatrix type.")
    # if both are MyMatrix type and are vectors, perform dot product
    elif (arg1.isArr == True) and (arg2.isArr == True):
        if ((arg1.rows==arg2.cols) and (arg1.cols==arg2.rows)) or ((arg1.rows==arg2.rows) and (arg1.cols==arg2.cols)):
            # check if vector needs to be flipped
            return flip_vector()
        else:
            raise LaLibError("Vectors do not have the same dimension.")
    # return any statement when dot product cannot be done
    elif (arg1.isArr == False):
        raise LaLibError("Cannot perform dot product. First operand is not a vector.")
    elif (arg2.isArr == False):
        raise LaLibError("Cannot perform dot product. Second operand is not a vector.")
