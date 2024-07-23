################################################################################
#
# SoapySDR
#
################################################################################
SOAPYSDRGIT_VERSION = a8df1c575ff7345fe72050c18ede8c545e255c46
#SOAPYSDRGIT_VERSION = fe8dfd1879a8512aa305045ef1e6657a5a33f3b9
#SOAPYSDRGIT_SITE =  $(call github,pothosware,SoapySDR-master,$(SOAPYSDRGIT_VERSION))
SOAPYSDR_SOURCE = SoapySDR-master.zip
SOAPYSDRGIT_SITE =  https://github.com/pothosware/SoapySDR/archive
#SOAPYSDRGIT_SITE_METHOD = git
SOAPYSDRGIT_INSTALL_STAGING = YES
SOAPYSDRGIT_LICENSE = Boost Software License 1.0
SOAPYSDRGIT_LICENSE_FILES = LICENSE_1_0.txt
#SOAPYSDRGIT_CONF_OPTS = -DENABLE_PYTHON3=OFF -DENABLE_PYTHON=ON
SOAPYSDRGIT_CONF_OPTS = -DCFLAGS=$(TARGET_CC) -DCXXFLAGS=$(TARGET_CXX) -DENABLE_PYTHON3=OFF  -DENABLE_PYTHON=YES  -DCFLAGS=-m32 -DCXXFLAGS=-m32
#SOAPYSDRGIT_CONF_OPTS = -DPYTHON_EXECUTABLE=/usr/bin/python -DENABLE_PYTHON3=NO


$(eval $(cmake-package))

#--------------------

#SOAPYSDR_VERSION = 0.7.2
#SOAPYSDR_SOURCE = soapy-sdr-$(SOAPYSDR_VERSION).tar.gz
#SOAPYSDR_SITE = https://github.com/pothosware/SoapySDR/archive
#SOAPYSDR_INSTALL_STAGING = YES
#SOAPYSDR_LICENSE = Boost Software License 1.0
#SOAPYSDR_LICENSE_FILES = LICENSE_1_0.txt
#SOAPYSDR_DEPENDENCIES = python
#SOAPYSDR_CONF_OPTS = -DENABLE_PYTHON3=OFF -DENABLE_PYTHON=OFF
# -DCFLAGS=$(TARGET_CC) -DCXXFLAGS=$(TARGET_CXX)

#$(eval $(cmake-package))


