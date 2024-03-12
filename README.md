# AirBnB Clone Project

## Overview

The AirBnB Clone project is part of the higher level programming track and aims to deploy a simplified version of the AirBnB website on a server. The project will focus on implementing key features of the AirBnB website to cover fundamental programming concepts.

## Features

- **Command Interpreter:** Implement a command-line interface to manipulate data without a visual interface, similar to a Shell. This is useful for development and debugging purposes.

- **Website (Front-end):** Develop a website that displays the final product to users, both static and dynamic content.

- **Database or File Storage:** Store and persist objects to a file (JSON file) or a database. This abstraction allows for easy storage type switching without updating the entire codebase.

- **API:** Create an API that provides a communication interface between the front-end and the data, allowing for operations like retrieve, create, delete, and update.

## Concepts to Learn

- **Unittest:** Write test cases to ensure the correctness of your code. Collaborate on testing to ensure comprehensive coverage.

- **Python Packages:** Understand the concept of Python packages and how they can be used to organize your code.

- **Serialization/Deserialization:** Learn how to convert Python objects into a format that can be easily stored (serialization) and how to convert them back into objects (deserialization).

- **\*args, **kwargs:** Learn how to use these features to pass a variable number of arguments to functions.

- **Datetime:** Use the `datetime` module to manipulate dates and times in your application.

## Steps

The project will be developed in several steps, each focusing on a specific concept:

1. **The Console:** Create a command interpreter to manipulate data and store/persist objects to a file (JSON).

2. **Web Static:** Learn HTML/CSS to create the static HTML content of your application.

3. **MySQL Storage:** Replace the file storage with a database storage using an ORM to map models to database tables.

4. **Web Framework - Templating:** Create a web server in Python and make your static HTML files dynamic by using objects stored in a file or database.

5. **RESTful API:** Expose all your objects stored via a JSON web interface and manipulate them via a RESTful API.

6. **Web Dynamic:** Learn JQuery to load objects from the client side using your RESTful API.

## File Structure

- **models:** Directory containing all classes used for the project. Each class represents a model, which is the representation of an object or instance.

- **tests:** Directory containing all unit tests.

- **console.py:** Entry point of the command interpreter.

- **models/base_model.py:** Base class of all models containing common elements such as id, created_at, and updated_at.

- **models/engine:** Directory containing all storage classes (using the same prototype), starting with file_storage.py.

## Conclusion

The AirBnB Clone project is an opportunity to learn and implement key concepts in web development and programming. By following the steps outlined above, you will develop a solid understanding of how web applications are built and deployed.
