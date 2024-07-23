################################################################################
#
# nng
#
################################################################################


NNG_VERSION = master
NNG_SITE = $(call github,nanomsg,nng,$(NNG_VERSION))
NNG_INSTALL_STAGING = YES
NNG_CONF_OPTS = -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON

$(eval $(cmake-package))


