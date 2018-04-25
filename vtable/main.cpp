#include <iostream>
#include <map>
#include <string>
#include <memory>
#include <vector>

class Vtable {
public:
    Vtable() = default;

    explicit Vtable(std::map<std::string, void*> map) {
        const auto &newMap(map);
        buffer = newMap;
    }

    void* getFuncPtr(std::string funcName) {
        if (buffer.find(funcName) == buffer.end()) {
            throw std::exception();
        }
        return buffer[funcName];
    }

    void addFuncPtr(std::string funcName, void* funcPtr) {
        buffer[funcName] = funcPtr; // Rewrite if exists
    }

    void print() const {
        std::cout << "vtable size: " << buffer.size() << std::endl;
        for (std::pair<std::string, void*> keyValue : buffer) {
            std::cout << keyValue.first << ": " << keyValue.second << std::endl;
        }
    }

    std::map<std::string, void*> buffer;
};

#define VIRTUAL_CLASS(Name) \
class Name { \
public: \
	static std::shared_ptr<Vtable> vptr; \

#define CLASS_END(Name) \
}; \
std::shared_ptr<Vtable> Name::vptr = std::make_shared<Vtable>();

#define DECLARE_METHOD(ClassName, methodName) \
void methodName() { \
	std::cout << "Call " << #ClassName << "::" << #methodName << std::endl; \
} \

#define ADD_METHOD(object, methodName) \
    object.vptr->addFuncPtr(#methodName, &methodName); \
    object.vptr->print(); \

#define VIRTUAL_CLASS_DERIVED(Name, BaseName) \
class Name { \
public: \
	std::shared_ptr<Vtable> vptr; \

#define CLASS_DERIVED_END(Name, BaseName) \
	Name() \
	{ \
        vptr = std::make_shared<Vtable>((*BaseName::vptr).buffer); \
	} \
}; \

#define VIRTUAL_CALL(object, methodName) \
{ \
    typedef void func(); \
    func* f = (func*)(object.vptr->getFuncPtr(#methodName)); \
    f(); \
}


VIRTUAL_CLASS(Base)
    int a;
CLASS_END(Base)
DECLARE_METHOD(Base, both)
DECLARE_METHOD(Base, onlyBase)

VIRTUAL_CLASS_DERIVED(Derived, Base)
    int b;
CLASS_DERIVED_END(Derived, Base)
DECLARE_METHOD( Derived, onlyDerived )

int main()
{
    Base b;
    ADD_METHOD(b, both)
    ADD_METHOD(b, onlyBase)
    VIRTUAL_CALL( b, both )

    Derived d;
    ADD_METHOD(d, both)
    ADD_METHOD(d, onlyDerived)
    VIRTUAL_CALL(d, onlyDerived)
    return 0;
}
