# Nome da biblioteca
LIB_NAME = libminpy.so

# Arquivos fonte
SOURCES = $(wildcard *.cpp)

# Arquivos objeto
OBJECTS = $(SOURCES:.cpp=.o)

# Flags do compilador
CXX = g++
CXXFLAGS = -fPIC

# Target principal
all: $(LIB_NAME)

# Regra para criar a biblioteca compartilhada
$(LIB_NAME): $(OBJECTS)
	$(CXX) -shared -o $@ $^

# Regra para compilar arquivos objeto
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Limpeza dos arquivos objeto e da biblioteca
clean:
	rm -f $(OBJECTS) $(LIB_NAME)

.PHONY: all clean