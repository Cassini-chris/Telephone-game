from google.cloud import storage
import imageio

# Get user input for bucket name, folder name, and number of images
bucket_name = input("Enter the bucket name: ")
folder_name = input("Enter the folder name: ")
num_images = int(input("Enter the number of images: "))
output_filename = input("Enter the desired output filename (e.g., animation.gif): ")
fps = int(input("Enter the desired frames per second (fps): "))

# Initialize a Google Cloud Storage client
client = storage.Client()

# Create a bucket object
bucket = client.bucket(bucket_name)

# Create an empty list to store the images
images = []

# Iterate through the images in the folder
for i in range(1, num_images + 1):
    # Construct the image name and path
    image_name = f"image_{i}.png"  # Assumes images are named image_1.png, image_2.png, etc.
    blob = bucket.blob(f"{folder_name}/{image_name}")

    # Download the image as bytes
    image_bytes = blob.download_as_bytes()

    # Read the image using imageio
    image = imageio.imread(image_bytes)

    # Add the image to the list
    images.append(image)

# Create a GIF from the images
imageio.mimsave(output_filename, images, fps=fps)
