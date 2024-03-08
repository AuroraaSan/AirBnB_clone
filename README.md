# AirBnB Clone Command Interpreter

This project is part of the larger AirBnB clone project and focuses on creating a command-line interpreter to manage AirBnB objects. The command interpreter allows users to create, retrieve, update, and delete objects such as User, State, City, Place, etc., that inherit from a base class called BaseModel. The project also includes a file storage system for managing the objects.

## How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository from GitHub:

   ```sh
   git clone https://github.com/your-username/airbnb_clone.git
   ```

2. Change into the project directory:

   ```sh
   cd airbnb_clone
   ```

3. Start the command interpreter:

   ```sh
   ./console.py
   ```

## How to Use the Command Interpreter

Once the command interpreter is started, you can use the following commands:

- `create <class>`: Create a new instance of the specified class.
- `show <class> <id>`: Show details of the instance with the specified ID.
- `destroy <class> <id>`: Delete the instance with the specified ID.
- `all [class]`: Show all instances of the specified class. If no class is specified, show all instances of all classes.
- `update <class> <id> <attribute> "<value>"`: Update the attribute of the instance with the specified ID.

## Examples

Here are some examples of how to use the command interpreter:

```sh
(hbnb) create User
2e520e7e-08c6-4a3d-a73d-431be6672b63
(hbnb) show User 2e520e7e-08c6-4a3d-a73d-431be6672b63
[User] (2e520e7e-08c6-4a3d-a73d-431be6672b63) {'id': '2e520e7e-08c6-4a3d-a73d-431be6672b63', 'created_at': datetime.datetime(2024, 3, 9, 15, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 3, 9, 15, 30, 0, 123456)}
(hbnb) all
["[User] (2e520e7e-08c6-4a3d-a73d-431be6672b63) {'id': '2e520e7e-08c6-4a3d-a73d-431be6672b63', 'created_at': datetime.datetime(2024, 3, 9, 15, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 3, 9, 15, 30, 0, 123456)}"]
(hbnb) update User 2e520e7e-08c6-4a3d-a73d-431be6672b63 first_name "John"
(hbnb) show User 2e520e7e-08c6-4a3d-a73d-431be6672b63
[User] (2e520e7e-08c6-4a3d-a73d-431be6672b63) {'id': '2e520e7e-08c6-4a3d-a73d-431be6672b63', 'created_at': datetime.datetime(2024, 3, 9, 15, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 3, 9, 15, 35, 0, 654321), 'first_name': 'John'}
```

## Background Context

This project is part of a series of projects aimed at building a full web application similar to AirBnB. The command interpreter is the first step in this project and will be used in conjunction with other projects to build the complete application.

## Learning Objectives

By working on this project, you will learn:

- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function