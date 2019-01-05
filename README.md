# Design Patterns

Short implementations of the GOF design patterns in python

## Creational

### Factory Method:

#### Factory pattern is a creational design patterns that provides an interface for creating objects in a superclass, but allows a subclass to alter the type of the created object.

##### When to use:

- Use the Factory Method when you don`t know beforehand the exact types and dependencies of the object you should work with.
- Use the factory Method when you want to provide users of your library or framework with a way to extend its internal components

### Abstract Factory Method

#### Abstract factory pattern is a creational design pattern that let u create object of families related object without specifying the concrete implementation.

##### When to use:

- Use the Abstract Factory Method when your code needs to work with various families of related products, but you don`t want it to depend on the concrete classes of those products - they might be unknown beforehand or you simply want t allow for future extensibility.
