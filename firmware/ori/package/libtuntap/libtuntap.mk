LIBTUNTAP_VERSION := bf8e0fe
LIBTUNTAP_SITE := https://github.com/tvelliott/libtuntap.git
LIBTUNTAP_SITE_METHOD := git
LIBTUNTAP_INSTALL_STAGING := YES
LIBTUNTAP_INSTALL_TARGET := YES

define LIBTUNTAP_INSTALL_STAGING_CMDS
	$(INSTALL) -D -m 0644 $(@D)/*.h $(STAGING_DIR)/usr/include/
	$(INSTALL) -D -m 0644 $(@D)/lib/* $(STAGING_DIR)/usr/lib/
endef

$(eval $(cmake-package))
