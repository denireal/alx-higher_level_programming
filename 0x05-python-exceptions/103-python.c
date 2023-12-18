#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

/**
* print_python_float - Prints information about Python float
* @py_float_obj: PyObject representing a Python float object
*/
void print_python_float(PyObject *py_float_obj)
{
PyFloatObject *float_obj = (PyFloatObject *)py_float_obj;
double float_value;

printf("[.] float object info\n");
if (!PyFloat_Check(float_obj))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
float_value = float_obj->ob_fval;
printf("  value: %s\n", PyOS_double_to_string(float_value, 'r', 0,
Py_DTSF_ADD_DOT_0, NULL));
}

/**
* print_python_bytes - Prints information about Python bytes
* @py_bytes_obj: PyObject representing a Python bytes object
*/
void print_python_bytes(PyObject *py_bytes_obj)
{
long unsigned int size;
unsigned int i = 0;
char *bytes_str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(py_bytes_obj))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)py_bytes_obj)->ob_size;
bytes_str = ((PyBytesObject *)py_bytes_obj)->ob_sval;
printf("  size: %lu\n", size);
printf("  trying string: %s\n", bytes_str);
printf("  first %lu bytes:", size < 10 ? size + 1 : 10);
while (i <= size && i < 10)
printf(" %02hhx", bytes_str[i++]);
printf("\n");
}

/**
* print_python_list - Prints information about Python lists
* @py_list_obj: PyObject representing a Python list
*/
void print_python_list(PyObject *py_list_obj)
{
long unsigned int size;
unsigned int i = 0;
PyListObject *list_obj = (PyListObject *)py_list_obj;
const char *element_type;

printf("[*] Python list info\n");
if (!PyList_Check(list_obj))
{
printf("  [ERROR] Invalid List Object\n");
return;
}
size = ((PyVarObject *)py_list_obj)->ob_size;
printf("[*] Size of the Python List = %lu\n", size);
printf("[*] Allocated = %lu\n", list_obj->allocated);
while (i < size)
{
element_type = (list_obj->ob_item[i])->ob_type->tp_name;
printf("Element %i: %s\n", i, element_type);
if (!strcmp(element_type, "bytes"))
print_python_bytes(list_obj->ob_item[i]);
if (!strcmp(element_type, "float"))
print_python_float(list_obj->ob_item[i]);
i++;
}
}
