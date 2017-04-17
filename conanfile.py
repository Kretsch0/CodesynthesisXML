from conans import ConanFile, CMake
import os

class ConanComponent(ConanFile):
    name = "CodesynthesisXML"
    version = "1.0"
    url = "NotAvailable"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "*"

    def requirements(self):
        self.requires("codeSynthesisXsdTool/4.0.0@Brunni/testing")
        self.requires("codeSynthesisXsdHeaders/4.0.0@Brunni/testing")
        self.requires("xerces-c/3.1.4@Brunni/testing")

    def build(self):
        # hopeful the ower of package codeSynthesisXsdTool will change the xsd-file-path see request:
        # https://github.com/Brunni/conan-xerces-c/issues/1
        xsdExeFile = self.deps_cpp_info["codeSynthesisXsdTool"].bin_paths[0] + "/xsd.exe"
        if not os.path.isfile(xsdExeFile):
            xsdExeFile = self.deps_cpp_info["codeSynthesisXsdTool"].rootpath  + "/xsd.exe"

        print "Using xsd-file from: " + xsdExeFile

        # given config files to generate. Could be even smarter :D find all xsd files .. stuff like that ..
        xsdFile = '%s/%s/%s/%s' % (self.conanfile_directory, self.name, "config", "hello.xsd")
        xsdPath = '%s/%s/%s' % (self.conanfile_directory, self.name, "config")

        # generate xsd to cpp files
        # --std c++11 could be removed to generate c++ 98 compatible code
        self.run('cd %s && %s cxx-tree --std c++11 %s' % (xsdPath, xsdExeFile, xsdFile))

        # do cmake stuff
        cmake = CMake(self.settings)
        self.run('cmake "%s/%s" %s' % (self.conanfile_directory, self.name, cmake.command_line))
        self.run('cmake --build . %s' % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include/" + self.name, src="install/include/" + self.name)
        self.copy("*.hxx", dst="include/" + self.name, src="install/include/" + self.name)
        self.copy("*.lib", dst="lib", src="install/lib/")
        self.copy("*.dll", dst="bin", src="install/bin/")

    def package_info(self):
        #these are the names of the libs that other components should link with
        self.cpp_info.libs = [self.name]
