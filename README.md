# 📌 Post Job - Django Mini Project

This mini Django project allows **recruiters** to post jobs with multiple tags like "Remote", "Internship", or "Full-Time".

## ✨ Features

- Create job posts with:
  - Title
  - Description
  - Location
  - Salary
  - Tags (ManyToManyField)
- List all job posts
- View job post details

## 🛠️ Technologies Used

- Python 3.x
- Django
- SQLite
- HTML + Bootstrap (for forms/templates)

## 📁 App Structure

- `jobs/` – Main app handling job posting
  - `models.py` – Job and Tag models
  - `forms.py` – Django ModelForm for job posting
  - `views.py` – Create and display job posts
  - `templates/jobs/` – HTML templates (job form, job list, detail)

## 🚀 How to Run the Project

1. Clone the repo or download the project.
2. Navigate to the project folder:
   ```bash
   cd post-job

## 📌 Purpose
This module demonstrates:
- Creating and managing jobs with Django
- Handling form submissions with ModelForms
- Role-based views (Recruiter vs Candidate)
- Using ManyToMany relationships (tags for jobs)

