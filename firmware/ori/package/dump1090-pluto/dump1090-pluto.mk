################################################################################
#
# dump1090-pluto
#
################################################################################
DUMP1090_PLUTO_VERSION = master
DUMP1090_PLUTO_SITE = $(call github,PlutoSDR,dump1090,$(DUMP1090_PLUTO_VERSION))
#DUMP1090_PLUTO_SOURCE = master
#DUMP1090_PLUTO_VERSION = 7f764ae8035d43ef5ceb3c8e3bfff8ec9dde66df
#DUMP1090_PLUTO_SITE = https://github.com/PlutoSDR/dump1090
#DUMP1090_PLUTO_SITE = https://codeload.github.com/PlutoSDR/dump1090/zip/refs/heads/master
#DUMP1090_PLUTO_SITE_METHOD = git
DUMP1090_PLUTO_LICENSE = BSD-3-Clause
# no real license file
DUMP1090_PLUTO_LICENSE_FILES = README.md
DUMP1090_PLUTO_DEPENDENCIES = host-pkgconf libad9361-iio

define DUMP1090_PLUTO_BUILD_CMDS
	$(TARGET_MAKE_ENV) $(MAKE) $(TARGET_CONFIGURE_OPTS) PREFIX=/usr -C $(@D)
endef

define DUMP1090_PLUTO_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 -D $(@D)/dump1090 $(TARGET_DIR)/usr/bin/dump1090
#	$(INSTALL) -m 0755 -D $(@D)/view1090 $(TARGET_DIR)/usr/bin/view1090
#	mkdir -p $(TARGET_DIR)/www/dump1090
#	$(INSTALL) -d $(TARGET_DIR)/www/dump1090
#	cp -r $(@D)/public_html/* $(TARGET_DIR)/www/dump1090
endef

$(eval $(generic-package))
