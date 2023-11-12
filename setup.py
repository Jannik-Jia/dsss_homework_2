from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',
    packages=find_packages(),
    description='A simple math quiz game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jannik Jia',
    author_email='gylz1004@gmail.com',
    url='https://github.com/Jannik-Jia/dsss_homework_2',
    install_requires=[
        'numpy'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='math quiz game education',
)
