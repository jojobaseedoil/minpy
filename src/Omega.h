#ifndef OMEGA_H
#define OMEGA_H

#include "Multistage.h"

#include "Slider.h"

class Omega : public Multistage
{
public:
    Omega(int size, int extras=0, int radix=4);
    bool route(int input, int output);
    bool unroute(int output);

private:

    bool __is_available(int path, int row, int col) const;
    void __send_message(int path);

public:
    const Slider WINDOW;
};

#endif // OMEGA_H