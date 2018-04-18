#ifndef EXCEPTIONS_EXCEPTIONSMACRO_H
#define EXCEPTIONS_EXCEPTIONSMACRO_H

#include <csetjmp>
#include <array>
#include <iostream>
#include <set>

class ExceptionSafe;

namespace {
    int envNumber = -1;
    const int maxTryNumber = 32;
    bool isClearing = false;

    std::array<jmp_buf, maxTryNumber> env{};
    std::array<std::set<ExceptionSafe*>, maxTryNumber> objectPtrs{};
}

#define TRY(statement) { \
    ++envNumber; \
    /* Fill env with information about current state */ \
    int exception = setjmp(env[envNumber]); /* NOLINT */ \
    objectPtrs[envNumber].clear(); \
    switch (exception) { \
        case 0: \
            { statement } \
            break; \

#define CATCH(exception, statement) \
        case exception: \
            { statement } \
            break; \

#define END \
        default: \
            --envNumber; \
            if (envNumber < 0) { \
                std::cerr << "Uncaught exception!" << std::endl; \
                exit(1); \
            } \
            /* Jump to original point */ \
            longjmp(env[envNumber], exception); /* NOLINT */ \
            break; \
    } \
    --envNumber; \
}

#define THROW(exception) { \
    if (isClearing) { \
        std::cerr << "Calling exception while clearing stack" << std::endl; \
        exit(1); \
    } \
    isClearing = true; \
    /* Clear stack and call all destructors */ \
    for (ExceptionSafe* objectPtr : objectPtrs[envNumber]) { \
        objectPtr->~ExceptionSafe(); \
    } \
    isClearing = false; \
    /* Jump to original point */ \
    longjmp(env[envNumber], exception); /* NOLINT */ \
}

class ExceptionSafe {
public:
    ExceptionSafe();

    virtual ~ExceptionSafe();
};

ExceptionSafe::ExceptionSafe() {
    objectPtrs[envNumber].insert(this);
}

ExceptionSafe::~ExceptionSafe() {
    objectPtrs[envNumber].erase(this);
}

enum Exception {
    E_InvalidParameterException = 1,
    E_FileNotFoundException
};

#endif //EXCEPTIONS_EXCEPTIONSMACRO_H
