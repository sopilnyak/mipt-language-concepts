#ifndef PROMISE_FUTURE_H
#define PROMISE_FUTURE_H

#include <memory>
#include "Data.h"
#include "Promise.h"

template <class T>
class Future {
public:
    Future() = default;
    explicit Future(std::shared_ptr<Data<T>> data) : data(data) {}

    Future(const Future&) = delete;
    Future(Future&&) = default;
    Future& operator =(const Future&) = delete;
    Future& operator =(Future&&) = default;
    ~Future() = default;

    std::shared_ptr<T> get() const { // Blocking get
        std::unique_lock<std::mutex> lock(data->mutex);
        data->fullNotifier.wait(lock, [this]() { return !data->isEmpty; });

        if (data->exception) {
            throw *data->exception;
        }

        return data->data;
    }

    std::shared_ptr<T> tryGet() const noexcept { // Non-blocking get
        return data->data;
    }

    friend class Data<T>;
    friend class Promise<T>;

private:
    std::shared_ptr<Data<T>> data;
};


#endif //PROMISE_FUTURE_H
