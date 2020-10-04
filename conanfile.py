from conans import ConanFile, CMake, tools


class BncsutilConan(ConanFile):
    name = "bncsutil"
    version = "1.5.0"
    license = "lgpl"
    author = "bnetdocs"
    url = "https://github.com/BNETDocs/bncsutil"
    description = "BNCSUtil is the Battle.Net Chat Service Utility which aids applications trying to logon to Classic Battle.net™ using the binary protocol. Specifically, BNCSUtil has functions that help with the cryptography of game versions, keys, and passwords."
    topics = ("battle.net v1", "bnet", "bnetd", "pvpgn")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    requires = "mpir/3.0.0"

    def source(self):
        git = tools.Git(folder="bncsutil")
        git.clone("https://github.com/cen1/bncsutil.git", "develop")

    def build(self):
        self.run("conan install ./bncsutil")
        cmake = CMake(self)
        cmake.configure(source_folder="bncsutil", build_folder=".")
        cmake.build()

    #def package_info(self):
        #self.cpp_info.includedirs = ["package/include/bncsutil"]

    def package(self):
        self.copy("*.h", dst="include/bncsutil", src="bncsutil/src/bncsutil")
        self.copy("*bncsutil.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.name = "bncsutil"
        self.cpp_info.libs = ["bncsutil"]
        self.cpp_info.includedirs = ['include']

