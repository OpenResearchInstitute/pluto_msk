LIBFEC_VERSION := 9750ca0
LIBFEC_SITE := https://github.com/quiet/libfec
LIBFEC_SITE_METHOD := git
LIBFEC_DEPENDENCIES += host-libfec
LIBFEC_INSTALL_STAGING := YES
LIBFEC_INSTALL_TARGET := YES

define HOST_LIBFEC_INSTALL_CMDS
	$(INSTALL) -D -m 0755 $(@D)/{gen_ccsds,gen_ccsds_tal} $(HOST_DIR)/bin/
endef

define LIBFEC_INSTALL_STAGING_CMDS
	$(INSTALL) -D -m 0644 $(@D)/*.so* $(STAGING_DIR)/usr/lib/
endef

$(eval $(cmake-package))
$(eval $(host-cmake-package))
