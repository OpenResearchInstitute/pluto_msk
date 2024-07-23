################################################################################
#
# RTL_433
#
################################################################################
RTL_433_VERSION := master
#RTL_433_VERSION := 82d0f551a5ebb9267c034540592f7106a6a83fbc
RTL_433_SITE := https://github.com/merbanan/rtl_433.git
RTL_433_SITE_METHOD := git
RTL_433_INSTALL_TARGET := YES
RTL_433_INSTALL_STAGING := YES
RTL_433_LICENSE := GPL-2.0
RTL_433_LICENSE_FILES :=  COPYING
RTL_433_DEPENDENCIES +=  soapysdr
RTL_433_CONF_OPTS := -DENABLE_SOAPYSDR=ON -DENABLE_RTLSDR=OFF 
-DCFLAGS=$(TARGET_CC) -DCXXFLAGS=$(TARGET_CXX)

$(eval $(cmake-package))
