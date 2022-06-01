#include "color_add.h"

#include <string.h>

#define DUMMY_COLOR "#000000"


void get_result(char *color_result) {
    strncpy(color_result, DUMMY_COLOR, strlen(DUMMY_COLOR) + 1);
}
