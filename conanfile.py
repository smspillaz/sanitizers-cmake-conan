from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "0.0.1"


class SanitizersCMakeConan(ConanFile):
    name = "sanitizers-cmake"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    generators = "cmake"
    requires = tuple()
    url = "http://github.com/aresnm/sanitizers-cmake"
    license = "MIT"

    def source(self):
        zip_name = "sanitizers-cmake.zip"
        download("https://github.com/arsenm/sanitizers-cmake/"
                 "archive/master.zip"
                 "".format(version="sanitizers-cmake-" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/sanitizers-cmake",
                  src=os.path.join("sanitizers-cmake-master"),
                  keep_path=True)
