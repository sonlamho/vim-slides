## .txt

     ______                            _
    |  ____|                          | |
    | |__     _ __    ___    ___    __| |   ___    _ __ ___
    |  __|   | '__|  / _ \  / _ \  / _` |  / _ \  | '_ ` _ \
    | |      | |    |  __/ |  __/ | (_| | | (_) | | | | | | |
    |_|      |_|     \___|  \___|  \__,_|  \___/  |_| |_| |_|

## .txt

    ╔╦╗┌─┐┌─┐  ┌┬┐┬ ┬┌─┐┬ ┬  ┌─┐┬─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐┌─┐
     ║ │ ││ │  ││││ ││  ├─┤  ├┤ ├┬┘├┤ ├┤  │││ ││││ ┌┘
     ╩ └─┘└─┘  ┴ ┴└─┘└─┘┴ ┴  └  ┴└─└─┘└─┘─┴┘└─┘┴ ┴ o

    • Python gives you a lot of freedom

    • That may not be a good thing

    • This talk is about how to restrict your freedom

## .txt

    ╔═╗┌┬┐┬┌┬┐┌─┐┬─┐┌─┐
    ║╣  │││ │ │ │├┬┘└─┐
    ╚═╝─┴┘┴ ┴ └─┘┴└─└─┘

    • Code editors are great tools for restricting freedom

    • Features include:
        ◦ Yelling at you for syntax errors
        ◦ Yelling at you for stylistic errors
        ◦ Forcing you to document your code by adding
          static types
        ◦ Other features: auto-completion, go to definition,
          go to references

## .txt

    ╔═╗┌┬┐┬┌┬┐┌─┐┬─┐┌─┐  ┌─┐┬ ┬┌─┐┬┌─┐┌─┐┌─┐
    ║╣  │││ │ │ │├┬┘└─┐  │  ├─┤│ │││  ├┤ └─┐
    ╚═╝─┴┘┴ ┴ └─┘┴└─└─┘  └─┘┴ ┴└─┘┴└─┘└─┘└─┘

    • Vscode
    • atom
    • vim / neovim
    • (This presentation is in neovim)

## .py

# DEMO
# Forcing better code style

class BeepBoop:
    def __init__(self,beep,
        boop,
                  ):
      self.beep =beep;self\
              .boop= boop;
      return
    def go(  self):   print(self.\
      beep\                               );
BeepBoop('beeeep','').go()

## .py

# DEMO
# Detecting obvious errors

import os
def loopy(n)
    for i in range(n)
        x = i**2
        print(i**2)
        time.sleep(0.5)
    return None

## .py

# DEMO
#Configuring for specific style

def loopy(n):
  for i in range(n):
    print(i**2)
  return None

## .py

# DEMO
# Static type checking
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

    • Type annotations is part of Python syntax
      since version 3.5
  
    • Type annotations does not change the code's
      runtime behavior
  
    • `mypy` is a separate program that can read
      your code (not running it) and identify type
      errors (given that you annotate correctly.)

## .py

# DEMO: Annotate a function
def func0(x: str) -> int:
    return len(x)

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

# DEMO: type-checking follow imports
from slide_0 import func0

func0(123)
func0('abc')
reveal_type(func0('abc'))


## .txt

    ╔═╗┌┬┐┌─┐┌┬┐┬┌─┐  ┌┬┐┬ ┬┌─┐┬┌┐┌┌─┐
    ╚═╗ │ ├─┤ │ ││     │ └┬┘├─┘│││││ ┬
    ╚═╝ ┴ ┴ ┴ ┴ ┴└─┘   ┴  ┴ ┴  ┴┘└┘└─┘

    • Type annotations can serve as documentations,
      it's "self documenting code"

    • Successfully type-checked code are cleaner, more
      readable, and better structured


## .txt

    STORY OF INVENTION OF MANNED FLIGHTS

    • Beside the Wrights brothers, another group attempted manned
      flights: led by Samuel Pierpont Langley. They are very
      well funded, by the U.S. war department and the Smithsonian

## .txt

    STORY OF INVENTION OF MANNED FLIGHTS

    • Beside the Wrights brothers, another group attempted manned
      flights: led by Samuel Pierpont Langley. They are very
      well funded, by the U.S. war department and the Smithsonian
        ◦ The result... to quote a congressman:
          "You tell Langley for me ... that the only thing he
          ever made fly was Government money."

## .txt

    STORY OF INVENTION OF MANNED FLIGHTS

    • Beside the Wrights brothers, another group attempted manned
      flights: led by Samuel Pierpont Langley. They are very
      well funded, by the U.S. war department and the Smithsonian
        ◦ The result... to quote a congressman:
          "You tell Langley for me ... that the only thing he
          ever made fly was Government money."
  
    • The Wright brothers: 4 years of experimentations, funded
      by their own bicycle shop, created controllable aircrafts
      that can take off and land - ultimately led to the modern
      day airplanes.

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

##
