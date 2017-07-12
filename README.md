# SAPsucker
Dockerized Python SAP extractor for analytics

### Usage  
1) Download a linux copy of NWRFCSDK using [these]<http://sap.github.io/PyRFC/install.html> instructions  
2) Copy NWRFCSDK.zip to this folder and extract (Entering "make unpack" into terminal works)   
3) Open the makefile and enter your SAP credentials where appropriate
4) Run "make docker_build" and "make docker_run" in order (may take a while)  
5) Watch terminal for "Download complete"  
    - There should be a new folder created with a CSV containing three fields and the first 10 rows of T001  

### Useful resources  
http://wbarczynski.pl/calling-bapis-with-python-and-pyrfc/  
http://www.alexbaker.me/code/python-and-sap-part-1-connecting-to-sap  
