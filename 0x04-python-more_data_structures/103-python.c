#include <Python.h>

void print_python_bytes(PyObject *p)
{
    /* Function to print information about Python bytes objects */

    Py_ssize_t size;
    char *byte_data = NULL;

    printf("[.] Checking bytes object info\n");

    /* Check if the object is a valid bytes object */
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    /* Get the string representation and size of the bytes object */
    size = PyBytes_Size(p);
    byte_data = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  byte data: %s\n", byte_data);

    /* Print the first 10 bytes (or less if the size is less than 10) */
    printf("  first %zd bytes:", (size < 10) ? size : 10);
    for (Py_ssize_t byte_index = 0; byte_index < size && byte_index < 10; byte_index++)
        printf(" %02hhx", byte_data[byte_index]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    /* Function to print information about Python lists */

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    /* Iterate through the elements of the list */
    for (Py_ssize_t element_index = 0; element_index < size; element_index++)
    {
        PyObject *element = PyList_GetItem(p, element_index);
        const char *element_type = Py_TYPE(element)->tp_name;

        printf("Element %zd: %s\n", element_index, element_type);

        /* If the element is of type "bytes," call print_python_bytes
		* to print more information
		*/
        if (!strcmp(element_type, "bytes"))
            print_python_bytes(element);
    }
}
