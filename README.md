# ErrorBot
## A simple one-line error counter with multiple response options.



Basic Usage:
```py
bot = ErrorBot()

empty_list = []

for i in range(1,5):     

    print (f'Pass #{i}') 

    try:
        make_error = empty_list[1]<br/>

    except:
        bot.check(3)


# [Out]: Pass #1
 
# [Out]: Pass #2
 
# [Out]: Pass #3

# [Out]: ERRORBOT: That's 3 errors since ERRORBOT was created ... Continue? (y/n) 

[In:] Y

# [Out]: Pass #4
```

### ErrorBot also supports several additional arguments for controlling the post-threshold behavior.
<br/>
Supported arguments:

kill=True:
> Exits program without prompting
  
throw=True:
> Raises a UserWarning exception
  
ask=True
>Prompts for [Y/N] input before continuing execution (Default: True)
  
reset=True:
> Resets error counter to 0 after error tolerance reached (Default: True)
