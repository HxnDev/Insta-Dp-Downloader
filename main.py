import instaloader
# Can be installed by running "pip install instaloader" on terminal

insta = instaloader.Instaloader()

username = input("Enter the insta username of the person = ")

# Downloading Profile Pic
insta.download_profile(username, profile_pic_only=True)
