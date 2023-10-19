from inspect import getmembers, isfunction, signature
from typing import Dict, Any, Callable, List


def collect_handlers_functions(module) -> Dict[Any, Callable | List[Callable]]:
    functions = {}  # type: Dict[Any, Callable| List[Callable]]
    for p, c in getmembers(module, isfunction):
        for name, model_type in signature(c).parameters.items():
            if name == "command":
                functions.update({model_type.annotation: c})
                break

            if name == "message":
                functions.setdefault(model_type.annotation, []).append(c)
                break

    return functions
