from setuptools import setup, find_packages

setup(
    name='quizpython',
    version='1.0.0',
    license='MIT',
    author="TheGallium",
    author_email='gallium.discord@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/TheGallium/quizpython',
    keywords='quiz input question',
    install_requires=[
          'os',
          'pick'
      ],

)
