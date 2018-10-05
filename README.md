# PyBundle

Set directory paths and file names for executable bundles created with Python.

Package features:

* 'frozen' environment resource management
* Frozen environment validation

## Propose
PyBundle was developed to handle paths while running from a bundled executable in a frozen environment.  Replaces functions that were repeated across projects and creates an lightweigth dependency.

## Usage
Check if you are running in a frozen environment (useful for 'dev' vs. 'production' configs), adjust paths for use in executables, manage resources in an executable file.


### Functions
| Name | Description
| --- | --- |
| **frozen()** | Determine if script is running in a frozen environment. |
| **bundle_dir()** | Handle resource management within an executable file. |
| **resource_path()** | Adjust path for executable use in executable file. |

```python
from PyBundle import frozen, bundle_dir, resource_path
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to utilize this package/repository you will need to have a Python (only tested on 3.6+ as of now) interpreter installed on your machine.

#### PyPi installation
```
pip install PyBundle
```

#### PyPi update
```
pip install --upgrade --no-cache-dir PyBundle
```

### Project Structure

```
PyBundle
├── PyBundle.py
├── __init__.py
└── _version.py
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/mrstephenneal/PyBundle/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/mrstephenneal/PyBundle). 

## Authors

* **Stephen Neal** - *Initial work* - [PyBundle](https://github.com/mrstephenneal)

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details
