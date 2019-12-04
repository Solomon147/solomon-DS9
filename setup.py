"""
y = 3
"""
import setuptools
REQUIRED = ['pandas','numpy']
with open("README.md", "r") as fh:
    LONG_DESCRIPTION                               = fh.read()
    setuptools.setup(name                          = "lambdata-solomon-DS9"
                    ,version                       = "0.1.10"
                    ,author                        = "Solomon147"
                    ,description                   = "a collection of data science helper functions"
                    ,long_description              = LONG_DESCRIPTION
                    ,long_description_content_type = "text/markdown"
                    ,url                           = "https://lambdaschool.com/courses/data-science"
                    ,packages                      = setuptools.find_packages()
                    ,python_requires               = ">=3.5"
                    ,install_requires              = REQUIRED
                    ,classifiers                   = ["Programming Language :: Python :: 3"
                                                     ,"Operating System :: OS Independent"
                                                     ,"License :: OSI Approved :: MIT License"]
    )