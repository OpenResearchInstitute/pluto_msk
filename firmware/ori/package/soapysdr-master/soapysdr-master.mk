################################################################################
#
# soapysdr
#
################################################################################

#https://github.com/pothosware/SoapySDR/archive/master/SoapySDR-master.zip
SOAPYSDR_MASTER_VERSION = soapysdr-master
SOAPYSDR_MASTER_SOURCE_BASENAME = SoapySDR-master
SOAPYSDR_MASTER_SOURCE =$(SOAPYSDR_MASTER_SOURCE_BASENAME).zip
SOAPYSDR_MASTER_SITE = $(call github,pothosware,SoapySDR,master)
SOAPYSDR_MASTER_INSTALL_STAGING = YES
SOAPYSDR_MASTER_LICENSE = Boost Software License 1.0
SOAPYSDR_MASTER_LICENSE_FILES = LICENSE_1_0.txt
#SOAPYSDR_MASTER_DEPENDENCIES = python
SOAPYSDR_MASTER_CONF_OPTS = -DENABLE_PYTHON3=OFF -DENABLE_PYTHON=OFF
# -DCFLAGS=$(TARGET_CC) -DCXXFLAGS=$(TARGET_CXX)

define SOAPYSDR_MASTER_EXTRACT_CMDS
    echo $(@D)
    unzip $(DL_DIR)/$(SOAPYSDR_MASTER_VERSION)/$(SOAPYSDR_MASTER_SOURCE_BASENAME).zip -d $(@D)
    mv $(@D)/$(SOAPYSDR_MASTER_SOURCE_BASENAME)/* $(@D)
 #   rmdir $(@D)/$(SOAPYSDR_MASTER_SOURCE_BASENAME)
endef

$(eval $(cmake-package))

