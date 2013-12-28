::cl /c hello.c
::link /dynamicbase:no hello.obj user32.lib
cl /c inj.c
link /dynamicbase:no inj.obj user32.lib