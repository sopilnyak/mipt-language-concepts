## Future/Promise
Implementation of thread-safe future and promise concepts. Supports following methods:
* Promise::getFuture() - get the future object associated with the promise
* Promise::set(T* data) - set a successful result
* Promise::setException(Exception* exception) - set an exception occured when retrieving the result
* Future::get() - blocks the thread while waiting for the result
* Future::tryGet() - makes an attempt to retrieve the result, non-blocking

Usage example: [main.cpp](https://github.com/sopilnyak/mipt-language-concepts/blob/master/promise/main.cpp)

*Written for Programming Language Concepts course at Moscow Institute of Physics and Technology in 2018.*
