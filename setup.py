import os
import setuptools

setuptools.setup(
    name="kconfiglib",
    # MAJOR.MINOR.PATCH, per http://semver.org
    version="6.0.0",
    description="A flexible Python Kconfig parser",
    long_description=
        open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    url="https://github.com/ulfalizer/Kconfiglib",
    author='Ulf "Ulfalizer" Magnusson',
    author_email="ulfalizer@gmail.com",
    keywords="kconfig, kbuild",
    license="ISC",

    py_modules=(
        "kconfiglib",
        "menuconfig",
        "genconfig",
        "oldconfig",
        "alldefconfig",
        "allnoconfig",
        "allmodconfig",
        "allyesconfig",
    ),

    # TODO: Don't install the menuconfig on Python 2. It won't run there.
    # setuptools needs better documentation...
    entry_points={
        "console_scripts": (
            "menuconfig = menuconfig:_main",
            "genconfig = genconfig:main",
            "oldconfig = oldconfig:main",
            "alldefconfig = alldefconfig:main",
            "allnoconfig = allnoconfig:main",
            "allmodconfig = allmodconfig:main",
            "allyesconfig = allyesconfig:main",
        )
    },

    # The terminal menuconfig implementation uses the standard Python 'curses'
    # module. The windows-curses package makes it available on Windows. See
    # https://github.com/zephyrproject-rtos/windows-curses.
    install_requires=(
        'windows-curses; sys_platform == "win32" and python_version >= "3"',
    ),

    # Needs support for unnumbered {} in format()
    python_requires=">=2.7,!=3.0.*",

    project_urls={
        "GitHub repository": "https://github.com/ulfalizer/Kconfiglib",
        "Examples": "https://github.com/ulfalizer/Kconfiglib/tree/master/examples",
    },

    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Operating System Kernels :: Linux",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    )
)
