#Feature Road Map:

Inter object support for lists, dictionaries, and classes

Support for import statements

Abstract Syntax tree Parser for all languages into a common form

Conversion from AST to C++

JIT for C++ code




existent converters:

https://code.google.com/a/eclipselabs.org/p/j2c/
--java to c++

c to c++: just compile as c++ code

python to C (builtin support)
ruby to C (builtin support)

plagiarism (tokenizer):
https://code.google.com/a/eclipselabs.org/p/j2c/

The plan:

mutilple pass throughs for each file to do optimization and register objects

Syntax:

#!? start python

print "Hello"

#!? end

#!? start java

System.out.println("Hello");

#!? end
#!? start ruby

puts "Hello"

#!? end
#!? start C

printf("Hello");

#!? end

#!? start cpp

cout << "Hello world" << endl;

#!? end
