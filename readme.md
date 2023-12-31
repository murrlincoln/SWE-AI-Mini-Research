# The LLM 100 Coding Problems Benchmark: A Comprehensive Assessment for AI Programming Skills

---

## 🌟 Introduction

Welcome to a revolutionary benchmark, specifically designed to assess the programming aptitude of next-generation Language Learning Models (LLMs) like Bard, GPT-4, and Claude-2. This repository contains 100 meticulously designed coding challenges that span across a wide range of topics—from data structures and algorithms to string manipulations and bitwise operations.

### 🚀 What's Novel?

What sets this benchmark apart is its multi-layered complexity:

1. **Diversity in Problems**: 100 problems carefully chosen to cover a broad spectrum of computer science topics.
2. **Four Types of Prompts**: Each problem category comes in four different prompt styles, a novel approach aimed at evaluating the model's comprehension and adaptability. It tests both the problem solving ability of an LLM, as well as its compatability with understanding questions prompted by the three chosen LLMS.
3. **Multiple LLMs for Question Generation**: The prompts are generated by a variety of sophisticated LLMs, adding an additional layer of complexity and variety.
4. **Comprehensive Assessment**: The structure allows for a granular evaluation of an LLM's programming skills, comprehension, and problem-solving abilities.

---

## 🎯 Types of Prompts

Each problem is presented in four unique styles to measure the LLM's adaptability and comprehension skills:

1. **Prompt Only**: The bare minimum—a straightforward problem statement.
2. **Prompt with Tests**: A problem statement accompanied by example test cases.
3. **Prompt Tests Only**: Only test cases are provided. How well can the LLM comprehend what's required?
4. **Prompt Generic Tests**: Test cases with a masked function name, evaluating how well the LLM can adapt to ambiguity.

---

## 🤖 Evaluating LLMs: The Ultimate Test of Comprehension

The prompts are generated by a diverse set of LLMs—Bard, GPT-4, and Claude-2. This multi-model approach ensures that the prompts not only vary in complexity but also in style and structure, providing a robust, comprehensive framework for evaluating a solving LLM's capabilities.

---

## 🛠 Getting Started: Step-by-Step Guide

### 🧪 Running the Unit Tests

1. **Clone the Repository**: Use `git clone` to download the repository.
2. **Navigate to the Project**: Use the terminal to enter the project directory.
3. **Run the Tests**: Execute `python unittest_main.py`.

This will run a series of unit tests to validate the correctness and efficiency of the generated code.

### 🎩 Generating Code using OpenAI API

1. **Set OpenAI API Key**: Make sure you have your OpenAI API key. You can set it as an environment variable or directly in `generate_code.py`.
2. **Run the Script**: Execute `python generate_code.py`.

The script will use the OpenAI Completion API to generate solutions for each of the 100 problems based on their prompts. The solutions will be saved in a designated directory.

---

## 🤝 Contributions and Feedback

Feel free to contribute to this pioneering project by submitting pull requests or issues. Your insights are invaluable.

---

## 🌠 Acknowledgements

Many thanks to the OpenAI team for providing the API and for their groundbreaking work in the field of AI, making this project possible.