################################################################################
#
# RTLSDR_AIRBAND
#
################################################################################
RTLSDR_AIRBAND_VERSION := v3.2.1
#RTLSDR_AIRBAND_VERSION := 82d0f551a5ebb9267c034540592f7106a6a83fbc
RTLSDR_AIRBAND_SITE := https://github.com/szpajder/RTLSDR-Airband
RTLSDR_AIRBAND_SITE_METHOD := git
RTLSDR_AIRBAND_INSTALL_TARGET := YES
RTLSDR_AIRBAND_INSTALL_STAGING := YES
RTLSDR_AIRBAND_LICENSE := GPL-2.0
RTLSDR_AIRBAND_LICENSE_FILES :=  COPYING
RTLSDR_AIRBAND_DEPENDENCIES +=
#RTLSDR_AIRBAND_DEPENDENCIES +=  soapysdr lame libshout lbvorbis 
RTLSDR_AIRBAND_CONF_OPTS := -lstdc++ -DWITH_SOAPYSDR=1 -DNFM=1 -DPULSE=0 -DWITH_RTLSDR=0

#RTLSDR_AIRBAND_FLAGS := -lstdc++

define RTLSDR_AIRBAND_BUILD_CMDS
#RTLSDR_AIRBAND_CFLAGS := -lstdc++
 # PLATFORM=armv7-generic $(TARGET_MAKE_ENV)  $(MAKE) CC="$(TARGET_CXX)" LD="$(TARGET_LD)" -C $(@D) WITH_SOAPYSDR=1 NFM=1 PULSE=0 WITH_RTLSDR=0

PLATFORM=armv7-generic $(TARGET_MAKE_ENV)  $(MAKE) CXX="$(TARGET_CXX)" CC="$(TARGET_CC)" LD="$(TARGET_LD)" -C $(@D) WITH_SOAPYSDR=1 NFM=1 PULSE=0 WITH_RTLSDR=0


endef


define RTLSDR_AIRBAND_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 -D $(@D)/rtl_airband $(TARGET_DIR)/usr/bin/rtl_airband
#	$(INSTALL) -m 0755 -D $(@D)/view1090 $(TARGET_DIR)/usr/bin/view1090
#	mkdir -p $(TARGET_DIR)/www/dump1090
#	$(INSTALL) -d $(TARGET_DIR)/www/dump1090
#	cp -r $(@D)/public_html/* $(TARGET_DIR)/www/dump1090
endef
$(eval $(generic-package))
