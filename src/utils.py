from typing import Tuple


coef_by_type = {
        1: 1.2,
        2: 1.38,
        3: 1.46,
        4: 1.55,
        5: 1.64,
        6: 1.73,
        7: 1.9,
    }
coef_by_gender = {
    'Male': 5,
    'Female': -161
}

categories = [
    ('Скуф', 'Человек с лишним весом, возраст от 39 лет'),
    ('Масик', 'Накаченный, спортивный, молодой-взрослый'),
    ('Тюбик', 'Худой, мямля, молодой-взрослый'),
    ('Штрих', 'Спортивный, молодой-взрослый')
]


def calculate_calorie_standard(
        gender: str,
        height: int,
        weight: int,
        age: int,
        physical_activity_type: int
) -> float:
    return (weight * 10 + height * 6.25 - age * 5 + coef_by_gender[gender]) * coef_by_type[physical_activity_type]


def get_category(
        height: int,
        weight: int,
        age: int,
        physical_activity_type: int
) -> Tuple[str, str]:
    imt = weight / (height * height)

    if age > 40 or imt > 22:
        return categories[0]
    if imt <= 18.5:
        return categories[2]
    if physical_activity_type >= 3:
        return categories[1]
    return categories[3]
