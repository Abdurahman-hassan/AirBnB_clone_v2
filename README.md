# AirBnB_clone_v2

Welcome to the AirBnB_clone project, a unique collaborative effort spearheaded by Holberton School through ALX Africa. This project engages students in creating a foundational version of a platform akin to Airbnb, focusing on essential functionalities such as user authentication, property listings, bookings, and user reviews. Emphasizing the use of technologies like HTML, CSS, JavaScript, Python, and MySQL, it stands as a pivotal educational tool. This initiative not only hones full-stack web development skills but also showcases the efficacy of collaborative learning in the realm of software development. It's a testament to the practical application of web development and software engineering principles, aimed at nurturing the next generation of tech innovators.

## Table of Contents

- [Key Features](#key-features)
- [Technologies Used](technologies-used)
- [Learning Objectives](#learning-objectives)
- [The Console](#the-console)
- [Authors](#authors)


## Key Features:
- User Authentication: Secure sign-up and login functionality.
- Property Listings: Ability for users to list, view, and manage properties.
- Search Functionality: Advanced search features to filter properties based on location, amenities, price, etc.
- Booking System: Facility for users to book properties, with date selection and pricing details.
- Reviews and Ratings: Users can rate and review properties they have stayed in.
- Responsive Design: The project is designed to be fully responsive, ensuring a seamless experience across various devices.

## Technologies Used:

- Frontend: HTML, CSS, JavaScript JQuery
- Backend: Python with Flask framework
- Database: MySQL
- Additional Tools: Docker, Git, RESTful API development

## Through this project, you will:
- Gain hands-on experience with full-stack web development.
- Learn the dynamics of collaborative software development using Git and GitHub.
- Understand the practical applications of web technologies in real-world projects.

## The Console
### Overview
This Python script provides a command-line interface (CLI) for interacting with storage and data models. The CLI is designed to manage instances of various classes, allowing users to create, display, modify, and delete instances, as well as list instances and count the number of instances of a specified class. The console work on interactive mode and non-interactive mode.

### Features
- **Class Management:** Create, display, and delete instances of predefined classes such as 'BaseModel,' 'User,' 'Place,' 'State,' 'City,' 'Amenity,' and 'Review.'
- **Data Manipulation:** Update the attributes of existing instances, including complex attributes like dictionaries.
- **Listing and Counting:** List all instances or instances of a specific class, and count the number of instances of a specified class.

- **Custom Commands:** The CLI supports custom commands with a syntax similar to existing commands.

### Usage
**1. Running the CLI:**
- Execute the script (console.py) to enter the command-line interface.
- The prompt (hbnb) will indicate that the CLI is ready for input.

**2. Basic Commands:**
- `create <class name>`: Create a new instance of the specified class.
- `show <class name> <id>`: Display information about a specific instance.
- `destroy <class name> <id>`: Remove a specified instance.
- `all <class name>`: List all instances or instances of a specific class.
- `update <class name> <id> <attribute name> "<attribute value>"`: Update the attributes of a specified instance.
- `count <class name>`: Count the number of instances of a specified class.
- `help <command>`: Display details on how to use specific commands.
- `quit`: Used to exit the program and return to the system shell.

**3. Custom Commands:**
- The CLI supports custom commands with a syntax like  
`class_name.method(arguments)`. For example, `User.show("123")` or `Place.update("456", {"name": "New York"})`.

### Examples

**1. Creating a User**  
```bash
$ ./console.py
(hbnb) create User
a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac
(hbnb)
```

**2. Displaying User Information**  
```bash
$ ./console.py
(hbnb) show User a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac
[User] (a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac) {'id': 'a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac', 'created_at': datetime.datetime(2024, 1, 15, 12, 0, 0, 0), 'updated_at': datetime.datetime(2024, 1, 15, 12, 0, 0, 0)}
(hbnb)
```

**3. Updating User Name**
```bash
(hbnb) update User a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac name "John Doe"
(hbnb)
```

**4. Displaying Updated User Information**
```bash
(hbnb) show User a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac
[User] (a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac) {'id': 'a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac', 'created_at': datetime.datetime(2024, 1, 15, 12, 0, 0, 0), 'updated_at': datetime.datetime(2024, 1, 15, 12, 1, 0, 0), 'name': 'John Doe'}
(hbnb)
```

**5. Listing User Instances**
```bash
(hbnb) all User
['[User] (a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac) {'id': 'a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac', 'created_at': datetime.datetime(2024, 1, 15, 12, 0, 0, 0), 'updated_at': datetime.datetime(2024, 1, 15, 12, 1, 0, 0), 'name': 'John Doe'}']
(hbnb)
```

**7. Counting User Instances**
```bash
(hbnb) count User
1
(hbnb)
```

**8. Destroying a User**
```bash
(hbnb) create User
7a8bfc22-09b7-44bd-8b09-82cb52e7319a
(hbnb) create User
b5f08f0e-61f2-4c5d-8779-5ff4ec36f498
(hbnb) count User
2
(hbnb) destroy User 7a8bfc22-09b7-44bd-8b09-82cb52e7319a
(hbnb) count User
1
(hbnb)
```

**9. Updating Instance Attributes with a Dictionary**
```bash
(hbnb) create User
b5f08f0e-61f2-4c5d-8779-5ff4ec36f498
(hbnb) update User {"name": "John Doe", "age": 25, "email": "john@example.com"}
(hbnb) show User b5f08f0e-61f2-4c5d-8779-5ff4ec36f498
[User] (b5f08f0e-61f2-4c5d-8779-5ff4ec36f498) {'id': 'b5f08f0e-61f2-4c5d-8779-5ff4ec36f498', 'created_at': datetime.datetime(2024, 1, 15, 12, 0, 0, 0), 'updated_at': datetime.datetime(2024, 1, 15, 12, 1, 0, 0), 'name': 'John Doe', 'age': 25, 'email': 'john@example.com'}
(hbnb) quit
$
```

**10. Class Name Syntax**
```bash
(hbnb) User.create()
b5f08f0e-61f2-4c5d-8779-5ff4ec36f498
(hbnb) User.show("a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac")
['[User] (a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac) {'id': 'a593eea5-9a36-4e2a-ae4a-7e7f3e8b6eac', 'created_at': datetime.datetime(2024, 1, 15, 12, 0, 0, 0), 'updated_at': datetime.datetime(2024, 1, 15, 12, 1, 0, 0)}']
```

**11. Error Management**
```bash
(hbnb) create
** class name missing **
(hbnb) create InvalidClass
** class doesn\'t exist **
(hbnb) show User
** instance id missing **
(hbnb) User.invalid_method()
*** Unknown syntax: User.invalid_method()
```

## Testing

All your files, classes, functions can be tested with unit tests
```
$ python3 -m unittest discover tests
```

## Authors

- **Mojtaba Mohamed** [mojmo](https://github.com/mojmo)  
- **Abdulrahman Hassan** [Abdurahman-hassan](https://github.com/Abdurahman-hassan)