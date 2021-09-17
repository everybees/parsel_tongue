# import exercise
# if __name__ == "__main__":
#     exercise.max_of_three_numbers()
import first_example

if __name__ == "__main__":

    first_example.register_native_to_cohort("John", "Doe", "M", "63798798978", "johndoe@gmail.com")

    print(first_example.cohort_eight)

    print("first name  | last name  |  email  |")
    print("====================================")

    for native in first_example.cohort_eight:
        print(value, "|", native.first_name, "|", native.last_name, "|", native.email)
         