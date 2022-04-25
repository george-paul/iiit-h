# 20210902 - DnA Tutorial on The ER Model

***

## Entities

Entities represent objects and have multiple attributes. That describe the data relating to a certain entity.

There are many kinds of attributes such as:

![image-20210902154135942](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902154135942.png)

**Entity types** are entities that posses the same attributes and it describes the schema for an entity

**Entity Sets** are all the entities of one type that are in a database.

### Weak Entities

Weak entities have a **partial key** that identifies it among the other weak entities that are a related to a strong entity

## Relationships

### Binary relationships

These relationships are ones that relate entity types.

### Identifying relationships

These relationships are the ones that identify weak entities since they are not identified otherwise.

The weak entities have an existential dependency on strong entities.

### Structural Constraints

**Participation Constraints** are either *total participation*, which means that all entities of that set are related to at least one other, or *partial participation* which means that not all entities of this type participate in this relationship. 

![image-20210902155808295](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902155808295.png)

**Cardinality ratio** gives an idea of how many entities are related for each entity of the other type

![image-20210902155820446](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902155820446.png)

**Cardinality Constraints** show the max/min number of entities that can participate in a relationship.

![image-20210902155833748](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902155833748.png)

### Higher Degree relationships

Relationships can have more than two types of entities participating in it. And **relationships can also have attributes**.

![image-20210902160143300](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902160143300.png)

### Self Relationships

![image-20210902160357249](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902160357249.png)

These are relationships that exist between entities of the same **type**.



## Enhanced ER Model

### Subclass / Superclass

![image-20210902160900586](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902160900586.png)

An entity can be of a type that is a **subclass** of a **superclass** but need not be since they are already of the superclass type.

### Type Inheritance / Local Attributes

![image-20210902161124743](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902161124743.png)

Subclasses will have all the attributes that are a part of the superclass on top of other attributes that are a part of the subclass.

### Specialization / Generalization

In the **Generalization** process properties are drawn from particular entities and thus we can create generalized entity. And vice versa with **Specialization**.

### Completeness Constraint

![image-20210902161436416](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902161436416.png)

Entities of a certain superclass need not be classified into a subclass type

A double line indicates total participation in a Specialization / Generalization.

`d`stands for **disjoint** i.e. donuts can only be from exclusively one of the subclasses.

`o` stands for **overlapping** i.e. an entity can be of any of the subclass types.

## Questions from the Textbook

(watch recording)

## Project

There are four phases in the project:

### Requirements Document

* Define a mini world
* Define entities
* Understand how they interact
* Translate interactions to relationships
* Define Boundaries
* Define basic system behaviour

### Sections in the requirements document:

Refer [template document](https://docs.google.com/document/d/1QZmNEz_wQTXh15yOPqsFTUdHzYUk4qSZGE4g5RVF16o/edit).

![image-20210902170651211](C:\Users\gpaul\AppData\Roaming\Typora\typora-user-images\image-20210902170651211.png)
