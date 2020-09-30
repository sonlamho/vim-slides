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
Editor

    • Code editors are great tools for restricting freedom

    • Features include:
        ◦ Yelling at you for syntax errors
        ◦ Yelling at you for stylistic errors
        ◦ Forcing you to document your code by adding
          static types
        ◦ Other features: auto-completion, go to definition,
          go to references

## .py

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
BeepBoop('beeep','').go()

## .py

# Detecting obvious errors

def loopy(n)
    for i in range(n)
        x = i**2
        print(i**2)
    return None

## .py

# Configuring for specific style

def loopy(n):
  for i in range(n):
    print(i**2)
  return None

## .py

##
╔═╗┌┬┐┌─┐┌┬┐┬┌─┐  ┌┬┐┬ ┬┌─┐┬┌┐┌┌─┐
╚═╗ │ ├─┤ │ ││     │ └┬┘├─┘│││││ ┬
╚═╝ ┴ ┴ ┴ ┴ ┴└─┘   ┴  ┴ ┴  ┴┘└┘└─┘

