from vertexai.preview.vision_models import ImageGenerationModel
from vertexai.generative_models import GenerativeModel, Part
import vertexai
from google.cloud import storage

# --- Constants ---
PROJECT_ID = "YOUR PROJECT"  # Replace with your Google Cloud project ID
LOCATION = "YOUR REGION"  # Replace with your preferred location
BUCKET_NAME = "YOUR BUCKET" #Replace with your Google Cloud Storage bucket name
INITIAL_IMAGE_URI = "YOUR SOURCE FILE"  # Replace with your initial image URI
LOOP_FOLDER = "FOLDER NAME"  # Folder within the bucket to store generated images
NUM_ITERATIONS = 500  # Number of iterations to run the loop

# --- Initialize Vertex AI ---
vertexai.init(project=PROJECT_ID, location=LOCATION)

# --- Load the image generation model ---
generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

# --- Load the Gemini Vision model ---
gemini_model = GenerativeModel("gemini-1.5-flash-002")

# --- Initialize Google Cloud Storage client ---
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

# --- Gemini Vision prompt ---
gemini_prompt = """You are an image generation expert. Analyze the image and provide a detailed description that can be used to generate a similar image. 

Specifically:

* **Content:**  Describe all objects, characters, and their actions. Include their positions and relationships to each other within the image.
* **Setting:** Describe the environment, including background details, lighting, and atmosphere. 
* **Style:** Note artistic elements like color palette, composition, and any apparent artistic style (e.g., photorealistic, painting-like, abstract).

Constraints:

* **Sensitivity:** Ensure the description is free of any offensive or harmful content.
* **Conciseness:** Be detailed but avoid unnecessary words.
* **Format:**  Only provide the descriptive text; no explanations or markdown.

Output ONLY the text that can be used as an image generation prompt."""

# --- Main loop ---
image_uri = INITIAL_IMAGE_URI
for i in range(NUM_ITERATIONS):
    print(f"Iteration {i + 1}")

    # --- Analyze the image with Gemini Vision ---
    response = gemini_model.generate_content(
        [
            Part.from_uri(image_uri, mime_type="image/jpeg"),
            gemini_prompt,
        ]
    )
    prompt = response.text
    print("Generated prompt:", prompt)

    # --- Generate an image from the prompt using Imagen ---
    image = generation_model.generate_images(
        prompt=prompt,
        number_of_images=1,
        aspect_ratio="3:4",
        safety_filter_level="block_some",
        person_generation="allow_adult",
    )

    # --- Display or save the generated image ---
    if image:
        # display_image(image[0])  # Assuming you have a display_image function defined
        local_file_name = f"image_{i + 1}.png"
        image[0].save(local_file_name)

        # --- Upload to GCS ---
        blob = bucket.blob(f"{LOOP_FOLDER}/{local_file_name}")
        blob.upload_from_filename(local_file_name)

        image_uri = f"gs://{BUCKET_NAME}/{LOOP_FOLDER}/{local_file_name}"
        print(f"Uploaded image to {image_uri}")
    else:
        print("No image was generated successfully.")
