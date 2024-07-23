################################################################################
#
# SUSCAN
#
################################################################################


SUSCAN_VERSION =  v0.1.0
#SUSCAN_VERSION = 050ad2ef10f6c8f8a67a1d8ed6f049e9dd8fc5fc
SUSCAN_SITE = https://github.com/BatchDrake/suscan
SUSCAN_SOURCE = suscan-0.1.0.tar.gz
#SUSCAN-$(SUSCAN_VERSION).tar.gz

#SUSCAN_VERSION = 571cc9aeccb2004d81032cea484324aacb1a5852

SUSCAN_SITE_METHOD = git

SUSCAN_INSTALL_STAGING = YES
SUSCAN_LICENSE = GPL-2.0
SUSCAN_LICENSE_FILES =  COPYING
SUSCAN_DEPENDENCIES +=  


$(eval $(cmake-package))
