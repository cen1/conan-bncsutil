# Conan Bncsutil

Conan package for bncsutil.

## Build profiles
TBD

## Building
Shared debug, shared release, static debug, static release.
```
conan create . bnetdocs/cen1 -s compiler.version=16 -s arch=x86_64 -s build_type=Debug -o *:shared=True
conan create . bnetdocs/cen1 -s compiler.version=16 -s arch=x86_64 -s build_type=Release -o *:shared=True
conan create . bnetdocs/cen1 -s compiler.version=16 -s arch=x86_64 -s build_type=Debug -o *:shared=False
conan create . bnetdocs/cen1 -s compiler.version=16 -s arch=x86_64 -s build_type=Release -o *:shared=False
```