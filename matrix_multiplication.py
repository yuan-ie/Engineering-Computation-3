def __mul__(self, arg: Union[MyMatrix, float]) -> MyMatrix:
    """performs multiplication via operator overloading. Both operands must be of type MyMatrix OR first operand must be of type MyMatrix, and second must be int or float

    Args:
        arg (Union[MyMatrix, float]): Object of type MyMatrix, or int/float

    Raises:
        Exception: Cannot multiply Vector and Matrix; Both must be Vector or both must be Matrix
        Exception: Vectors/Matrices must have same dimensions but flipped.
        Exception: Constant must be float or int
    Returns:
        MyMatrix: _description_
    """        
    
    # Avoids circular imports
    from .operations import dot
    
    def mul_scalar():
        '''performs multiplication of vector/matrix to scalar'''
        
        if self.isRow == True:
            # initialize empty vector
            result = [None for _ in range(self.cols)]
            for i in range(self.cols):
                result[i] = self.mat[i] * arg
        else:
            # initialize empty vector
            result = [[None for _ in range(self.cols)] for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] = self.mat[i][j] * arg
        return MyMatrix(result)

    def mul_vector():
        '''performs multiplication of matrices with size 1 col or size 1 row'''
        # go through each row
        for i in range(self.rows):
            # go to next column in same row
            for k in range(arg.cols):
                # initialize the product to 0
                prod = 0
                # go through each element in column
                for j in range(arg.rows):
                    # if the first vector is a row vector (row vector * col vector) -> returns scalar
                    if self.isRow == True: 
                        prod = prod + (self.mat[j] * arg.mat[j][k])
                    # if the second vector is a row vector (col vector * row vector) -> returns matrix
                    else:
                        prod = prod + (self.mat[i][j] * arg.mat[k])
                # store the product sum into the corresponding place in the result matrix
                result[i][k] = prod
        if self.isRow == True:
            return result[0][0]
        else: 
            return MyMatrix(result)

    def mul_matrix():
        '''performs multiplication of matrices'''

        # go through each row
        for i in range(self.rows):
            # go to next column in same row
            for k in range(arg.cols):
                # initialize the result to 0
                prod = 0
                # go through each element in column
                for j in range(arg.rows):
                    prod = prod + (self.mat[i][j] * arg.mat[j][k])
                # store the product sum into the corresponding place in the result matrix
                result[i][k] = prod
        return MyMatrix(result)
    
    # check if it is matrix multiplication or matrix times a scalar
    # else if the first argument is a matrix of any size (that is not 1xn or nx1)
    if self.isMat == True or self.isArr == True:
        try:
            # if second argument is not a matrix, but a scalar, multiply scalar to matrix
            if isinstance(arg, Union[float,int]):
                return mul_scalar()
            # if the second argument is a matrix, perform matrix multiplication
            elif ((arg.isMat == True) or (arg.isArr == True)) and (self.rows==arg.cols) and (self.cols==arg.rows):
                result = [[None for _ in range(arg.cols)] for _ in range(self.rows)]
                # if the matrices are vectors, perform matrix multiplication with specific conditions
                if (self.isCol == True and arg.isRow == True) or (self.isRow == True and arg.isCol == True):
                    return mul_vector()
                # otherwise perform regular matrix multiplication
                else:
                    return mul_matrix()
        # raise an error if the matrices are types other than MyMatrix, int, or float
        #elif isinstance(arg, (MyMatrix, int, float)) is False:
        except:
            raise LaLibError("Input is neither a matrix or an int/float.")
        # raise an error if the matrices do not have same dimension
        else:
            raise LaLibError("Matrices do not have the correct dimensions in order of [N,M] and [M,N].")
