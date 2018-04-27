#include <iostream>
#include <map>
#include <memory>
#include <unordered_map>

class Vtable {
public:
    Vtable() = default;

    explicit Vtable(std::unordered_map<std::string, void*>& table) {
        std::unordered_map<std::string, void*> newMap(table);
        buffer = newMap;
    }

    void addNew(std::unordered_map<std::string, void*>& table) {
        for (std::pair<std::string, void*> keyValue : table) {
            if (buffer.find(keyValue.first) == buffer.end()) {
                buffer[keyValue.first] = keyValue.second;
            }
        }
    }

    void* getAddress(const std::string& funcName) {
        return buffer[funcName];
    }

    void setAddress(const std::string& funcName, void* address) {
        buffer.insert(std::make_pair(funcName, address));
    }

    void print() const {
        std::cout << "--------------" << std::endl;
        std::cout << "vtable size: " << buffer.size() << std::endl;
        for (std::pair<std::string, void*> keyValue : buffer) {
            std::cout << keyValue.first << ": " << keyValue.second << std::endl;
        }
        std::cout << "--------------" << std::endl;
    }

    std::unordered_map<std::string, void*> buffer;
};

#define VIRTUAL_CLASS(Name) \
class Name { \
public: \
    static std::shared_ptr<Vtable> vptr;

#define END(Name) \
}; \
std::shared_ptr<Vtable> Name::vptr = std::make_shared<Vtable>();

#define INIT_METHOD(className, methodName) \
    className::vptr->setAddress(#methodName, (void(*)(className*)) &methodName);

#define DECLARE_METHOD(className, methodName) \
void methodName(className* _this)

#define VIRTUAL_CALL(object, methodName) \
{ \
    void* ptr = ((*object).vptr->getAddress(#methodName)); \
    typedef void (*func)(); \
    ((func) ptr)(); \
}

#define VIRTUAL_CLASS_DERIVED(Name, BaseName) \
class Name : public BaseName { \
public: \
    static std::shared_ptr<Vtable> vptr;

#define END_DERIVED(Name, BaseName) \
    Name() { \
        vptr->addNew((*BaseName::vptr).buffer); \
    } \
}; \
std::shared_ptr<Vtable> Name::vptr = std::make_shared<Vtable>();


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
END_DERIVED(Derived, Base)

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

    base.vptr->print();
    derived.vptr->print();

    Base* reallyDerived = reinterpret_cast<Base*>(&derived);


    VIRTUAL_CALL(&base, both)
    VIRTUAL_CALL(reallyDerived, both)
    VIRTUAL_CALL(reallyDerived, onlyBase)

    return 0;
}
