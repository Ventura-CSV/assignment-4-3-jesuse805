def main():
    number = int(input('Enter your input: '))
    result = []
    
    while number > 0:
        remainder = number % 2
        result.append(remainder)
        number = number // 2
        
    
        

    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
