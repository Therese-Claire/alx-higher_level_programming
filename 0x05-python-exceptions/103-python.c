#include <Python.h>
#include <stdio.h>
#include <floatobject.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the Python list object.
 *
 * Return: None.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyListObject\n");
		fflush(stdout);
		return;
	}

	Py_ssize_t size = PyObject_Length(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type);
	}

	fflush(stdout);
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 *
 * Return: None.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyBytesObject\n");
		fflush(stdout);
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	const char *data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);

	printf("  first %ld bytes: ", (size > 10) ? 10 : size);
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", data[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: Pointer to the Python float object.
 *
 * Return: None.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyFloatObject\n");
		fflush(stdout);
		return;
	}

	double value = PyFloat_AS_DOUBLE(p);

	printf("[.] float object info\n");

	if (PyFloat_IS_INTEGER(p))
	{
		printf("  value: %.1f\n", value);
	}
	else
	{
		printf("  value: %.17g\n", value);
	}

	fflush(stdout);
}
