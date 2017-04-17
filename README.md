# CodesynthesisXMLReader
XML-Reader for language C++ based on XSD Code Generator - Example 

## Whats the cool thing about it? Lets see...

Check this out and you know what I mean.

http://www.codesynthesis.com/products/xsd/

## Procedure to build and install:
* Install Conan ( Package-Manager for C++) https://www.conan.io/

Folder structure:

* UpperFolder
	* CodesynthesisXML
	* buildFolder ( could be anywhere )

* Change dir to `buildFolder`
* type `conan install ..\CodesynthesisXML` --build missing  -g txt

Conan should fetch the dependencies to like `xerces-c`. After successful installation of all dependencies

* type `conan build ..\CodesynthesisXML`. Software should start a build. Thats it.

To start:

* Go to the Project.exe you build before. Copy the xerces-c*.dll to the folder. (Should be somewhere in your system because conan downloaded it previously)
* type: `Project.exe` Path to `CodesynthesisXML\CodesynthesisXML\config\hello.xml`


# Have Fun !!
