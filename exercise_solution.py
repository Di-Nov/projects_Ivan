class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

dict_1 = {
    'names': {
        'Ivan': [],
        'Nikita': []
    }
}

my_dict = MyDict(dict_1)
print(my_dict)
print(my_dict.__dict__)