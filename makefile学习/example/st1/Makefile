objects=circle.o square.o test.o 
test:$(objects)
	cc -o test $(objects)
circle.o:circle.h 
square.o:square.h 
test.o:circle.h square.h
.PHONY: clean 
clean: 	
	-rm test $(objects)

