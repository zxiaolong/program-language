

all:

ifneq ($(REMAKE_BUILD),1)
  override REMAKE_BUILD=1
  export REMAKE_BUILD
else
all:
	@echo TARGET all
endif

%::
	@echo "TARGET %::"
#	@make -r $@
