#include "color_add.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define COLOR_HEX_MAX_LENGTH 8
#define RED_MASK 0xff0000
#define GREEN_MASK 0x00ff00
#define BLUE_MASK 0x0000ff

void get_color_a(char *);
void get_color_b(char *);

static uint32_t color_hex_to_int(const char *color_hex);
static uint32_t color_add(uint32_t color_a_int, uint32_t color_b);
static void color_int_to_hex(uint32_t color_int, char *color_hex);

void get_result(char *color_result) {
    char color_a[COLOR_HEX_MAX_LENGTH];
    char color_b[COLOR_HEX_MAX_LENGTH];

    get_color_a(color_a);
    get_color_b(color_b);
    uint32_t color_a_int = color_hex_to_int(color_a);
    uint32_t color_b_int = color_hex_to_int(color_b);
    uint32_t color_result_int = color_add(color_a_int, color_b_int);
    color_int_to_hex(color_result_int, color_result);
}

static uint32_t color_hex_to_int(const char *color_hex) {
    return strtoul(color_hex + 1, NULL, 16);
}

static uint32_t color_add(uint32_t color_a_int, uint32_t color_b_int) {
    uint32_t red_sum = (color_a_int & RED_MASK) + (color_b_int & RED_MASK);
    if (red_sum > RED_MASK) {
        red_sum = RED_MASK;
    }
    uint32_t green_sum =
        (color_a_int & GREEN_MASK) + (color_b_int & GREEN_MASK);
    if (green_sum > GREEN_MASK) {
        green_sum = GREEN_MASK;
    }
    uint32_t blue_sum = (color_a_int & BLUE_MASK) + (color_b_int & BLUE_MASK);
    if (blue_sum > BLUE_MASK) {
        blue_sum = BLUE_MASK;
    }
    return (red_sum | green_sum | blue_sum);
}

static void color_int_to_hex(uint32_t color_int, char *color_hex) {
    snprintf(color_hex, COLOR_HEX_MAX_LENGTH, "#%06x", color_int);
}
