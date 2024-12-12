# codevertex
# 📚 Book Recommendation System and Multi-feature Applications

Welcome to a multi-functional project that combines a **Book Recommendation System**, an **Interactive Chatbot**, and an **Image Captioning Application**, each designed for unique user interactions and experiences.

---

## 🚀 Features

### 📖 Book Recommendation System
- 📘 View a dataset with detailed book information.
- 🔍 Enter your favorite book title and get personalized recommendations.
- 📝 Provides detailed descriptions of recommended books.

### 🤖 Interactive Chatbot
- 💬 Engage in natural conversations.
- 🧠 Handles multiple intents like greetings, weather queries, and general chats.
- ✨ Simulates realistic responses with typing effects.

### 🖼️ Image Captioning
- 📤 Upload images and receive AI-generated captions.
- 🖼️ Supports multiple image formats (JPG, PNG).

---

## 🛠️ Technology Stack

- **Frontend:**
  - 🌐 Streamlit

- **Backend:**
  - 🐍 Python

- **Libraries:**
  - `Streamlit`: For interactive web apps.
  - `Pandas`: For data manipulation.
  - `NumPy`: For numerical computations.
  - `scikit-learn`: For vectorization and similarity calculations.
  - `transformers`: For AI-based image captioning.
  - `torch`: For deep learning capabilities.
  - `Pillow`: For image processing.

---

## 📂 Dataset

### Book Recommendation System
The dataset (`data.csv`) includes:
- 📕 Book titles
- ✍️ Authors
- 🗂️ Categories
- 📅 Published year
- 🖼️ Thumbnails
- 📜 Descriptions

Ensure the file is in the project directory.

---

## 💻 Installation and Usage

### 1️⃣ Prerequisites
- 🖥️ Python 3.8 or higher
- 🛠️ Recommended: Create a virtual environment

### 2️⃣ Clone the Repository
```bash
$ git clone https://github.com/yourusername/project-repo.git
$ cd project-repo
```

### 3️⃣ Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4️⃣ Run the Applications
#### Book Recommendation System:
```bash
$ streamlit run book_recommendation_app.py
```

#### Interactive Chatbot:
```bash
$ python interactive_chatbot.py
```

#### Image Captioning:
```bash
$ streamlit run image_captioning_app.py
```

---

## 🧪 How It Works

### Book Recommendation System
1. Dataset Handling:
   - 📊 Loads the dataset using Pandas.
   - ⚙️ Fills missing data with empty strings.

2. Feature Engineering:
   - 🧩 Combines title, categories, authors, and descriptions into a single text field.

3. Vectorization:
   - 🔢 Converts text to numerical vectors using TF-IDF.

4. Similarity Calculation:
   - 📈 Computes cosine similarity between books.

5. Recommendation:
   - 🎯 Recommends similar books based on user input.

### Interactive Chatbot
1. **Intent Matching**:
   - 🔍 Uses regex to identify user intent.

2. **Dynamic Responses**:
   - 💡 Responds to user queries with relevant answers.

3. **Typing Effects**:
   - 🕒 Simulates typing delays for realistic conversations.

### Image Captioning
1. **Image Processing**:
   - 🖌️ Converts images to RGB if necessary.

2. **Caption Generation**:
   - 🤖 Uses a pre-trained VisionEncoderDecoder model to generate captions.

3. **Output**:
   - 📜 Displays captions along with uploaded images.

---

## 🌟 Example Usage

### Book Recommendation System
1. **Enter a Book Title**:
   - 🖊️ Input a favorite book title in the search bar.
2. **Receive Recommendations**:
   - 📑 The system displays the top 10 similar books with their descriptions.

### Interactive Chatbot
1. 🗣️ Start the chatbot and respond to its questions.
2. 🌐 Explore various intents like greetings, weather, or hobbies.

### Image Captioning
1. 📂 Upload an image file.
2. 🖼️ View the AI-generated caption.


Enjoy exploring books, chatting, and captioning images! 📖✨

