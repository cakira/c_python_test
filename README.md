# c_python_test
Small proof of concept of python tests for C code replacing python code

# Software requirements
## Python
It's necessary to have the packages [CFFI](https://foss.heptapod.net/pypy/cffi)
and [webcolors](https://github.com/ubernostrum/webcolors). They can be
installed with the command below:

    pip install -r requirements.txt

## C
It's necessary to have a C compiler. This code was tested with
[GCC](https://gcc.gnu.org/).

Check if GCC is already installed (`gcc --version` in the command line).
If necessary, GCC can be installed with the command below (not tested), root
required:

    sudo apt install gcc


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


# Python + C tests
## How to run the Python + C tests

    rm color_add
    ln -s ccolor_add color
    script/generate_color_add_wrapper.py
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
    │                     ▼
    │          ┌─────────────────────────┐
    │          │          ▼   Wrapper    │
    │          └──────────┬──────────┐   │
    │                     │          │   │
    │                     ▼          │   │
    │             ┌───────────────┐  │   │
    │             │               │  │   │
    │             │               │  │   │
    │             │   color_add   │  │   │
    │             │      (C)      │  │   │
    │             │               │  │   │
    │             │               │  │   │
    │             └────┬─────┬────┘  │   │
    │                  │     │       │   │
    │                  ▼     ▼       │   │
    │          ┌─────────────────────┘   │
    │          │       ▼     ▼           │
    │          └───────┬─────┬───────────┘
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
              Version in Python + C
```

# Other
This code was tested with [GCC](https://gcc.gnu.org/) 9.4 running in on
[Ubuntu](https://ubuntu.com/) 20.04.4 LTS over
[WSL](https://docs.microsoft.com/windows/wsl/).
