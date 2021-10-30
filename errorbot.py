"""

ErrorBot found at https://github.com/robempire
----------------------------------------------

Basic Usage:
    
> bot = ErrorBot()
> empty_list = []
> for i in range(1,5):     
>    print (f'Pass #{i}') 
>    try:
>        make_error = empty_list[1]
>    except:
>        bot.check(3)

[Out]: Pass #1
[Out]: Pass #2
[Out]: Pass #3

[Out]: ERRORBOT: That's 3 errors since ERRORBOT was created ... Continue? (y/n) 

> Y
[Out]: Pass #4

Supported arguments:
    
    kill=True:  Exits program without promptimg
    throw=True: Raises a UserWarning exception
    ask=True:   Prompts for [Y/N] input before continuing execution (Default: True)
    reset=True: Resets error counter to 0 after error tolerance reached (Default: True)

"""

import sys

class ErrorBot:
    
    def __init__(self):
        
        self.errors = 0
        
    def check(self, tolerance, ask=True, kill=False, throw=False, reset=True, ):
        
        self.errors += 1
        
        if self.errors >= tolerance:
            if reset:
                    self.errors = 0
            if throw:

                raise UserWarning('ERRORBOT: Quitting after {self.errors} errors.')
                
            if kill:

                print ('ERRORBOT: Quitting after {self.errors} errors...')
                sys.exit()
            
            if ask:
                
                goahead = input(f"ERRORBOT: That's {self.errors} errors since ERRORBOT was created ... Continue? (y/n) ")
                
                if goahead in ['N', 'n']:
                    if reset:
                        self.errors = 0
                
                    sys.exit()
        
            return
