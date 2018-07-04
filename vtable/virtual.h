#ifndef VTABLE_VITRUAL_H
#define VTABLE_VITRUAL_H

#include "vtable.h"

#define VIRTUAL_CLASS(Name) \
class Name { \
public: \
    Name() : vptr(&vtable) {} \
    static Vtable vtable; \
    Vtable* vptr;

#define END(Name) \
}; \
Vtable Name::vtable;

#define INIT_METHOD(className, methodName) \
className::vtable.setAddress(#methodName, static_cast<void(*)(className*)>(&methodName));

#define DECLARE_METHOD(className, methodName) \
void methodName(className* _this)

#define VIRTUAL_CLASS_DERIVED(Name, BaseName) \
class Name { \
public: \
    Name() : vptr(&vtable) { \
        vtable.addNotExisting( BaseName::vtable ); \
    } \
    static Vtable vtable; \
    Vtable* vptr;

#define END_DERIVED(Name) \
}; \
Vtable Name::vtable;

#define VIRTUAL_CALL(object, methodName) \
{ \
    typedef void (*func)(); \
    void* ptr = (*object).vptr->getAddress(#methodName); \
    if (ptr != nullptr) { \
        ((func) ptr)(); \
        std::cout << (*object).a << std::endl; \
    } \
}

#endif //VTABLE_VITRUAL_H
