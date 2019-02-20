| Testing | Coverage | Documentation |
| :-----: | :------: | :-----------: |
| [![Build Status](https://travis-ci.org/duncaneddy/python_package_template.svg?branch=master)](https://travis-ci.org/duncaneddy/python_package_template) | [![Coverage Status](https://coveralls.io/repos/github/duncaneddy/python_package_template/badge.svg?branch=master)](https://coveralls.io/github/duncaneddy/python_package_template?branch=master) | [![](https://img.shields.io/badge/docs-stable-blue.svg)](https://duncaneddy.github.iopython_package_template) |

# python_package_template
python_package_template provides an example Julia project template to quickly setup
continuous integration, test coverage reports, and automatic documentation deployment.

## Documentation

The documentation for the package can be found here: <https://sisl.github.io/python_package_template.jl/latest>

More example code and examples will be added as time permits.

## Configuring Package Name

To start off with, look through the package and replace `python_package_template` 
with your own project name.

`deps` contains C/C++ file dependencies of the packages which are compiled when
the package is installed by using the BinDeps.jl package.

`docs` contains

`src` contains the Julia source code of the package.

`test` contains unit tests which can be run locally

## Testing Locally

It is possible to test the package and code locally before commiting the update
and triggering a CI build. 

First, open a terminal window and navigate to the package root directory and 
start Julia

```bash
deddy@Andromeda:~$ cd /Stanford/repos/python_package_template.jl
deddy@Andromeda:~/Stanford/repos/python_package_template.jl$ julia
julia>
```

Next, activate the local package development environment 
```julia
julia> ]
(v1.0) pkg> activate .
(python_package_template) pkg> 
```

From here we can test the package by simply typing in the `test` command:
```julia
(python_package_template) pkg> test
```

If the package depends on C/C++ source files, these first must be compiled before
testing the package. In which case testing would involve two commands:
```julia
(python_package_template) pkg> build
(python_package_template) pkg> test
```

## Setting Up Continuous Integration

To setup continuous integration for the package we will use Travis-CI. Travis is 
free to use for open source projects (Thank you Travis!), or for build of private
repositories a subscription can be purchased.

To setup continuous integration your repository must contain a `.travis.yml` file 
AND continuous integration must be enabled for your repository on the TRAVIS CI 
webpage. This can be done either for your presonal repositories here:

`https://travis-ci.org/account/repositories`

or for your organizations' repositories here:

https://travis-ci.org/organizations/YOUR_GITHUB_ORGANIZATION_NAME/repositories

Note: If the project does not appear immediately, you may need to hit the "sync
repositories" button to have it appear.

## Setting Up Test Coverage

To set up test coverage, go to [coveralls.io](https://coveralls.io/repos/new),
login with your github account, and activate the project to add coverage reports.

Note: If the project does not appear immediately, you may need to hit the "sync
repositories" button to have it appear.

## Setting Up Documentation Deployment

If you have not done so, set up github pages by adding a pages repository to your
github account by following the [setup instructions](https://pages.github.com/) or just add an empty repository
named `username.github.io` or `orgname.github.io` to your personal or organization account. This repository can be private.

Documentation and documentation deployment is accomplished with the Julia packager
`Documenter.jl`

To setup the automated deployment of documentation as part of the CI build process
follow the [Deploy Instructions](https://juliadocs.github.io/Documenter.jl/stable/man/hosting/).

This involves two steps:
1. Adding a deploy key to the github deploy keys to allow travis CI to push to new pages to the repository.
2. Adding an environment variable to your Travis CI build settings with the deployment keys.

## Adding package to Python Package Repository (PyPi)

1. Make an account with the [Python Package Index](https://pypi.org/).
2. Install the travis-ci command line client so you can encrypt your PyPi account information.
3. 