#include <iostream>
#include <map>
#include <memory>
#include <unordered_map>
#include <string>

class Vtable {
public:
    void addNotExisting( const std::unordered_map<std::string, void*>& table )
    {
        for( std::pair<std::string, void*> keyValue : table ) {
            if( buffer.find( keyValue.first ) == buffer.end() ) {
                buffer[keyValue.first] = keyValue.second;
            }
        }
    }

    void* getAddress( const std::string& funcName ) const
    {
        try {
            return buffer.at( funcName );
        } catch (const std::out_of_range& e) {
            std::cout << "Cannot find method " << funcName << std::endl;
        }
    }

    void setAddress( const std::string& funcName, void* address )
    {
        buffer.insert( std::make_pair( funcName, address ) );
    }

    const std::unordered_map<std::string, void*>& getBuffer()
    {
        return buffer;
    }

private:
    std::unordered_map<std::string, void*> buffer;
};

#define VIRTUAL_CLASS(Name) \
class Name { \
public: \
	Name() : vptr(&vtable) {} \
    static Vtable vtable; \
	std::shared_ptr<Vtable> vptr; \

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
		vtable.addNotExisting( (BaseName::vtable).getBuffer() ); \
	} \
    static Vtable vtable; \
	std::shared_ptr<Vtable> vptr; \

#define END_DERIVED(Name, BaseName) \
}; \
Vtable Name::vtable;

#define VIRTUAL_CALL(object, methodName) \
{ \
    typedef void (*func)(); \
    void* ptr = ((*object).vptr->getAddress(#methodName)); \
    ((func) ptr)(); \
	std::cout << (*object).a << std::endl; \
}


VIRTUAL_CLASS( Base )
    int a;
END( Base )

DECLARE_METHOD( Base, both )
{
    std::cout << "Base::both" << std::endl;
}

DECLARE_METHOD( Base, onlyBase )
{
    std::cout << "Base::onlyBase" << std::endl;
}

VIRTUAL_CLASS_DERIVED( Derived, Base )
    int a;
END_DERIVED( Derived, Base )

DECLARE_METHOD( Derived, both )
{
    std::cout << "Derived::both" << std::endl;
}

DECLARE_METHOD( Derived, onlyDerived )
{
    std::cout << "Derived::onlyDerived" << std::endl;
}

int main()
{
    INIT_METHOD( Base, both )
    INIT_METHOD( Base, onlyBase )
    INIT_METHOD( Derived, both )
    INIT_METHOD( Derived, onlyDerived )

    Base base;
    base.a = 0;

    Derived derived;
    derived.a = 1;

    Base* reallyDerived = reinterpret_cast<Base*>(&derived);

    VIRTUAL_CALL( &base, both )
    VIRTUAL_CALL( reallyDerived, both )
    VIRTUAL_CALL( reallyDerived, onlyBase )
    VIRTUAL_CALL( reallyDerived, onlyDerived )
    VIRTUAL_CALL( reallyDerived, noSuchMethod )

    return 0;
}
