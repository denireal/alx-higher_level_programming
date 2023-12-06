#include <Python.h>
#include <object.h>
#include <bytesobject.h>
#include <listobject.h>

void print_python_bytes(PyObject *p)
{
    /* Function to print information about Python bytes objects */

    long int size;
    int byte_index;
    char *byte_data = NULL;

    printf("[.] Checking bytes  object info\n");

    /* Check if the object is a valid bytes object */
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    /* Get the string representation and size of the bytes object */
    PyBytes_AsStringAndSize(p, &byte_data, &size);

    printf("  size: %li\n", size);
    printf("  byte data: %s\n", byte_data);

    /* Print the first 10 bytes (or less if the size is less than 10) */
    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    for (byte_index = 0; byte_index <= size && byte_index < 10; byte_index++)
        printf(" %02hhx", byte_data[byte_index]);
    printf("\n");
}
void print_python_list(PyObject *p)
{
    /* Function to print information about Python lists */

    long int size = PyList_Size(p);
    int element_index;
    PyListObject *list = (PyListObject *)p;
    const char *element_type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);

    /* Iterate through the elements of the list */
    for (element_index = 0; element_index < size; element_index++)
    {
        element_type = (list->ob_item[element_index])->ob_type->tp_name;
        printf("Element %i: %s\n", element_index, element_type);

        /* If the element is of type "bytes," call print_python_bytes
		* to print more information
		*/
        if (!strcmp(element_type, "bytes"))
            print_python_bytes(list->ob_item[element_index]);
    }
}
