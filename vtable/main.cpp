#include "virtual.h"

int main() {
    INIT_METHOD(Base, both)
    INIT_METHOD(Base, onlyBase)
    INIT_METHOD(Derived, both)
    INIT_METHOD(Derived, onlyDerived)

    Base base;
    base.a = 0;

    Derived derived;
    derived.a = 1;

    Base* reallyDerived = reinterpret_cast<Base*>(&derived);

    VIRTUAL_CALL(&base, both)
    VIRTUAL_CALL(reallyDerived, both)
    VIRTUAL_CALL(reallyDerived, onlyBase)
    VIRTUAL_CALL(reallyDerived, onlyDerived)
    VIRTUAL_CALL(reallyDerived, noSuchMethod)

    return 0;
}
