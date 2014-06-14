#include "Python.h"

static PyObject * hello(PyObject *self)
{
    printf("Hello World!!\n");
        Py_RETURN_NONE;
}

static char hello_doc[] = "hello module\n";

static PyMethodDef methods[] = {
    {"hello", (PyCFunction)hello, METH_NOARGS, "print hello world.\n"},
        {NULL, NULL, 0, NULL}
};

void inithello(void)
{
    Py_InitModule3("hello", methods, hello_doc);
}


