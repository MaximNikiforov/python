def divine_path(full_path: str):
    def divine(abs_path: str, div: str) -> tuple:
        abs_path = abs_path.split(div)
        file_name, extension = abs_path[-1].split('.')
        path = div.join(abs_path[:-1])
        return path, file_name, extension

    return divine(full_path, '/') if '/' in full_path else divine(full_path, '\\')


print(divine_path('C:/Users/Xiaomi/Documents/GitHub/python/2.py'))
