LIBOSMOPLUTOSDR_VERSION := c78c8e6
LIBOSMOPLUTOSDR_SITE := https://github.com/Hoernchen/libosmoplutosdr.git
LIBOSMOPLUTOSDR_SITE_METHOD := git
LIBOSMOPLUTOSDR_INSTALL_TARGET := YES

$(eval $(cmake-package))
