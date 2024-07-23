################################################################################
#
#LUARADIO
#
################################################################################
LUARADIO_BASIC_VERSION = 0.10.0
LUARADIO_BASIC_SITE = https://github.com/vsergeev/luaradio/archive/v$(LUARADIO_BASIC_VERSION)
#LUARADIO_SITE_METHOD = git

LUARADIO_BASIC_INSTALL_STAGING = YES
LUARADIO_BASIC_LICENSE = MIT
LUARADIO_BASIC_LICENSE_FILES = LICENSE
LUARADIO_BASIC_DEPENDENCIES += luajit

#define_PLUTO_BUILD_CMDS
#	$(TARGET_MAKE_ENV) $(MAKE) $(TARGET_CONFIGURE_OPTS) PREFIX=/usr -C $(@D)
#endef

#define LIBINST
#  cd /home/eric/plutosdr-fw/buildroot/output/build/luaradio-0.5.1/embed
#  make lib
#endef
#lib: $(MAKE) -C embed
define LUARADIO_BASIC_BUILD_CMDS

        mkdir -p $(TARGET_DIR)/root/luaradio/radio
        cp -R $(@D)/radio/* $(TARGET_DIR)/root/luaradio/radio
        $(INSTALL) -D -m 755 $(@D)/luaradio $(TARGET_DIR)/root/luaradio/luaradio


endef

$(eval $(generic-package))


define LUARADIO_BASIC_INSTALL_TARGET_CMDS

        mkdir -p $(TARGET_DIR)/root/luaradio/radio
        cp -R $(@D)/radio/* $(TARGET_DIR)/root/luaradio/radio
        $(INSTALL) -D -m 755 $(@D)/luaradio $(TARGET_DIR)/root/luaradio/luaradio

endef

