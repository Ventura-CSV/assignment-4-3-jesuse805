def main():
    x = int(input('Enter your input: '))
    result = []
    
    while x > 0:
        remainder = x % 2
        result.append(remainder)
        x = x // 2
        
    #result.reverse()
    
    print(' '.join(map(str, result)))
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
