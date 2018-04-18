#ifndef EXCEPTIONS_SAFEFILE_H
#define EXCEPTIONS_SAFEFILE_H


#include "exceptions.h"

#include <memory>

class SafeFile : public ExceptionSafe {
public:
    explicit SafeFile(const char* filename);
    virtual ~SafeFile();

private:
    std::string name;
    FILE* file;
};

SafeFile::SafeFile(const char* filename) : name(filename) {
    file = fopen(filename, "r");
    if (file == nullptr) {
        THROW(Exception::E_FileNotFoundException)
    }
}

SafeFile::~SafeFile() {
    std::cout << "SafeFile destructor: " << this << std::endl;
}


#endif //EXCEPTIONS_SAFEFILE_H
