################################################################################
#
# RXTOOLS
#
################################################################################

#RXTOOLS_VERSION = f8f7e4560dd7a8bfaf5e3dfe50685a50ab1e04a9
RXTOOLS_VERSION = master
RXTOOLS_SITE = https://github.com/LamaBleu/rx_tools/archive
#RXTOOLS_SITE = $(call github,LamaBleu,rx_tools,$(RXTOOLS_VERSION))
#RXTOOLS_SOURCE = rxtools-$(RXTOOLS_VERSION).tar.gz
RXTOOLS_SOURCE = $(RXTOOLS_VERSION).tar.gz
#RXTOOLS_VERSION = 571cc9aeccb2004d81032cea484324aacb1a5852
#RXTOOLS_SITE = https://github.com/rxseger/rx_tools.git
#oRXTOOLS_SITE_METHOD = git

RXTOOLS_INSTALL_STAGING = YES
RXTOOLS_LICENSE = GPL-2.0
RXTOOLS_LICENSE_FILES = COPYING
RXTOOLS_DEPENDENCIES = soapysdr


$(eval $(cmake-package))
#https://github.com/LamaBleu/rx_tools/archive/refs/heads/master.zip
