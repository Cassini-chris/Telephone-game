# Telephone-game

# Diffusion-Multimodal Bias Loop

This repository contains the code for a research project investigating potential biases in state-of-the-art diffusion models and multimodal systems. The project employs an iterative approach, generating images from prompts, describing them with a multimodal model, and using the descriptions to generate new images in a continuous loop.

## Project Description

This research aims to identify and analyze potential biases in diffusion models and multimodal systems by establishing a closed loop between them. The process involves:

1. **Initialization:** Providing an initial prompt to a diffusion model (e.g., Stable Diffusion) to generate an image.
2. **Description:** Feeding the generated image into a multimodal model (e.g., BLIP) to obtain a detailed textual description.
3. **Regeneration:** Using the generated description as a prompt for the diffusion model to create a new image.
4. **Iteration:** Repeating steps 2 and 3 for a large number of iterations (e.g., 10,000).

By analyzing the evolution of the generated images and textual descriptions over many iterations, this project seeks to uncover subtle biases and drifts in semantic meaning, artistic style, composition, and other visual attributes.

## Hypotheses

This research explores the following hypotheses:

1. **Semantic Drift:**  Gradual shift in the meaning of generated images.
2. **Style Convergence:** Convergence towards a specific artistic style.
3. **Compositional Simplification:** Decrease in complexity of image composition.
4. **Bias Amplification:** Exaggeration of existing biases (gender, race, etc.).
5. **Prompt Specificity:** Increase in specificity and detail of generated prompts.
6. **Loss of Detail:** Progressive loss of fine-grained image details.
7. **Emergence of Artifacts:** Appearance of visual artifacts or anomalies.
8. **Concept Fixation:** Fixation on a particular concept or theme.
9. **Oscillation:** Oscillation between distinct visual states.
10. **Unpredictability:** Chaotic and unpredictable evolution of images and prompts.

## Getting Started

1. **Clone the repository:** `git clone https://github.com/your-username/Diffusion-Multimodal-Bias-Loop.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Configure models:**  Specify the desired diffusion model and multimodal model in `config.py`.
4. **Run the main script:** `python main.py`

## Results and Analysis

The `results` directory will store the generated images and textual descriptions at each iteration. Jupyter notebooks in the `analysis` directory provide tools for visualizing and analyzing the evolution of the generated content, including:

* **Image grids:** Visualizing the progression of images over iterations.
* **Semantic analysis:** Tracking changes in the frequency and co-occurrence of keywords in the descriptions.
* **Style analysis:** Quantifying changes in artistic style using image features.
* **Bias detection:** Measuring potential biases using established metrics.

## Contributing

Contributions to this project are welcome! Feel free to open issues for bug reports or feature requests. Pull requests with improvements or extensions are also encouraged.
