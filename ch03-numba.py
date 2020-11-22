def timing(f):
    @wraps(f):
    def wraps(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kwargs}] took: {te-ts} sec)")
        return result
    return wrap
