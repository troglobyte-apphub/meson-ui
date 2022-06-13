#!/usr/bin/env python3
#
# Troglobyte AppHub:
# author: Michael Gene Brockus
# Gmail: <mail: michaelbrockus@gmail.com>
#
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='meson-ui',
        version='0.1.0',
        author='Michael Gene Brockus',
        author_email='michaelbrockus@gmail.com',
        license='Apache 2',
        zip_safe=True,
        url='https://github.com/troglobyte-apphub/meson-ui',
        packages=[
            'code',
            'code.mesoncli'
        ],
        python_requires='>=3.8',
        entry_points={
            'console_scripts': [
                'prog=code.main:main_prog',
            ],
        }
    )
