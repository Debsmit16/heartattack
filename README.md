# Heart Attack Prediction Django App

A Django web application that predicts heart attack risk using machine learning.

## Features

- Heart attack risk prediction using machine learning model
- User-friendly web interface
- Real-time prediction results

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the Django project:
   ```bash
   cd HeartAttack_ML
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment on Vercel

This project is configured for deployment on Vercel. Follow these steps:

### Prerequisites
- GitHub account
- Vercel account (sign up at vercel.com)

### Deployment Steps

1. **Push to GitHub:**
   - Create a new repository on GitHub
   - Push your code to the repository:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/yourusername/your-repo-name.git
     git push -u origin main
     ```

2. **Deploy on Vercel:**
   - Go to [vercel.com](https://vercel.com) and sign in
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the configuration from `vercel.json`
   - Click "Deploy"

3. **Environment Variables (Optional):**
   - In Vercel dashboard, go to your project settings
   - Add environment variables if needed:
     - `SECRET_KEY`: Your Django secret key
     - `DEBUG`: Set to `false` for production

### Project Structure

```
Heart attack/
├── HeartAttack_ML/          # Django project directory
│   ├── HeartPred/           # Django app
│   ├── templates/           # HTML templates
│   ├── db.sqlite3          # SQLite database
│   ├── dtc.pkl             # Machine learning model
│   └── manage.py           # Django management script
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel configuration
├── build_files.sh          # Build script for Vercel
└── README.md               # This file
```

## Technologies Used

- Django 5.2.3
- Python 3.9+
- scikit-learn
- NumPy
- Pandas
- Gunicorn (for production)
- WhiteNoise (for static files)

## Model Information

The application uses a Decision Tree Classifier (dtc.pkl) to predict heart attack risk based on:
- Age
- Gender
- Heart rate (impulse)
- Blood pressure (high/low)
- Glucose levels
- Troponin levels
