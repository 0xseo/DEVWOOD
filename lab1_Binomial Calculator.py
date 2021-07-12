A = input("Enter the command: ").strip()
value = {}

while A.lower() != 'quit':

    # if the command was 'def'
    if A[0:4] == 'def ':
        A = A.replace('def', '').lstrip()

        # if there are more than one '=' in var name
        if A.count('=') != 1:
            print('Error : invalid input format')
            A = input("Enter the command: ").strip()
            continue

        else:
            var = A[0:A.index('=')].rstrip()

            # if the var name is incorrect
            if ('+' in var) or ('-' in var) or ('*' in var) or ('/' in var) or var.isdigit():
                print('Error : invalid variable name')
                A = input("Enter the command: ").strip()
                continue

            else:
                A = A.replace(var, '')
                A = A.replace('=', '').strip()

                # if there is any character in operand
                if not A.isdigit():
                    print('Error : invalid number')
                    A = input("Enter the command: ").strip()
                    continue

                else:
                    num = int(A)
                    # add var and num in value dictionary
                    value[var] = num
                    A = input("Enter the command: ").strip()
                    continue

    # if the command was 'calc'
    elif A[0:5] == 'calc ':
        A = A.replace('calc', '').lstrip()
        # if there are more than one operator
        cnt = 0
        for i in ['+', '-', '*', '/']:
            if i in A:
                cnt += 1
        if cnt != 1:
            print('Error : too much operator')
            A = input("Enter the command: ").strip()
            continue

        else:
            # if the operator was '+'
            if '+' in A:
                # split num1 and num2
                num1 = A[0:A.index('+')].strip()
                num2 = A[A.index('+') + 1:].strip()

                # check if each num is digit or variable name
                # check if input variable was defined
                if num1.isdigit():
                    if num2.isdigit():
                        result = int(num1) + int(num2)
                    else:
                        if num2 in value.keys():
                            result = int(num1) + value[num2]
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue
                else:
                    if num2.isdigit():
                        if num1 in value.keys():
                            result = value[num1] + int(num2)
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue
                    else:
                        if num1 in value.keys() and num2 in value.keys():
                            result = value[num1] + value[num2]
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue

            # if the operator was '-'
            elif '-' in A:
                # split num1 and num2
                num1 = A[0:A.index('-')].strip()
                num2 = A[A.index('-') + 1:].strip()

                # check if each num is digit or variable name
                # check if input variable was defined
                if num1.isdigit():
                    if num2.isdigit():
                        result = int(num1) - int(num2)
                    else:
                        if num2 in value.keys():
                            result = int(num1) - value[num2]
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue
                else:
                    if num2.isdigit():
                        if num1 in value.keys():
                            result = value[num1] - int(num2)
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue
                    else:
                        if num1 in value.keys() and num2 in value.keys():
                            result = value[num1] - value[num2]
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue

            # if the operator was '*'
            elif '*' in A:
                # split num1 and num2
                num1 = A[0:A.index('*')].strip()
                num2 = A[A.index('*') + 1:].strip()

                # check if each num is digit or variable name
                # check if input variable was defined
                if num1.isdigit():
                    if num2.isdigit():
                        result = int(num1) * int(num2)
                    else:
                        if num2 in value.keys():
                            result = int(num1) * value[num2]
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue
                else:
                    if num2.isdigit():
                        if num1 in value.keys():
                            result = value[num1] * int(num2)
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue
                    else:
                        if num1 in value.keys() and num2 in value.keys():
                            result = value[num1] * value[num2]
                        else:
                            print("Error : undefined variable")
                            A = input("Enter the command: ").strip()
                            continue

            # if the operator was '/'
            elif '/' in A:
                # split num1 and num2
                num1 = A[0:A.index('/')].strip()
                num2 = A[A.index('/') + 1:].strip()

                try:
                    # check if each num is digit or variable name
                    # check if input variable was defined
                    if num1.isdigit():
                        if num2.isdigit():
                            result = int(num1) / int(num2)
                        else:
                            if num2 in value.keys():
                                result = int(num1) / value[num2]
                            else:
                                print("Error : undefined variable")
                                A = input("Enter the command: ").strip()
                                continue
                    else:
                        if num2.isdigit():
                            if num1 in value.keys():
                                result = value[num1] / int(num2)
                            else:
                                print("Error : undefined variable")
                                A = input("Enter the command: ").strip()
                                continue
                        else:
                            if num1 in value.keys() and num2 in value.keys():
                                result = value[num1] / value[num2]
                            else:
                                print("Error : undefined variable")
                                A = input("Enter the command: ").strip()
                                continue

                # exception handling for ZeroDivisionError
                except ZeroDivisionError:
                    print("Error : division by zero")
                    A = input("Enter the command: ").strip()
                    continue

            print(result)
            A = input("Enter the command: ").strip()
            continue

    # if the command was 'see'
    elif 'see' in A:
        print("=" * 20)
        for i in value.keys():
            print(i, ":", value[i])
        print("=" * 20)
        A = input("Enter the command: ").strip()
        continue

    # if the command was undefined
    else:
        print('undefined')
        A = input("Enter the command: ").strip()
        continue
