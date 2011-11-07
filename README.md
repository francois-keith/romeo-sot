Romeo
=================

IMPORTANT: This software is *NOT* open-source.

Setup
-----

if the folder cmake does not exists, please run first
git submodule add git://github.com/jrl-umi3218/jrl-cmakemodules.git cmake
git submodule init 
git submodule update

To compile this package, it is recommended to create a separate build
directory:

    mkdir _build
    cd _build
    cmake [OPTIONS] ..
    make install

Please note that CMake produces a `CMakeCache.txt` file which should
be deleted to reconfigure a package from scratch.


### Dependencies

The matrix abstract layer depends on several packages which
have to be available on your machine.

 - System tools:
   - CMake (>=2.6)
