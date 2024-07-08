---
title: "Matrix Transpose"
summary: "Use GPU specific features in order to gain good GPU performance."
contributor: max
---

#include <iostream>
#include <sycl/sycl.hpp>

class kernel_a_1;
class kernel_b_1;
class kernel_c_1;
class kernel_d_1;

int main(int, char**) {
    constexpr size_t dataSize = 256;

    float inA[dataSize], inB[dataSize], inC[dataSize], out[dataSize];
    for (int i = 0; i < dataSize; ++i) {
        inA[i] = static_cast<float>(i);
        inB[i] = static_cast<float>(i);
        inC[i] = static_cast<float>(i);
        out[i] = 0.0f;
    }

    try {
        auto queue = sycl::queue{sycl::default_selector_v,
                    {sycl::property::queue::in_order{}}};

        std::cout << "Running on: "
              << queue.get_device().get_info<sycl::info::device::name>()
              << "\n";

        auto bufInA = sycl::buffer{inA, sycl::range{dataSize}};
        auto bufInB = sycl::buffer{inB, sycl::range{dataSize}};
        auto bufInC = sycl::buffer{inC, sycl::range{dataSize}};
        auto bufOut = sycl::buffer{out, sycl::range{dataSize}};

        queue.submit([&](sycl::handler& cgh) {
            sycl::accessor accInA{bufInA, cgh, sycl::read_write};

            cgh.parallel_for<kernel_a_1>(
            sycl::range{dataSize}, [=](sycl::id<1> idx) { accInA[idx] *= 2.0f; });
        });

        queue.submit([&](sycl::handler& cgh) {
            sycl::accessor accIn{bufInA, cgh, sycl::read_only};
            sycl::accessor accOut{bufInB, cgh, sycl::read_write};

            cgh.parallel_for<kernel_b_1>(sycl::range{dataSize}, [=](sycl::id<1> idx) {
                accOut[idx] += accIn[idx];
            });
        });

        queue.submit([&](sycl::handler& cgh) {
            sycl::accessor accInA{bufInA, cgh, sycl::read_only};
            sycl::accessor accInC{bufInC, cgh, sycl::read_write};

            cgh.parallel_for<kernel_c_1>(sycl::range{dataSize}, [=](sycl::id<1> idx) {
                accInC[idx] -= accInA[idx];
            });
        });

        queue.submit([&](sycl::handler& cgh) {
            sycl::accessor accInB{bufInB, cgh, sycl::read_only};
            sycl::accessor accInC{bufInC, cgh, sycl::read_only};
            sycl::accessor accOut{bufOut, cgh, sycl::write_only};

            cgh.parallel_for<kernel_d_1>(sycl::range{dataSize}, [=](sycl::id<1> idx) {
                accOut[idx] = accInB[idx] + accInC[idx];
            });
        });

        queue.wait_and_throw();
    } catch (const sycl::exception& e) {
        std::cout << "Exception caught: " << e.what() << std::endl;
    }

    for (int i = 0; i < dataSize; ++i) {
        auto val1 = std::to_string(out[i]);
        auto val2 = std::to_string(i * 2.0f);

        if (val1 == val2) {
            std::cout << "Success! " 
                      << val1
                      << " is equal to " 
                      << val2
                      << std::endl;
        } else {
            std::cout << "Failure! " 
                      << val1
                      << " is NOT equal to " 
                      << val2
                      << std::endl;
        }
    }
}
