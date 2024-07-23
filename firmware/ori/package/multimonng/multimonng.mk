################################################################################
#
# MULTIMONNG
#
################################################################################


MULTIMONNG_VERSION = 1.1.9
MULTIMONNG_SITE = https://github.com/EliasOenal/multimon-ng/archive/refs/tags
MULTIMONNG_SOURCE = $(MULTIMONNG_VERSION).tar.gz


MULTIMONNG_INSTALL_STAGING = YES
MULTIMONNG_LICENSE = GPL-2.0
MULTIMONNG_LICENSE_FILES = COPYING
#MULTIMONNG_DEPENDENCIES = 
#MULTIMONNG_SITE_METHOD = git




$(eval $(cmake-package))


