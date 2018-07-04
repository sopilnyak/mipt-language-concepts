#include <iostream>
#include <thread>
#include "Future.h"

void printInt(Future<int>& future) {
    try {
        std::cout << *future.get() << std::endl;
    } catch (Exception &e) {
        std::unique_ptr<Exception> exception(&e);
        std::cerr << exception->what() << std::endl;
    }
}

int main() {

    std::shared_ptr<Promise<int>> promise(new Promise<int>());

    auto future = promise->getFuture();
    std::thread thread(printInt, std::ref(future));

    try {
        promise->set(new int(10));
    } catch (...) {
        promise->setException(new Exception());
    }

    thread.join();

    return 0;
}
