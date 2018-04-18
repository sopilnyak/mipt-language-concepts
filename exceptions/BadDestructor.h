#ifndef EXCEPTIONS_BADDESTRUCTOR_H
#define EXCEPTIONS_BADDESTRUCTOR_H


#include "SafeString.h"

class BadDestructor : public SafeFile {
public:
    BadDestructor(const char* str);
    virtual ~BadDestructor();
};

BadDestructor::BadDestructor(const char* filename) : SafeFile(filename) {}

BadDestructor::~BadDestructor() {
    std::cout << "Bad destructor: " << this << std::endl;
    THROW(Exception::E_FileNotFoundException)
}


#endif //EXCEPTIONS_BADDESTRUCTOR_H
