################################################################################
#
# satdump
#
################################################################################


SATDUMP_VERSION = master
SATDUMP_SITE = $(call github,SatDump,SatDump,$(SATDUMP_VERSION))
SATDUMP_INSTALL_STAGING = YES
SATDUMP_CONF_OPTS = -DBUILD_GUI=OFF -DBUILD_ZIQ=OFF -DBUILD_OPENCL=OFF -DBUILD_OPENMP=OFF -DPLUGINS_ALL=OFF -DPLUGIN_DVB=ON
#SATDUMP_CONF_OPTS = -DBUILD_GUI=OFF -DBUILD_OPENMP=OFF
$(eval $(cmake-package))


