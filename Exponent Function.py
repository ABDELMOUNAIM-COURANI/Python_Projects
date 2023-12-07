def raise_to_pow (basenum, pownum):
    result = 1
    for index in range(pownum):
        result = result * basenum 
    return result
    
print (raise_to_pow(9,7))