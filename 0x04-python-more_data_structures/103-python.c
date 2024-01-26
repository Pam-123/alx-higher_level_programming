#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
		if (strcmp(Py_TYPE(element)->tp_name, "bytes") == 0)
			print_python_bytes(element);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i + 1 < size && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
}
