#ifndef MULTISTAGE_H
#define MULTISTAGE_H

#include <unordered_map>

class Multistage
{
public:

    Multistage(int size, int extras=0, int radix=4);
    ~Multistage();
    void clear();
    void show() const;

public:

    const int SIZE;
    const int EXTRAS;
    const int RADIX;
    const int STAGES;
    const int EXTRA_CODES;

protected:

    int *_min;
    int *_swt;

    std::unordered_map<int, int> _routed;
};

#endif // MULTISTAGE_H