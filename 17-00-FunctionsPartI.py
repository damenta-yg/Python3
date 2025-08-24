"""
===================
Function Definition
===================
Functions are used for comply the DRY Principle => Dont Repeat Yourself
Clean up and prevent code duplication
Abstract away code for other users
Functions also can used for organize logic in code more efficient
"""


"""
===================
Function Structure
===================

def function_name(arguments/parameters):
    -----logic section-----
    return x => not all function need return

"""

"""
===================
Common Return Keyword Mistakes
===================

1. Wrong Placement of Keywords Return
2. Unnecessary else on putting Return on if/else statement

"""

"""
===================
Default Parameters
===================

def function_name(args1,args2=2,args3=5):
    return args1 * args2 * args3

function_name(3) => 3*2*5 => will return 30

Why need default params:
1. Allows to be more defensive
2. Avoids errors with incorrect parameters
3. More readable examples
 
"""

"""
===================
Keyowrd Arguments
===================

def function_name(args1,args2=2,args3=5):
    return args1 * args2 * args3

function_name(args2=5,args3=7,args1=4)
=> can execute without order

"""