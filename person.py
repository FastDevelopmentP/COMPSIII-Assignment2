class Person:
    # Constructor method to initialize the Person object with name, age, and country
    def __init__(self, name: str, age: int, country: str):
        self.name = name           # Assign the provided name to the instance variable
        self.age = age             # Assign the provided age to the instance variable
        self.country = country     # Assign the provided country to the instance variable

    # Method to return a string representation of the Person object
    def __str__(self) -> str:
        # Step 8: must RETURN (not print) this exact format
        return f"{self.name} is {self.age} years old and is from {self.country}."  # Format and return the string

    # Method to check if the person is eligible to vote (18 or older)
    def can_vote(self) -> bool:
        # Step 9: True if 18 or older, else False
        return self.age >= 18      # Return True if age is 18 or more, otherwise False
    
# Step 10: Example usage
# Inputs
person_1 = Person("Pete", 20, "USA")
person_2 = Person("Emma", 17, "Brazil")

# Outputs
print(person_1) # "Pete is 20 years old and is from USA."
print(person_1.can_vote()) # True
print(person_2) # "Emma is 17 years old and is from Brazil."
print(person_2.can_vote()) # False