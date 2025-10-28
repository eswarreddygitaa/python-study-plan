import random
import string

#1  # Write a function which generates a six digit/character random_user_id.
def random_user_id():
    chars = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(chars) for _ in range(6))
    return user_id
print(random_user_id())


#2  # Modify previous task: user_id_gen_by_user() — takes input for length and count.
def user_id_gen_by_user():
    num_chars = int(input("\nEnter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    chars = string.ascii_letters + string.digits
    for _ in range(num_ids):
        user_id = ''.join(random.choice(chars) for _ in range(num_chars))
        print(user_id)
user_id_gen_by_user()


#3  # Write a function named rgb_color_gen that generates RGB colors
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"\nrgb({r},{g},{b})"
print(rgb_color_gen())