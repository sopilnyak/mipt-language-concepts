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

#define END_DERIVED(Name, BaseName) \
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


VIRTUAL_CLASS(Base)
    int a;
END(Base)

DECLARE_METHOD(Base, both) {
    std::cout << "Base::both" << std::endl;
}

DECLARE_METHOD(Base, onlyBase) {
    std::cout << "Base::onlyBase" << std::endl;
}

VIRTUAL_CLASS_DERIVED(Derived, Base)
    int a;
END_DERIVED(Derived, Base)

DECLARE_METHOD(Derived, both) {
    std::cout << "Derived::both" << std::endl;
}

DECLARE_METHOD(Derived, onlyDerived) {
    std::cout << "Derived::onlyDerived" << std::endl;
}

#endif //VTABLE_VITRUAL_H
