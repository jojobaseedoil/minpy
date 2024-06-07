#include "Multistage.h"

#include <iostream>
#include <cassert>
#include <cmath>

extern "C" {

Multistage* Multistage_new(int size, int extras, int radix) {
    return new Multistage(size, extras, radix);
}

void Multistage_clear(Multistage* obj) {
    obj->clear();
}

void Multistage_show(const Multistage* obj) {
    obj->show();
}

int Multistage_get_stages(Multistage* obj)
{
    return obj->STAGES;
}

}

Multistage::Multistage(int size, int extras, int radix):
    SIZE        (size),
    EXTRAS      (extras),
    RADIX       (radix),
    STAGES      (std::ceil(std::log2(size) / std::log2(radix)) + extras),
    EXTRA_CODES (std::pow(radix, extras))
{
    _min = new int[SIZE * STAGES];        
    _swt = new int[SIZE * STAGES];

    clear();
}

Multistage::~Multistage()
{
    delete[] _min;
    delete[] _swt;
}

void Multistage::clear()
{
    for(int i=0; i<SIZE*STAGES; i++)
    {
        _min[i] =  0;
        _swt[i] = -1;
    }

    _routed.clear();
}

void Multistage::show() const
{
    for(int i=0; i<SIZE; i++)
    {
        for(int j=0; j<STAGES; j++)
        {
            std::cout << _min[i * STAGES + j] << " ";
        }
        std::cout << "\n";
    }
}