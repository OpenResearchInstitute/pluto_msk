################################################################################
#
# SoapyPlutoSDR
#
################################################################################
#SOAPYSDR_SOURCE = soapy-sdr-$(SOAPYSDR_VERSION).tar.gz
#SOAPYSDR_SITE = https://github.com/pothosware/SoapySDR/archive
#SOAPYPLUTOSDR_VERSION = ac9a9da5c14c73e752796618d56e259ca1ac6b11
#https://codeload.github.com/pothosware/SoapyPlutoSDR/tar.gz/refs/tags/soapy-plutosdr-0.2.1
SOAPYPLUTOSDR_VERSION = soapy-plutosdr-0.2.1
SOAPYPLUTOSDR_SOURCE = $(SOAPYPLUTOSDR_VERSION).tar.gz
#SOAPYPLUTOSDR_SOURCE = soapy-plutosdr-$(SOAPYPLUTOSDR_VERSION).tar.gz
SOAPYPLUTOSDR_SITE = https://github.com/pothosware/SoapyPlutoSDR
#SOAPYPLUTOSDR_SITE = https://github.com/pothosware/SoapyPlutoSDR
SOAPYPLUTOSDR_SITE_METHOD = git

SOAPYPLUTOSDR_INSTALL_STAGING = YES
SOAPYPLUTOSDR_LICENSE = LGPL-2.1+
SOAPYPLUTOSDR_LICENSE_FILE = LICENSE
SOAPYPLUTOSDR_DEPENDENCIES = libiio libad9361-iio

$(eval $(cmake-package))
