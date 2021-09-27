8. Errors and Exceptions

There are (at least) two kinds of errors: syntax errors and exceptions.

Syntax Errors (also known as parsing errors)

he parser repeats the offending line and displays a little ‘arrow’ pointing at
the earliest point in the line where the error was detected. The error is caused
by (or at least detected at) the token preceding the arrow
File name and line number are printed so you know where to look in case the
input came from a script.

Exceptions (error when an attempt is made to execute it.)
Exceptions come in different types, and the type is printed as part of the messa
ge: the types in the example are ZeroDivisionError, NameError and TypeError.
The rest of the line provides detail based on the type of exception and what cau
sed it.

The preceding part of the error message shows the context where the exception
occurred, in the form of a stack traceback