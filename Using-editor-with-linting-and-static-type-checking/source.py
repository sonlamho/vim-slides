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
      beep\
                                      );
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

def func0(s: str):
    return s + '.csv'

func0(123)

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

## .txt

    STORY OF INVENTION OF MANNED FLIGHTS

  • Another group attempted manned flights: led by
    Samuel Pierpont Langley. They are well funded, with the
    U.S. defense department and the Smithsonian is support.

## .txt

    STORY OF INVENTION OF MANNED FLIGHTS

  • Another group attempted manned flights: led by
    Samuel Pierpont Langley. They are well funded, with the
    U.S. defense department and the Smithsonian is support.
      ◦ The result... to quote a congressman:
        "You tell Langley for me ... that the only thing he
        ever made fly was Government money."

## .txt

    STORY OF INVENTION OF MANNED FLIGHTS

  • Another group attempted manned flights: led by
    Samuel Pierpont Langley. They are well funded, with the
    U.S. defense department and the Smithsonian is support.
      ◦ The result... to quote a congressman:
        "You tell Langley for me ... that the only thing he
        ever made fly was Government money."

  • The Wright brothers: 4 years of experimentations, funded
    by their own bicycle shop, created controllable aircrafts
    that can take off and land - ultimately led to the modern
    day airplanes.

# .txt


    

    "Freedom is the enemy of creativity,
    limitations are its saviour"
                                - Someone on the internet


# .txt




    "The enemy of art is the absence of limitations"
                                    - Orson Welles

# .txt


    

    "Embrace code linting and static type checking"
                                    - Me

