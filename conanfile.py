from conans import ConanFile, CMake, tools


class GooglecloudcppConan(ConanFile):
    name = "googlecloudcpp"
    version = "0.1"
    url = "https://github.com/SechinM/conan-googlecloudcpp"
    description = "C++ library for Google Cloud"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/googleapis/google-cloud-cpp")

    def build(self):
        cmake = CMake(self)
	self.run("cd google-cloud-cpp && cmake -Hsuper -Bcmake-out")
	self.run('cd google-cloud-cpp && cmake --build cmake-out --target install')

    def package(self):
        self.copy("*.h", dst="include", src="google-cloud-cpp")
        self.copy("*googlecloudcpp.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["googlecloudcpp"]

