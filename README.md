MOVED
=====
---------

This program has been migrated to [SimpleHelperTools](https://git.zontreck.com/AriasCreations/SimpleHelperTools)

Pause
======
------------

This is a simple pause / wait command. It will halt and wait for the user to press a key to continue.

Usage
======
----------

- pause


Compiling
=======
-------

```bash
mkdir build
cd build

cmake ..
make
```

Installation
=======
-----

See the above compile steps first.
```bash
make install
```

Will place the pause executable into `/usr/bin` on linux.


On windows, manual installation into a directory in your %PATH% will be required.
