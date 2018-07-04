#ifndef PROMISE_PROMISE_H
#define PROMISE_PROMISE_H


#include <bits/shared_ptr.h>
#include "Data.h"

template <class T>
class Promise {
public:
    Promise() : data(new Data<T>()) {}
    Promise(const Promise&) = delete;
    Promise(Promise&&) noexcept = default;
    Promise& operator =(const Promise&) = delete;
    Promise& operator =(Promise&&) noexcept = default;
    ~Promise() = default;

    Future<T> getFuture() {
        return Future<T>(data);
    }

    void set(T* newData) {
        data->set(newData);
    }
    void setException(Exception* exception) {
        data->setException(exception);
    }

private:
    std::shared_ptr<Data<T>> data;
};


#endif //PROMISE_PROMISE_H
