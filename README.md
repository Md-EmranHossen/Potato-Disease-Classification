# Potato-Disease-Classification(Early blight & Late blight)
![late_blight_1](https://github.com/user-attachments/assets/d87d1f9d-2c19-490c-bd78-77a2b0a97765)
![early_blight_1](https://github.com/user-attachments/assets/b2325ac3-8660-425d-9118-55ef4d58247d)


This project classifies potato leaf images into two disease categories: Early Blight and Late Blight, using deep learning techniques. The model is trained on a dataset sourced from Kaggle, and utilizes Convolutional Neural Networks (CNNs) for accurate classification.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Setup](#setup)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to develop a deep learning model that can distinguish between Early Blight and Late Blight in potato leaves. These two diseases are major threats to potato crops, and an automated detection system can help farmers monitor and control these diseases more effectively.

## Dataset

The dataset for this project is available on Kaggle and contains images of potato leaves, labeled as either "Early Blight" or "Late Blight."

[Kaggle Potato Diseases Dataset](https://www.kaggle.com/datasets/sbhatti/plantdisease)

### Dataset Details:
- **Categories**: Early Blight, Late Blight
- **Image Size**: 224x224 pixels
- **Labels**: Images are labeled based on the type of disease or "Healthy" if applicable.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/potato-diseases-classification.git
cd potato-diseases-classification
```

### 2. Install Dependencies

Install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

Download the dataset from Kaggle and place it in the `data/` folder.

```bash
mkdir data
# Move your dataset here
```

## Model Architecture

The classification model is built using Convolutional Neural Networks (CNN). The architecture includes:

- **Conv2D Layers** for feature extraction
- **MaxPooling** for downsampling
- **Fully Connected Layers** for classification
- **Softmax Activation** for binary classification (Early Blight vs. Late Blight)

The model is implemented using [TensorFlow](https://www.tensorflow.org/) (or PyTorch, depending on the framework used).

## Training

To train the model, run:

```bash
python train.py
```

### Training Parameters:
- **Batch Size**: 32
- **Epochs**: 20
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy

## Usage

After training, you can use the model for predictions:

```bash
python predict.py --image path/to/leaf_image.jpg
```

This will output either "Early Blight" or "Late Blight."

## Results

The model achieves an accuracy of **XX%** on the validation set. The confusion matrix for the results is as follows:

|           | Early Blight | Late Blight |
|-----------|--------------|-------------|
| **Early Blight** | 500          | 30          |
| **Late Blight**  | 40           | 450         |

## Contributing

Feel free to contribute by forking the repository and submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
