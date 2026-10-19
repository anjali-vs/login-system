
# import logging

# logging.basicConfig(
#     filename="login.log",
#     level=logging.INFO,
#     format="%(levelname)s: %(message)s"
# )

# username = "employee"
# password = "4321"
# attempts = 0
# max_attempts = 3


# class InvalidLoginError(Exception):
#     pass


# while attempts < max_attempts:
#     try:
#         user = input("Enter username: ")
#         pwd = input("Enter password: ")

#         if user != username or pwd != password:
#             raise InvalidLoginError("Invalid username or password")

#         print("Login successful!")
#         logging.info("Employee logged in successfully")
#         break

#     except InvalidLoginError as e:
#         attempts += 1
#         print("Login failed:", e)
#         logging.warning("Failed login attempt")

#         if attempts == max_attempts:
#             print("Maximum attempts reached. Try again later.")
#             logging.error("Maximum login attempts exceeded")

#     except Exception as e:
#         print("An error occurred:", e)
#         logging.error("Error: %s", e)

#     finally:
#         print("Login attempt completed.")