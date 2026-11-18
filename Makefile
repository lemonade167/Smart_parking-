CC = gcc
CFLAGS = -std=c11 -O2 -Wall -Wextra -Iinclude
SOURCES = src/main.c src/core.c src/algorithms.c
all: parksmart
parksmart: $(SOURCES) include/parksmart.h
	$(CC) $(CFLAGS) $(SOURCES) -o parksmart
clean:
	rm -f parksmart
.PHONY: all clean
test:
	$(CC) $(CFLAGS) tests/test.c src/core.c src/algorithms.c -o test_parksmart
	./test_parksmart
