################################################################################
#
# soapyremote
#
################################################################################
SOAPYREMOTE_VERSION = 0.5.0
SOAPYREMOTE_SOURCE = soapy-remote-$(SOAPYREMOTE_VERSION).tar.gz
SOAPYREMOTE_SITE = https://github.com/pothosware/SoapyRemote/archive
SOAPYREMOTE_INSTALL_STAGING = YES
SOAPYREMOTE_LICENSE = Boost Software License 1.0
SOAPYREMOTE_LICENSE_FILES = LICENSE_1_0.txt
#SOAPYREMOTE_DEPENDENCIES = soapysdr


$(eval $(cmake-package))
