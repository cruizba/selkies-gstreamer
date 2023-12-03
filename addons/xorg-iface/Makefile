PREFIX ?= /usr/local
PKG_NAME ?= selkies-xorg-iface
LIBS := -lX11 -lXrandr -lXtst -lXfixes

all:
	gcc -shared -fPIC -o xorg.so xorg.c $(LIBS)

install: all
	mkdir -p $(PREFIX)/lib/$(PKG_NAME)
	cp *.so $(PREFIX)/lib/$(PKG_NAME)/

clean:
	rm -f *.so
