## .txt

    ╦┌─┐  ┬┌┬┐  ┌─┐┌─┐┌─┐┌─┐┬┌┐ ┬  ┌─┐  ┌┬┐┌─┐  ┬ ┬┌─┐┬  ┬┌─┐
    ║└─┐  │ │   ├─┘│ │└─┐└─┐│├┴┐│  ├┤    │ │ │  ├─┤├─┤└┐┌┘├┤
    ╩└─┘  ┴ ┴   ┴  └─┘└─┘└─┘┴└─┘┴─┘└─┘   ┴ └─┘  ┴ ┴┴ ┴ └┘ └─┘
    ┌┬┐┌─┐┌─┐  ┌┬┐┬ ┬┌─┐┬ ┬  ┌─┐┬─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐┌─┐
     │ │ ││ │  ││││ ││  ├─┤  ├┤ ├┬┘├┤ ├┤  │││ ││││ ┌┘
     ┴ └─┘└─┘  ┴ ┴└─┘└─┘┴ ┴  └  ┴└─└─┘└─┘─┴┘└─┘┴ ┴ o


## .txt

    ╔╦╗┌─┐┌─┐  ┌┬┐┬ ┬┌─┐┬ ┬  ┌─┐┬─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐
     ║ │ ││ │  ││││ ││  ├─┤  ├┤ ├┬┘├┤ ├┤  │││ ││││
     ╩ └─┘└─┘  ┴ ┴└─┘└─┘┴ ┴  └  ┴└─└─┘└─┘─┴┘└─┘┴ ┴

    • Python gives you a lot of freedom

    • That may not be a good thing

    • This talk is about how to restrict your freedom
      when coding in Python

## .txt

    ╔═╗┌┬┐┬┌┬┐┌─┐┬─┐┌─┐
    ║╣  │││ │ │ │├┬┘└─┐
    ╚═╝─┴┘┴ ┴ └─┘┴└─└─┘

    • Code editors are great tools for restricting freedom

    • Features include:
        ◦ Yelling at you for syntax errors
        ◦ Yelling at you for stylistic errors
        ◦ Forcing you to document your code by adding static types,
          and keep the types consistent and updated.
        ◦ Other features: auto-completion, go to definition,
          go to references

## .txt

    ╔═╗┌┬┐┬┌┬┐┌─┐┬─┐┌─┐  ┌─┐┬ ┬┌─┐┬┌─┐┌─┐┌─┐
    ║╣  │││ │ │ │├┬┘└─┐  │  ├─┤│ │││  ├┤ └─┐
    ╚═╝─┴┘┴ ┴ └─┘┴└─└─┘  └─┘┴ ┴└─┘┴└─┘└─┘└─┘

    • Vscode (*)
    • Vim / Neovim (*)
    • Atom
    • (This presentation is in Neovim)

## .txt



        Let's jump right to a demo of how code editors
            can set boundaries for your code

## .py

# DEMO: flake8 - forcing better code style

class BeepBoop:
    def __init__(self,beep,
        boop,
                  ):
      self.beep =beep;self\
              .boop= boop;
      return
    def go(  self):   print(self.\
      beep                               );
BeepBoop('beeeep','').go()

## .py

# DEMO: flake8 - detecting syntax errors

import os
def loopy(n)
    for i in range(n)
        x = i**2
        print(i**2)
        time.sleep(0.5)
    return None

## .py

# DEMO: flake8 - configuring for our own style

def loopy(n):
  for i in range(n):
    print(i**2)
  return None

## .py

# DEMO: mypy - static type checking
from math import log

def log1p(x: float) -> float:
    return log(abs(x) + 1)

log1p(123)
log1p(0.123)
log1p('123')

## .txt

    ╔═╗┌┬┐┌─┐┌┬┐┬┌─┐  ┌┬┐┬ ┬┌─┐┬┌┐┌┌─┐
    ╚═╗ │ ├─┤ │ ││     │ └┬┘├─┘│││││ ┬
    ╚═╝ ┴ ┴ ┴ ┴ ┴└─┘   ┴  ┴ ┴  ┴┘└┘└─┘

    • Type annotations is part of Python syntax since version 3.5

    • Type annotations does not change the code's runtime behavior

    • `mypy` is a separate program that can read your code
      (not running it) and identify type errors (given that
      you annotate correctly.)

## .py

# DEMO: Annotate a function
def func0(x:str, y:str = 'abc') -> int:
    return len(x) + len(y)

func0('some string')    # OK
func0(5678)             # error
func0([1, 2, 3])        # error, runtime ok

reveal_type(func0('some string'))
n = func0('some string') + 1    # OK
m = func0('some string') + '1'  # error

## .py

# DEMO: Annotate a function - bad annotations will cause error
# Exercise: fix these annotations
from math import log

def func0(x: str) -> str:
    return len(x)

def func1(x: int) -> int:
    return log(x + 1)

func1(4.5)

## .txt

    ╔═╗┌┬┐┌─┐┌┬┐┬┌─┐  ┌┬┐┬ ┬┌─┐┬┌┐┌┌─┐
    ╚═╗ │ ├─┤ │ ││     │ └┬┘├─┘│││││ ┬
    ╚═╝ ┴ ┴ ┴ ┴ ┴└─┘   ┴  ┴ ┴  ┴┘└┘└─┘

    • Python primitive types are:
        int, float, str, bool, bytes, None

    • There are also generic types:
        List, Tuple, Dict, Set, ...

## .py

# DEMO: generic types - List
# List[T] : a list of things of type T
from typing import List

def append1(a: List[int]) -> int:
    a.append(1)
    return a[0]

append1([4, 3, 2])          # OK
append1(0.777)              # error
append1(['a', 'b', 'c'])    # error, runtime ok
append1([1.0, 2.0, 3.0])    # error, runtime ok

## .py

# DEMO: generic types - Tuple
# Tuple[T0, T1] : tuple of 2 elements
# Tuple[T0, T1, T2] : tuple of 3 elements
# Tuple[T,...] : tuple of uncertain length
from typing import Tuple

def func2(t: Tuple[int, str]) -> int:
    return t[0]

def func3(t: Tuple[float, ...]) -> int:
    return len(t)

## .py

# DEMO: generic types - Dict
# Dict[KT, VT] : dict with key type KT and value type VT
from typing import Dict, Tuple, List

# Exercise: what's the problem here?
def reinit(d: Dict[str, Tuple[str, float]]) -> List[str]:
    d['Bob'] = ('male', 20)
    d['Alice'] = ('female', '25')
    d['Bob'][1] = 30
    return d.keys()

## .py

# DEMO: DataFrame, Series, ndarray
from pandas import DataFrame, Series

def col_prefixed(df: DataFrame, colname: str) -> Series:
    s = df[colname].copy()
    prefixed_label = 'p_' + colname
    s.name = prefixed_label
    return s


## .py

# DEMO: type-checking follow function calls everywhere
from typing import Dict, Tuple
from math import log

def get_age(d, name):
    gender, age = d[name]
    return age

def get_log_age(d: Dict[str, Tuple[str, float]], name: str
                ) -> float:
    age = get_age(d, name)
    result = log(age)
    return result

## .py

# DEMO: you can type annotate variables too, though often not needed
from typing import Dict

d: Dict[str, float] = {'mark': 10.5, 'peter': 13.4}
reveal_type(d['bob'])

arr = [[0, 1], [12, 13], [24, 25]]
reveal_type(arr[2])
reveal_type(arr[1][1])

## .py

# DEMO: constants: variables that should/must not be changed
# useful for configs
from typing import Sequence, Mapping
from typing_extensions import Final

REPO_NAME: Final[str] = 'jackson'
ADMIN_USERS: Final[Sequence] = ['Chin Chin', 'Shiwen']
POSITION: Final[Mapping] = {'a': 1, 'b': 2, 'c': 3}

# mypy will catch you if you change constants:
REPO_NAME = 'Jeksam'
ADMIN_USERS.append('Son')
POSITION['a'] = 99

## .py

# DEMO: Union types
from typing import Union
import re

def process_ln(x: Union[str, int]) -> int:
    if isinstance(x, int):
        return x
    else:
        match = re.findall(r'^[0-9]+', x)
        if len(match) > 0:
            return int(match[0])
        else:
            return 0

process_ln(123)

## .py

# DEMO: Optional[T] = Union[T, None]
from typing import Optional

def func4(x: Optional[str]) -> str:
    return '' if x is None else x

func4('asdf')       # Ok
func4(None)         # Ok
func4(3.14)         # error

## .txt

    ╔═╗┌┬┐┌─┐┌┬┐┬┌─┐  ┌┬┐┬ ┬┌─┐┬┌┐┌┌─┐
    ╚═╗ │ ├─┤ │ ││     │ └┬┘├─┘│││││ ┬
    ╚═╝ ┴ ┴ ┴ ┴ ┴└─┘   ┴  ┴ ┴  ┴┘└┘└─┘

    • Good type annotations tell you how the function should be used.
    • Type-checking provide mechanism to ensure annotations are correct
    • Successfully type-checked code are cleaner, more readable,
      and better structured
    • Static typing is a big topic:
        ◦ https://mypy.readthedocs.io/en/stable/introduction.html
        ◦ https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python


## .txt




    "Freedom is the enemy of creativity,
     limitations are its saviour"
                            - Someone on the internet


## .txt




    "The enemy of art is the absence of limitations"
                                    - Orson Welles

## .txt




    "Embrace code linting and static type checking"
                                    - Me

