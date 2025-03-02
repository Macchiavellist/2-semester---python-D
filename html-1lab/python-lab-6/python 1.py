from module import multiply_list, delayed_sqrt, count_case, is_palindrome, all_true

# Тестирование функций
print(multiply_list([1, 2, 3, 4, 5]))  # 120
print(count_case("Hello World!"))      # (2, 8)
print(is_palindrome("madam"))          # True
print(delayed_sqrt(25100, 2123))       # 158.42979517754858
print(all_true((True, True, False)))   # False