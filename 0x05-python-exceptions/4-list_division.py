#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_3 = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            list_3.append(quotient)
    return list_3
