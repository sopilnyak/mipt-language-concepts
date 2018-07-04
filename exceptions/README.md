## C++ Exceptions
Implementation of C++ exceptions using **setjmp** and **longjmp** functions. Macros TRY, CATCH and THROW are imitating the behavior of exceptions.

* An exception can pass through several nested functions
* All destructors of local objects are called when throwing an exception
* Several types of exceptions are supported (e.g. InvalidParameterException or FileNotFoundException)
* Throwing an exception from destructor is not permitted

Usage example: [SafeFile.h](https://github.com/sopilnyak/mipt-language-concepts/blob/master/exceptions/SafeFile.h), [SafeString.h](https://github.com/sopilnyak/mipt-language-concepts/blob/master/exceptions/SafeString.h)

*Written for Programming Language Concepts course at Moscow Institute of Physics and Technology in 2018.*
