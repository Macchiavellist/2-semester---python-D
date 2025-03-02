import re


def match_a_b(text):
    return bool(re.fullmatch(r"ab*", text))


def match_a_b_2_3(text):
    return bool(re.fullmatch(r"ab{2,3}", text))


def find_lowercase_underscore(text):
    return re.findall(r"[a-z]+_[a-z]+", text)


def find_upper_lower(text):
    return re.findall(r"[A-Z][a-z]+", text)

def match_a_anything_b(text):
    return bool(re.fullmatch(r"a.*b", text))


def replace_with_colon(text):
    return re.sub(r"[ ,.]", ":", text)


def snake_to_camel(text):
    words = text.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


def split_at_uppercase(text):
    return re.split(r"(?=[A-Z])", text)


def insert_spaces_capital(text):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", text)


def camel_to_snake(text):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", text).lower()

# --- Тестирование функций ---
if __name__ == "__main__":
    print(match_a_b("ab"))
    print(match_a_b_2_3("abb"))
    print(find_lowercase_underscore("hello_world test_case"))
    print(find_upper_lower("Hello World ThisIsTest"))
    print(match_a_anything_b("acb"))     # True
    print(replace_with_colon("Hello, World. Python"))
    print(snake_to_camel("snake_case_example"))
    print(split_at_uppercase("SplitAtUppercase"))
    print(insert_spaces_capital("InsertSpacesBetweenWords"))
    print(camel_to_snake("CamelCaseExample"))