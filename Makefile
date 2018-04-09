
.PHONY: all clean

BINARY = agent
GOFILES = $(wildcard *.go)

all: $(BINARY)

$(BINARY):
	go build -o bin/$(BINARY) $(GOFILES)

clean:
	@rm -rf bin/
