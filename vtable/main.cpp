#include "virtual.h"

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
END_DERIVED(Derived)

DECLARE_METHOD(Derived, both) {
    std::cout << "Derived::both" << std::endl;
}

DECLARE_METHOD(Derived, onlyDerived) {
    std::cout << "Derived::onlyDerived" << std::endl;
}

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
