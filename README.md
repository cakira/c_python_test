# c_python_test
Small proof of concept of python tests for C code replacing python code


# Pure Python test
## How to run the pure Python tests
    pytest -v


## Block diagram of the pure Python tests
```
                  ┌───────────────┐
                  │               │
                  │     Tests     │
    ┌─────────────┤    (Python)   │
    │             │               │
    │             └───────┬───────┘
    │                     │
    │                     │  get_result()
    │                     │
    │                     │
    │                     │
    │                     ▼
    │             ┌───────────────┐
    │             │               │
    │             │               │
    │             │               │
    │             │               │
    │             │               │
    │             │   color_add   │
    │             │    (Python)   │
    │             │               │
    │             │               │
    │             │               │
    │             │               │
    │             │               │
    │             └────┬─────┬────┘
    │                  │     │
    │                  │     │
    │                  │     │
    │   get_color_a()  │     │  get_color_b()
    │                  │     │
    │                  ▼     ▼
    │             ┌───────────────┐
    │             │               │
    └────────────►│  Environment  │
    set_colors()  │    (Python)   │
                  │               │
                  └───────────────┘

              Version in pure Python
```
