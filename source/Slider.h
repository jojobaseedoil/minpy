#ifndef SLIDER_H
#define SLIDER_H

class Slider
{
public:

    Slider(int size, int extras, int radix);

    inline int slide(int word, int col) const
    {
        return (word >> (WORD_BITS - col * SLIDE_RATE - WIN_BITS)) & WIN_MASK; 
    }

    inline int concat(int begin, int middle, int end) const
    {
        return end | (middle << WIN_BITS) | (begin << (WIN_BITS + EXT_BITS));
    }

    inline int source(int word, int col) const
    {
        return (word >> (WORD_BITS - col * SLIDE_RATE)) & SRC_MASK;
    }
public:

    const int WIN_BITS;
    const int EXT_BITS;
    const int WORD_BITS;
    const int WIN_MASK;
    const int SRC_MASK;
    const int SLIDE_RATE;
};

#endif // SLIDER_H