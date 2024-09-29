# **lokiRecon**
A personal project focused on integrating Large Language Models (LLMs) with open-source intelligence (OSINT) techniques for reconnaissance.

![lokiRecon](./img/cover.png)




## **Installation**

### **Environment configuration**


To effectively integrate Large Language Models (LLMs) with hacking techniques , some tools must be installed on your system. These tools will enable seamless interaction between LLMs and open-source intelligence data:

1. Install Ollama, Ollama is a platform that allows you interact locally with Large Language Models (LLMs) without the need for an internet connection. To install Ollama, follow the instructions on the official repository:  [Ollama Installation Guide](https://ollama.com/download)

2. Make pull of LLaVA model,LLaVA is an end-to-end trained large multimodal model that is designed to understand and generate content based on both visual inputs (images) and textual instructions. To download the LLaVA model, follow the instructions on the official repository: [LLaVA Model](https://ollama.com/blog/vision-models)

### **App configuration**

1. Clone the repository:
    ```bash
    git clone https://github.com/CristianPerafan/lokiRecon.git
    ``` 
2. Create a virtual environment:
    ```bash
    python -m venv env
    ```
3. Activate the virtual environment:

    Windows:
    ```bash
    env\Scripts\activate
    ```
    Linux:
    ```bash
    source env/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. To interact with the modules of the project, you must to set some environment variables. Create a `.env` file in the root of the project and add the following variables:

    ```bash
    VISION_MODEL=Name of the vision model, you installed (e.g. llava:7b, llava:13b, llava:24b)
    INSTAGRAM_USERNAME=Instagram username used to interact with the Instagram API
    INSTAGRAM_PASSWORD=Instagram password.
    ```


