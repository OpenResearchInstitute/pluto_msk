################################################################################
#
# soapysdr
#
################################################################################


#SOAPYSDR_VERSION = master
SOAPYSDR_SOURCE_BASENAME = SoapySDR
SOAPYSDR_SOURCE = soapysdr/SoapySDR.zip
SOAPYSDR_SITE = $(call github,pothosware,SoapySDR,master)
SOAPYSDR_INSTALL_STAGING = YES
SOAPYSDR_LICENSE = Boost Software License 1.0
SOAPYSDR_LICENSE_FILES = LICENSE_1_0.txt
#SOAPYSDR_MASTER_DEPENDENCIES = python
SOAPYSDR_CONF_OPTS = -DENABLE_PYTHON3=OFF -DENABLE_PYTHON=OFF
# -DCFLAGS=$(TARGET_CC) -DCXXFLAGS=$(TARGET_CXX)

define SOAPYSDR_EXTRACT_CMDS
    echo $(@D)
    unzip $(DL_DIR)/$(SOAPYSDR_SOURCE) -d $(@D)
    mv $(@D)/$(SOAPYSDR_SOURCE_BASENAME)/* $(@D)
 #   rmdir $(@D)/$(SOAPYSDR_MASTER_SOURCE_BASENAME)
endef

$(eval $(cmake-package))

