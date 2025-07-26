# 🎮 Multi-Label Game Genre Classifier

A multi-label classification system to predict game genres from descriptions using FastAI, Hugging Face Transformers, and ONNX for deployment.

---

## 📌 Overview

This project demonstrates end-to-end NLP for classifying video game genres based on textual descriptions. It includes:

- Web scraping using Selenium
- Dataset preparation
- Model training using `fastai`, `transformers`, and `blurr`
- Conversion to ONNX (with quantization)
- Deployment on Hugging Face Spaces and Render

---

## 🗃 Dataset

- Scraped from [IMDb](https://www.imdb.com/) using **Selenium**
- Final dataset has **3 columns**:
  - `name`: Game title
  - `description`: Game description
  - `genres`: Multi-label genre tags

📁 **Final CSV:** [Download here](https://github.com/SajjadHossain43/app-multi-label-classification-imdb/tree/main/Dataset) <!-- 🔁 Replace with your actual dataset link -->

---

## 🧠 Modeling Approach

- Used [`fastai.text`](https://docs.fast.ai/text/) + [`transformers`](https://huggingface.co/transformers/) with [`blurr`](https://github.com/ohmeow/blurr)
- Base model: [`distilroberta-base`](https://huggingface.co/distilroberta-base) (chosen for light GPU usage)
- Training was done in **two stages**, saving each stage's model
- Final model exported for ONNX inference

🧪 **Validation**: 10% split using `RandomSplitter`

---

## 📏 Evaluation Metrics

- **F1 Score (macro & micro)**
- **Multi-label accuracy**
  - Threshold: `0.2` to consider a label as predicted

---

## 🔁 ONNX Conversion

Converted final model to ONNX in **two formats**:

1. Regular ONNX
2. Quantized ONNX

✅ Both versions produce the same evaluation results.

📦 **Quantized ONNX Model:** [Download here](https://drive.google.com/drive/folders/1MK2XDAeef6U1cSdeCdnOESnofPnBcO0s) <!-- 🔁 Replace with ONNX model link -->

---

## 🚀 Deployment

### 🧪 Hugging Face Spaces

- Built with **Gradio**
- Uses **quantized ONNX model** for inference

🔗 [Live on Hugging Face Spaces](https://huggingface.co/spaces/Sajjad43/app-multi-label-classification-imdb) <!-- 🔁 Replace with your HF Space link -->

---

### 🌐 Flask Frontend

- A simple **Flask** web app that calls the Hugging Face Space API
- Final app deployed on **Render**

🔗 [Live on Render](https://app-multi-label-classification-imdb.onrender.com) <!-- 🔁 Replace with your Render app link -->

---

## 🛠 Tech Stack

- Python, Pandas, Numpy
- Selenium
- FastAI, Hugging Face Transformers, Blurr
- ONNX, ONNX Runtime, Optimum
- Gradio, Flask
- Hugging Face Spaces, Render

---

## 📸 Screenshots

> *(Add screenshots of your UI here)*  
> ![Gradio UI Screenshot](https://github.com/SajjadHossain43/app-multi-label-classification-imdb/blob/main/Assets/hf-space.png)  
> ![Flask UI Screenshot](https://github.com/SajjadHossain43/app-multi-label-classification-imdb/blob/main/Assets/render-service.png)

---

## ✅ TODOs / Future Improvements

- [ ] Try larger models like `roberta-large` on better GPU
- [ ] Optimize ONNX quantization further
- [ ] Expand dataset coverage
- [ ] Add confidence scores per predicted label

---

## 📜 License

This project is released under the [MIT License](LICENSE).

---
