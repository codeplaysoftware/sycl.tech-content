---
title: "ND Range Kernel"
summary: "Learn how to enqueue ND range kernel functions."
contributor: rod
---

#include <iostream>
#include <sycl/sycl.hpp>

class vector_add_2;

int main(int, char**) {
    constexpr size_t dataSize = 1024;
    constexpr size_t workGroupSize = 128;

    int a[dataSize], b[dataSize], r[dataSize];
    for (int i = 0; i < dataSize; ++i) {
        a[i] = i;
        b[i] = i;
        r[i] = 0;
    }

    try {
        auto queue = sycl::queue{sycl::default_selector_v};

        std::cout << "Running on: "
              << queue.get_device().get_info<sycl::info::device::name>()
              << "\n";

        auto bufA = sycl::buffer{a, sycl::range{dataSize}};
        auto bufB = sycl::buffer{b, sycl::range{dataSize}};
        auto bufR = sycl::buffer{r, sycl::range{dataSize}};

        queue.submit([&](sycl::handler& cgh) {
            sycl::accessor accA{bufA, cgh, sycl::read_write};
            sycl::accessor accB{bufB, cgh, sycl::read_write};
            sycl::accessor accR{bufR, cgh, sycl::read_write};

            auto ndRange =
            sycl::nd_range{sycl::range{dataSize}, sycl::range{workGroupSize}};

            cgh.parallel_for<vector_add_2>(ndRange, [=](sycl::nd_item<1> itm) {
                auto globalId = itm.get_global_id();
                accR[globalId] = accA[globalId] + accB[globalId];
            });
        });

        queue.throw_asynchronous();
    } catch (const sycl::exception& e) {
        std::cout << "Exception caught: " << e.what() << std::endl;
    }

    for (int i = 0; i < dataSize; ++i) {
        if (r[i] == i * 2) {
            std::cout << "Success! Values match." << std::endl;
        } else {
            std::cout << "Failure! Values do not match." << std::endl;
        }
    }
}
