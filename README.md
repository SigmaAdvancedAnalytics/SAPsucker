# SAPsucker
Dockerized Python SAP extractor for analytics

### Usage (windows)
0) Install [Docker](https://docs.docker.com/docker-for-windows/install/#start-docker-for-windows) (including Docker Compose)
1) Download a linux copy of NWRFCSDK (Net Weaver RFC SDK) from SAP from [here](http://sap.github.io/PyRFC/install.html) (do not install the SDK)  
    _*A valid SAP account is required to download these libraries*_  
2) Copy nwrfcsdk.zip to this repository and extract it (ensure folder name remains 'nwrfcsdk')   
3) Open configuration.env and enter the relevant SAP credentials  
4) Open powershell, navigate to this repository, then enter "docker-compose up" (Watch the logs - this may take some time)  
5) Watch terminal logs for "Download complete" followed by the results data from:  
    >"select MANDT, BUKRS, BUTXT from T001 where BUKRS <> 0"  
6) (Optional) For minor in-flight tweaks to the docker container, use "docker-compose run" in place of 'up' - this will drop you into a terminal inside the container  

### Useful resources  
http://wbarczynski.pl/calling-bapis-with-python-and-pyrfc/  
http://www.alexbaker.me/code/python-and-sap-part-1-connecting-to-sap  
