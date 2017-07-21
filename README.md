# SAPsucker  
![Our mascot](https://github.com/joshua-barber/SAPsucker/blob/master/SAPsucker.PNG)  
Dockerized Python SAP extractor for analytics engagements.  


### Setup (windows)
1) Install [Docker](https://docs.docker.com/docker-for-windows/install/#start-docker-for-windows) (including Docker Compose) 
2) Clone the SAPsucker repository to a working directory on your local machine  
3) Download a **linux** copy of NWRFCSDK (Net Weaver RFC SDK) from SAP from [here](http://sap.github.io/PyRFC/install.html) (do not install the SDK)   
    _**NOTE: A valid SAP account is required to download these libraries**_  
4) Extract nwrfcsdk.zip prom the previous step to this repository in a folder named 'nwrfcsdk' 


### Usage
1) Open configuration.env and enter the relevant SAP credentials for the current engagement 
2) Open powershell, navigate to this repository, then enter "docker-compose up" (Watch the logs - this may take some time on first use)  
3) Watch terminal logs for "Download complete" followed by the results data from:  
    >"select MANDT, BUKRS, BUTXT from T001 where BUKRS <> 0"  
4) Celebrate! *You now have a python-based SAP extraction tool!*

(Additional) For minor in-flight tweaks to the docker container, use "docker-compose run" in place of 'up' - this will drop you into a terminal inside the container. The connection and SQL query to SAP is currently specified inside query-builder.py  


### Future plans (once SAPsucker is stable)    
* Add a feature for defining SAP tables from CSV
* Add automated reconcilliation and summary reporting
* Another project is in progress to automate storage and ETL pipelines for the extracted SAP tables using PySpark and AWS


### Useful resources
The 0.1 version code for this project is heavily based on the below blog posts.  
http://wbarczynski.pl/calling-bapis-with-python-and-pyrfc/  
http://www.alexbaker.me/code/python-and-sap-part-1-connecting-to-sap  
