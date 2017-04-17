# CodesynthesisXMLReader
XML-Reader for language C++ - based on XSD Code Generator

Procedure to install:
* Install Conan ( Package-Manager for C++) https://www.conan.io/

Folder structure:

* UpperFolder
	* CodesynthesisXML
	* buildFolder ( could be anywhere )

* Change dir to `buildFolder`
* type `conan install ..\CodesynthesisXML`  -g txt

Conan should fetch the dependencies to like `xerces-c`. After successful installation of all dependencies. 

* type `conan build ..\CodesynthesisXML`. Thats it.

To start:

* Go to the Project.exe to build before. Copy the xerces-c*.dll to the folder. (Should be somewhere in your system because conan downloaded it previously)
* type: `Project.exe` Path to `CodesynthesisXML\CodesynthesisXML\config\hello.xml`
