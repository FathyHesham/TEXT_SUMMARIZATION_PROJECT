# Text Summarization Project

## Project Overview

The **Text Summarization Project** is designed to provide effective summarization of any text using **Natural Language Processing (NLP)** techniques. This project transforms text into embeddings, enabling a machine to deeply understand words and phrases to deliver more accurate and meaningful summaries. We are utilizing the **BART-SAMSum model** from Facebook, which is specially tailored for summarizing dialogues and conversations using the SAMSum dataset.

## Features

- **Accurate Text Summarization**: Provides human-like summarization by focusing on the context and semantics of the text.
- **Dialogue and Conversation Support**: Optimized to handle conversational data.
- **Customizable Configuration**: All essential configurations are maintained in `config.yaml` for easy modification and maintenance.

## Tools and Technologies

- **Python**: Core programming language used, implementing Object-Oriented Programming (OOP).
- **Transformers**: To work with the BART-SAMSum model and tokenizer.
- **Logging**: To monitor each step of the process, ensuring accurate functionality.
- **Config File**: `config.yaml` is used for storing variables, simplifying code changes.
- **PyTorch**: To run the model on GPU for performance enhancement.
- **Regular Expressions**: For text preprocessing.
- **requirements.txt**: Lists all required libraries with specified versions.
- **Docker**: For containerizing the application, making it cross-platform compatible.

## Project Structure

```plaintext

Text_Summarization_Project/
├── main.py
├── requirements.txt
├── config.yaml
├── Dockerfile
├── application/
│   ├── streamlit_app.py
│   └── __init__.py
├── models/
│   ├── summarizer_model.py
│   ├── summarizer_experiment.ipynb
│   ├── __init__.py
│   └── preprocessing.py
├── utils/
│   ├── config_loader.py
│   └── __init__.py
└── logging/
    ├── custom_logging.py
    └── __init__.py

```

## Challenges and Solutions

1. **Model Selection**:
   - **Challenge**: Identifying the best model for human-like summarization.
   - **Solution**: Tested multiple models, including BART-Large-CNN, Pegasus-Large, and BART-SAMSum. The BART-SAMSum model was selected as it combines the understanding capabilities of BART with the summarization innovation of Pegasus, making it suitable for summarizing conversational data.

2. **User Interface (UI)**:
   - **Challenge**: Creating a GUI for easy model usage.
   - **Solution**: Streamlit was used to develop a simple web-based interface, making it accessible and easy to use.

3. **Application Monitoring**:
   - **Challenge**: Ensuring complete monitoring of the app, from library imports to model and preprocessing steps.
   - **Solution**: Implemented a logging system that tracks each step, logs execution times, step names, levels (info/debug), and whether each step was successful.

4. **Code Maintainability**:
   - **Challenge**: Making the code maintainable and easy to update.
   - **Solution**: Followed OOP principles and externalized variables into `config.yaml` for easier code maintenance.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/Text_Summarization_Project.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Docker and GPU Setup

### Docker Setup

To run the application using Docker:

1. Build the Docker image:

   ```bash
   docker build -t text_summarization_app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8501:8501 text_summarization_app
   ```

This will allow the application to run on any operating system with Docker installed.

### GPU Setup

To enable GPU usage, ensure that:

- **CUDA** is installed on your machine.
- You have a compatible NVIDIA GPU.
- `torch` with GPU support is installed (e.g., `torch==1.9.0+cu111` for CUDA 11.1).

## Future Enhancements

- Implement model fine-tuning on additional datasets.
- Extend summarization capabilities to support multi-lingual texts.

## Contributors

We welcome contributions! Please fork the repository and submit a pull request with detailed descriptions of your changes.

## License

This project is licensed under the MIT License.
