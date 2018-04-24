# Programming with Python3

## requirements

#### [py.test](https://docs.pytest.org/en/latest/getting-started.html#getstarted): helps you write better programs

> pytest is a mature full-featured Python testing tool that helps you write better programs.

* Run multiple tests

   pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows [standard test discovery rules](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery).
      
* Group multiple tests in a class
* Request a unique temporary directory for functional tests

```python
pytest --fixtures   # shows builtin and custom fixtures
```

[Marking test functions with attributes - skip, skipx](https://docs.pytest.org/en/latest/mark.html#mark)
[]


----
### [Conventions for Python test discovery](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
pytest implements the following standard test discovery:

* If no arguments are specified then collection starts from testpaths (if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.
* Recurse into directories, unless they match norecursedirs.
* In those directories, search for test_*.py or *_test.py files, imported by their test package name.
* From those files, collect test items:
    * test_ prefixed test functions or methods outside of class
    * test_ prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)


