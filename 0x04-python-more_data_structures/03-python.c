#include <Python.h>

/**
 * print_python_list - Prints basic info about a Python list
 * @p: Pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	size = PyList_Size(p);
	printf("[*] Size = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	if (size > 10)
		size = 10;

	bytes = PyBytes_AsString(p);
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
