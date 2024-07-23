################################################################################
#
# LamaBleu apps
#
################################################################################


#LAMABLEU_APPS_VERSION = 01747db5cd60ff64115a73ac1f3bb97911f5c58e
LAMABLEU_APPS_SITE = /home/eric/pluto032/buildroot/dl/lamableu-apps
LAMABLEU_APPS_SITE_METHOD = local
#LAMABLEU_APPS_SITE = https://github.com/lamableu
#LAMABLEU_APPS_SITE_METHOD = git
LAMABLEU_APPS_LICENSE = GPLv2
LAMABLEU_APPS_LICENSE_FILES = LICENSE
LAMABLEU_APPS_DEPENDENCIES = libiio
LAMABLEU_APPS_VERSION = 0.2
define LAMABLEU_APPS_BUILD_CMDS
#	$(TARGET_CC) $(TARGET_CFLAGS) $(TARGET_LDFLAGS) \
#		$(@D)/timems.c -o $(@D)/timems -lm -lpthread 
	$(TARGET_CC) $(TARGET_CFLAGS) $(TARGET_LDFLAGS) \
		$(@D)/pow_pluto.c -o $(@D)/pow_pluto -lm -liio
	$(TARGET_CC) $(TARGET_CFLAGS) $(TARGET_LDFLAGS) \
		$(@D)/pisstv.c -o $(@D)/pisstv -lm -lgd -lmagic
#	$(TARGET_CC) -c $(TARGET_CFLAGS) $(TARGET_LDFLAGS) $(@D)/fly/fly.c 
	$(TARGET_CC) $(TARGET_CFLAGS) $(TARGET_LDFLAGS) \
		$(@D)/fly/fly.c -o $(@D)/fly/fly -lgd -lm -lz -lpng
endef

define LAMABLEU_APPS_INSTALL_TARGET_CMDS
#	$(INSTALL) -D -m 755 $(@D)/timems $(TARGET_DIR)/usr/bin/timems
	$(INSTALL) -D -m 755 $(@D)/pow_pluto $(TARGET_DIR)/usr/bin/pow_pluto
	$(INSTALL) -D -m 755 $(@D)/pisstv $(TARGET_DIR)/usr/bin/pisstv
	$(INSTALL) -D -m 755 $(@D)/fly/fly $(TARGET_DIR)/usr/bin/fly
endef

$(eval $(generic-package))
