# CREATIONAL PATTERNS

### **FACTORY**

Factory is an object specializing in creating other objects.  
It encapsulates object creation.

### **ABSTRACT FACTORY**

Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

### **SINGLETON**

Global variable in an object-oriented way.

The Borg pattern (also known as the Monostate pattern) is a way to implement singleton behavior, but instead of having only one instance of a class, there are multiple instances that share the same state.

### **BUILDER**

Builder is a creational design pattern that lets you construct complex objects step by step.

### **PROTOTYPE**

Creating many identical objects individually is expensive in terms of computing power. Good alternative - cloning, because it makes a copy in the memory space instead of building individual objects respectively, from scratch the usual way.
Create a prototypical instance first, clone it whenever you need the replica

# STRUCTURAL PATTERNS

### **DECORATOR**

Allows users to add new features to existing objects without changing their structures

### **PROXY**

Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object.

### **ADAPTER**

Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

### **COMPOSITE**

The composite pattern describes a group of objects that are treated the same way as a single instance of the same type of object.

### **BRIDGE**

Bridge is used when we need to decouple an abstraction from its implementation so that the two can vary independently.

### **FACADE**

Facade pattern hides the complexities of the system and provides an interface to the client using which the client can access the system.

<u>Benefits</u>:

- Reduces complexity
- Protects client classes
- Promotes loose coupling
- Increases maintainability  
  <br>

# BEHAVIORAL PATTERNS

### **OBSERVER**

The observer pattern is a software design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

### **VISITOR**

Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

### **ITERATOR**

Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation

### **STRATEGY**

In Strategy pattern, a class behavior or its algorithm can be changed at run time.

### **CHAIN OF RESPONSIBILITY**

Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers.
Decouples the request and its processing

### **COMMAND**

Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request.

### **INTERPRETER**

The Interpreter pattern defines a grammatical representation for a language and an interpreter to interpret the grammar.

### **MEDIATOR**

The Mediator design pattern defines an object that encapsulates how a set of objects interact.

<u>Benefits</u>:

- Loose coupling
- Better maintainability  
  <br>

### **MEMENTO**

Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

### **STATE**

State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

### **TEMPLATE METHOD**

Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

- Stricter polymorphism
- Select methods to be overridden
- Protected methods
