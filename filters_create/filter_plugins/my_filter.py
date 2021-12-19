def some_filter(my_string):
    return my_string.upper()


class FilterModule:
    def filters(self):
        return {"some_filter": some_filter}
