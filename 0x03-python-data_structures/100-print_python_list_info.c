#include "Python.h"

/**
* print_python_list_info - Prints information about a Python list.
* @p: Pointer to a PyObject (Python list).
*/
void print_python_list_info(PyObject *p)
{
Py_ssize_t i, py_list_size;
PyObject *item;
PyListObject *list_object_cast;

list_object_cast = (PyListObject *)p;
py_list_size = PyList_Size(p);

printf("[*] Size of the Python List = %ld\n", py_list_size);
printf("[*] Allocated = %ld\n", list_object_cast->allocated);

for (i = 0; i < py_list_size; ++i)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
