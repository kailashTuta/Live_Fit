# Live Fit

Live Fit is a Django-based web application designed to help users track their fitness goals, monitor progress, and stay motivated.

## Features

- User authentication and profile management
- AI Dietician: Personalized Diet Plans: The AI-powered dietician generates customized diet plans based on your BMI, helping you achieve your fitness and health goals.
- Workout Recommendations: Along with diet plans, the AI also suggests suitable workout routines that complement your dietary needs and fitness level.
- Blog Sharing & Editing: Create & Share Blogs: Users can write, share, and edit their own blogs related to health, fitness, diet, and wellness.
- Interact with Other Blogs: Read and explore blogs written by other users.
- Ayurvedic Tips: Holistic Health Advice: Access a section dedicated to Ayurvedic tips that provide natural remedies and lifestyle advice for overall wellness.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kailashTuta/Live_Fit.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv Live_Fit
   source Live_Fit/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Navigate to the project directory:
   ```bash
   cd Live_Fit
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register for a new account or log in with your superuser credentials.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
