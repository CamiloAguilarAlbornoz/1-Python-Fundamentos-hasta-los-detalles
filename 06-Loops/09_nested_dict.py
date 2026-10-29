nested_dict = {
    'person_one': {
        'name': 'Carolina Rodriguez',
        'age': 27,
        'city': 'Cali - Tunja'
    },
    'person_two': {
        'name': 'Dayana Moreno',
        'age': 29,
        'city': 'Tunja'
    },
    'person_three': {
        'name': 'Mayerly Rivera',
        'age': 27,
        'city': 'Tunja'
    },
    'person_four': {
        'name': 'Silvana Nieto',
        'age': 28,
        'city': 'Simijaca - Bogotá'
    }
}

for key, value in nested_dict.items():
    print(f'\n{key}: ')
    for sub_key, sub_value in value.items():
        print(f'{sub_key}: {sub_value}', end=' ')
    print()
print()