# IB Solution Cookiecutter

Command line utility to set up an IB devX package or a Marketplace solution.

## Usage

```
pip install cookiecutter
cookiecutter https://github.com/vishnu-chopra/ib-solution-cookiecutter
```

This should begin the CLI to setup the project

```sh
name [my_ib_package]: # Your package name should align with IB package naming conventions
version [0.0.1]: 0.2.1
icon_url [None]: icon.png # Required only when `"solution_type": "ibflowbin"`, always `"icon.png"`
keywords [None]: testing, test  # Comma separated list of strings 
category [None]: banking 
short_description [None]: description
long_description [None]: deeeeeeeeeessssssssccccription
authors [Instabase]: Instabase, IB, CS # Comma separated list of strings
beta [True]: 
Select solution_type:
1 - ibflowbin
2 - pkpkg
Choose from 1, 2 [1]: 2
Select encryption_type:
1 - large_files
2 - v1
Choose from 1, 2 [1]: 1
```

This should generate the skeleton of the project

```sh
(base) ➜  playground cd my_ib_package 
(base) ➜  my_ib_package tree .
.
└── solution
    ├── __init__.py
    ├── package.json
    ├── readme.md
    ├── src
    │   ├── __init__.py
    │   └── my_ib_package.py
    └── test
        ├── __init__.py
        └── test_my_ib_package.py

3 directories, 7 files
```

and generate the corresponding `solution/package.json`

```sh
{
    "name": "my_ib_package",
    "version": "0.2.1",
    "icon_url": "icon.png",
    "keywords": "testing, test",
    "category": "banking",
    "short_description": "description",
    "long_description": "deeeeeeeeeessssssssccccription",
    "authors": [
        "Instabase",
        "IB",
        "CS"
    ],
    "beta": true,
    "solution_type": "pkpkg",
    "encryption_config": {
        "encryption_type": "large_files"
    }
}
```