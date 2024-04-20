def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please give me name and coorect phone (10 digit)."
        except KeyError:
            return "Give me correct name"
        except IndexError:
            return "Give me correct index"
    return inner