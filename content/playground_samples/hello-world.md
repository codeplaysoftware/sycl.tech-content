---
title: "Hello World! (on device)"
summary: "Learn the basics with classic Hello World! sample, run on device."
contributor: scott
cached_response: "Hello World! (on device)"
---

#include <sycl/sycl.hpp>

class hello_world;

int main(int, char**) {
    auto device_selector = sycl::default_selector_v;
    
    sycl::queue queue(device_selector);

    std::cout << "Running on: "
              << queue.get_device().get_info<sycl::info::device::name>()
              << "\n";
    
    queue.submit([&] (sycl::handler& cgh) {
        auto os = sycl::stream{128, 128, cgh};
        cgh.single_task<hello_world>([=]() { 
            os << "Hello World! (on device)\n"; 
        });
    });
    
    return 0;
}
