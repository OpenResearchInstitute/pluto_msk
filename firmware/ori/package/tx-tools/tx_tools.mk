################################################################################
#
# TX_TOOLS
#
################################################################################
TX_TOOLS_VERSION := 252989cb06a7fe2f453f11ea9ebc72111fe77122
TX_TOOLS_SITE := https://github.com/triq-org/tx_tools
TX_TOOLS_SITE_METHOD := git
TX_TOOLS_INSTALL_TARGET := YES
TX_TOOLS_INSTALL_STAGING := YES
TX_TOOLS_LICENSE := GPL-2.0
TX_TOOLS_LICENSE_FILES :=  COPYING
TX_TOOLS_DEPENDENCIES +=  soapysdr
TX_TOOLS_CONF_OPTS := -DCFLAGS=$(TARGET_CC) -DCXXFLAGS=$(TARGET_CXX)

$(eval $(cmake-package))
