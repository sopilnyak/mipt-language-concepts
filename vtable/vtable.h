#ifndef VTABLE_VTABLE_H
#define VTABLE_VTABLE_H

#include <iostream>
#include <map>
#include <memory>
#include <unordered_map>
#include <string>

class Vtable {
public:
    void* getAddress(const std::string &funcName) const {
        if (buffer.find(funcName) == buffer.end()) {
            std::cout << "Cannot find method " << funcName << std::endl;
            return nullptr;
        } else {
            return buffer.at(funcName);
        }
    }

    void setAddress(const std::string &funcName, void* address) {
        buffer.insert(std::make_pair(funcName, address));
    }

    void addNotExisting(const Vtable &table) {
        for (std::pair<std::string, void*> keyValue : table.buffer) {
            if (buffer.find(keyValue.first) == buffer.end()) {
                buffer[keyValue.first] = keyValue.second;
            }
        }
    }

private:
    std::unordered_map<std::string, void*> buffer;
};

#endif //VTABLE_VTABLE_H
