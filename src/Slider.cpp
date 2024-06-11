#include "Slider.h"

#include <cmath>

extern "C" {

Slider* Slider_new(int size, int extras, int radix) {
    return new Slider(size, extras, radix);
}

}

Slider::Slider(int size, int extras, int radix):
    WIN_BITS   (std::ceil(std::log2(size))),
    EXT_BITS   (std::ceil(radix/2) + extras),
    WORD_BITS  (2 * WIN_BITS + EXT_BITS),
    WIN_MASK   (size - 1),
    SRC_MASK   (radix - 1),
    SLIDE_RATE (std::ceil(radix/2))   
{

}