class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def __getattr__(self, item):
    #     if

dict_1 = {
    'names': {
        'Ivan': [],
        'Nikita': []
    }
}



my_dict = MyDict(dict_1)
# print(my_dict.names.Ivan)
print(my_dict.__dict__)
# print(my_dict.names.Ivan)