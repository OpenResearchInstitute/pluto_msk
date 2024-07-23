################################################################################
#
# SIGUTILS
#
################################################################################


SIGUTILS_VERSION =  v0.1.0
#SIGUTILS_VERSION = 050ad2ef10f6c8f8a67a1d8ed6f049e9dd8fc5fc
SIGUTILS_SITE = https://github.com/BatchDrake/sigutils
SIGUTILS_SOURCE = sigutils-0.1.0.tar.gz
#SIGUTILS-$(SIGUTILS_VERSION).tar.gz

#SIGUTILS_VERSION = 571cc9aeccb2004d81032cea484324aacb1a5852

SIGUTILS_SITE_METHOD = git

SIGUTILS_INSTALL_STAGING = YES
SIGUTILS_LICENSE = GPL-2.0
SIGUTILS_LICENSE_FILES =  COPYING
SIGUTILS_DEPENDENCIES +=  


$(eval $(cmake-package))
