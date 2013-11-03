test: RSA.o test.o
	g++ -o test RSA.o test.o
test.o: test.cc
	g++ -c test.cc
RSA.o: RSA.cc RSA.h
	g++ -c RSA.cc 
clean:
	rm RSA.o test.o
