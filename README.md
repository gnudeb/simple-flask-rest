# spring-test

## Description

Please write a Spring REST controller that handles user registration. 
The REST resource should be accessible via "/api/user" and accepts following JSON data:

```
{
   "firstName": "Some first name",
   "lastName": "The last name",
   "userName": "The user name",
   "password": "The password in plain text"
}
```

In case of <strong>success</strong> it should return the user object without the password:

```
{
   "id": "Id generated by the back-end",
   "firstName": "Some first name",
   "lastName": "The last name",
   "userName": "The user name"
}
```

In case the username is <strong>already existing</strong>, an error response should be returned with <strong>HTTP error-code 409</strong>:

```
{
   "code": "USER_ALREADY_EXISTS",
   "description": "A user with the given username already exists"
}
```

# Preconditions

You have an user-repository service available which you can autowire into the REST controller:

```
package com.maystrovyy.repository;

public interface UserRepository {
     User createUser(User user) throws UserAlreadyExistsException;
}
```

And following data object:

```
package com.maystrovyy.model;

public class User {

    private String id;
    private String firstName;
    private String lastName;
    private String userName;
    private String plainTextPassword;
    private String hashedPassword;

 // Getter and setter omitted for readability

}
```

# Bonus task
Write and deliver a running Spring Boot application (without database).

# Extra bonus task
Write unit tests for the REST controller handling all usecases.
