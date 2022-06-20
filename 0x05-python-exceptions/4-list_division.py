#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_n = []
    for idx in range(list_length):
        try:
            div = 0
            div = (my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            list_n.append(div)
    return list_n
