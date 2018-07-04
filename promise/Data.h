#ifndef PROMISE_DATA_H
#define PROMISE_DATA_H

#include <memory>
#include <mutex>
#include <atomic>
#include <condition_variable>

class Exception : public std::exception {
public:
    explicit Exception() = default;
};

template <class T>
class Future;

template <class T>
class Data {
public:
    Data() : isEmpty(true), data(nullptr), exception(nullptr) {}

    Data(const Data&) = delete;
    Data(Data&&) noexcept = delete;
    Data& operator =(const Data&) = delete;
    Data& operator =(Data&&) noexcept = delete;
    ~Data() = default;

    void set(T* newData) {
        std::lock_guard<std::mutex> lock(mutex);
        isEmpty = false;
        data.reset(newData);
        fullNotifier.notify_all();
    }

    void setException(Exception* newException) {
        std::lock_guard<std::mutex> lock(mutex);
        exception = newException;
        isEmpty = false;
        fullNotifier.notify_all();
    }

    friend class Future<T>;

private:
    std::mutex mutex;
    std::condition_variable fullNotifier;
    std::shared_ptr<T> data;
    Exception* exception;
    std::atomic<bool> isEmpty;
};


#endif //PROMISE_DATA_H
