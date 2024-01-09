#include <stdio.h>
#include <stdlib.h>
#include <python.h>
/**
 * print_python_list_info - function that prints some basic about python
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] size of the python list = %ld\n", py_SIZE(p));
	printf("[*] allocated = %ld\n", list->allocated);

	for (int elem = 0; elem < py_SIZE(p); elem++)
	{
		PyObject *item = PyList_GetItem(p, elem);
		printf("element %d: %s\n", elem, py_TYPE(item)->tp_name);
	}
}
