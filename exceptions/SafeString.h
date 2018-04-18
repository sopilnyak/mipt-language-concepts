#ifndef EXCEPTIONS_SAFESTRING_H
#define EXCEPTIONS_SAFESTRING_H

#include "exceptions.h"

#include <memory>

class SafeString : public ExceptionSafe {
public:
    explicit SafeString(std::string str);
    virtual ~SafeString();

    void printPrefixes();

private:
    std::string value;
};

SafeString::SafeString(std::string str) : value(std::move(str)) {}

SafeString::~SafeString() {
    std::cout << "Destructor: " << this << std::endl;
}

void SafeString::printPrefixes() {
    if (value.empty()) {
        THROW(Exception::E_InvalidParameterException)
    } else {
        std::cout << value << std::endl;
        SafeString prefix {value.substr(0, value.size() - 1)};
        prefix.printPrefixes();
    }
}

#endif //EXCEPTIONS_SAFESTRING_H
