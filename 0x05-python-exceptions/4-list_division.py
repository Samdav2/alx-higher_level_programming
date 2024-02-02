#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            map(lambda x, y: x / y, my_list_1[i], my_list_2[i])
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        else:
            new_list = list(map(lambda x, y: x / y, my_list[i], my_list_2[i]))
        finally:
            return new_list
