CHARON_VERSION := af15fb0
CHARON_SITE := https://github.com/tvelliott/charon.git
CHARON_SITE_METHOD := git
CHARON_DEPENDENCIES += batctl bridge-utils fftwf iperf3 iproute2 liquid-dsp tunctl util-linux libfec libtuntap
CHARON_INSTALL_TARGET := YES

define CHARON_BUILD_CMDS
	$(MAKE) WORKING_DIR=$(@D) CC="$(TARGET_CC)" CXX="$(TARGET_CXX)" LD="$(TARGET_LD)" -C $(@D)
endef

define CHARON_INSTALL_TARGET_CMDS
	$(INSTALL) -D -m 0755 $(@D)/bin/* $(TARGET_DIR)/usr/bin/
	cp -r $(@D)/changes_to_plutosdr_fw_configs_rel_to_v28/buildroot/output/target/root $(TARGET_DIR)/
	cp -r $(@D)/changes_to_plutosdr_fw_configs_rel_to_v28/buildroot/output/target/etc/init.d/* $(TARGET_DIR)/etc/init.d/
endef

$(eval $(generic-package))
