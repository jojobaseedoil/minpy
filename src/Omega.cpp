#include "Omega.h"

#include <cassert>

extern "C" {

Omega* Omega_new(int size, int extras, int radix) {
    return new Omega(size, extras, radix);
}

bool Omega_route(Omega* obj, int input, int output) {
    return obj->route(input, output);
}

bool Omega_unroute(Omega* obj, int output) {
    return obj->unroute(output);
}

}

Omega::Omega(int size, int extras, int radix):
    Multistage (size, extras, radix),
    WINDOW     (size, extras, radix)
{

}

bool Omega::route(int input, int output)
{
    assert(0 <= input  && input  < SIZE);
    assert(0 <= output && output < SIZE);

    if(_routed.find(output) != _routed.end())
    {
        return false;
    }

    for(int extra=0; extra<EXTRA_CODES; extra++)
    {
        bool found = true;
        int  path  = WINDOW.concat(input, extra, output);

        for(int col=0; col<STAGES; col++)
        {
            int row = WINDOW.slide(path, col + 1);

            if( !__is_available(path, row, col))
            {
                found = false;
                break;
            }

        }

        if(found)
        {
            _routed[output] = path;
            __send_message(path);

            return true;
        }
    }

    return false;
}

bool Omega::unroute(int output)
{
    assert(0 <= output && output < SIZE);

    if(_routed.find(output) == _routed.end())
    {
        return false;
    }

    int path = _routed[output];

    for(int col=0; col<STAGES; col++)
    {
        int row = WINDOW.slide(path, col + 1);
        int idx = row * STAGES + col;

        _min[idx] = std::max(0, _min[idx] - 1);

        if(_min[idx] == 0)
        {
            _swt[idx] = -1;
        }
    }

    _routed.erase(output);

    return true;
}

bool Omega::__is_available(int path, int row, int col) const
{
    bool is_free      = _min[ row * STAGES + col] == 0;
    bool is_multicast = _swt[ row * STAGES + col] == WINDOW.source(path, col + 1);

    return is_free || is_multicast;
}

void Omega::__send_message(int path)
{
    for(int col=0; col<STAGES; col++)
    {
        int row = WINDOW.slide(path, col + 1);

        _min[ row * STAGES + col] += 1;
        _swt[ row * STAGES + col]  = WINDOW.source(path, col + 1);
    }
}
