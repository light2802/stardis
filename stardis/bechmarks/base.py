import inspect


def dump_args(args_dict = None):
    if not args_dict:
        return
    # Get function name
    f_name = inspect.stack()[1].function
    # Get function args
    f_args = inspect.getargvalues(inspect.stack()[1].frame).locals
    # Remove unwanted args
    f_args.pop("args_dict")
    args_dict[f_name] = f_args