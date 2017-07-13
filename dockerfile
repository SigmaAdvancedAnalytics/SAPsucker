FROM ubuntu:16.10

RUN apt-get update && \
    apt-get install git python-pip -qq && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U pip && \
    pip install ipython

RUN cd /tmp && \
    git clone https://github.com/SAP/PyRFC.git;

RUN cd /tmp/PyRFC/dist && \
	pip install pyrfc-1.9.5-cp27-cp27mu-linux_x86_64.whl

#
# mount *nwrfcsdk* as volume under /usr/sap/nwrfcsdk
#
RUN mkdir -p /etc/ld.so.conf.d/ && \
	mkdir -p /usr/sap/ && \
	echo "# include nwrfcsdk" > /etc/ld.so.conf.d/nwrfcsdk.conf && \
	echo "/usr/sap/nwrfcsdk/lib" >> /etc/ld.so.conf.d/nwrfcsdk.conf

WORKDIR /home/
