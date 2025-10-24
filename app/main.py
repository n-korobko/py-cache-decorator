from typing import Callable, Any

_function_caches = {}


def cache(func: Callable) -> Callable[..., Any]:
    _function_caches[func] = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in _function_caches[func]:
            print("Getting from cache")
            return _function_caches[func][key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            _function_caches[func][key] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulo: int) -> int:
    return (base ** exponent ** modulo) % (base * modulo)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
