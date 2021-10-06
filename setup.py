import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
requirements = [
    'pandas','htmlmin','pdfkit'
]
print(requirements)
setuptools.setup(
     name='csv_to_pdf',  
     version='0.1.1',
     scripts=['csv_to_pdf'] ,
     author="Yatharth Mathur",
     author_email="yatharth.mathur@gmail.com",
     description="CSV to formatted PDF converter.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/accops-yatharth/csv-to-pdf",
     packages=setuptools.find_packages(),
     install_requires=requirements,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )