################################################################################
#
# LIBDVBMOD
#
################################################################################

#LIBDVBMOD_VERSION = 2.2.5
#LIBDVBMOD_SITE =  /home/eric/libdvbmod/libdvbmod
LIBDVBMOD_SITE =  /ext/Eric/old_linux/libdvbmod
#LIBDVBMOD_SOURCE = /home/eric/plutosdr-fw/buildroot/dl/libdvbmod.tar.gz
#LIBDVBMOD_INSTALL_STAGING = YES
#LIBDVBMOD_AUTORECONF = YES
LIBDVBMOD_SITE_METHOD = local


define LIBDVBMOD_BUILD_CMDS
    $(MAKE) $(CC)="$(TARGET_CXX)" LD="$(TARGET_LD)" -C $(@D)/libdvbmod
    $(MAKE) $(CC)="$(TARGET_CXX)" LD="$(TARGET_LD)" -C $(@D)/DvbTsToIQ

endef
# $(MAKE) CC="$(TARGET_CC)"
#define LIBDVBMOD_INSTALL_TARGET_CMDS
#    $(INSTALL) -D -m 0755 $(@D)/hello $(TARGET_DIR)/usr/bin
#endef

#$(eval $(generic-package))

#$(eval $(autotools-package))
$(eval $(generic-package))

