# PharmoKal 1.0.1

**PharmoKal** is a medication aggregator that parses data from other websites and provides a search functionality for them. Users can find the required medication and get a link to the original source.

---

## 📋 Project Features

- 🔍 **Medication Search** in a database aggregated from various websites.
- 🔗 **Direct link to the original source** for detailed information about the medication.
- ⚙️ Leveraging **modern technologies** for easy deployment and scaling.

---

## 🛠️ Technologies

- **Backend**: Django
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

---

## 🚀 Installation and Launch

### 🔑 Prerequisites

1. Install [Docker](https://www.docker.com/).
2. Install [Docker Compose](https://docs.docker.com/compose/).

### 📝 Steps to Launch

1. Clone the project repository:

   ```bash
   git clone https://github.com/spareack/pharmacy
   cd pharmokal
   ```

2. Run the following command in the project root to start:

   ```bash
   docker-compose up
   ```

3. Wait for the containers to build. After successful startup, the project will be accessible at:

   ```
   http://localhost:8000
   ```

---

## 📁 Project Structure

- **`backend`**: Main Django application code.
- **`docker-compose.yml`**: Docker Compose configuration.
- **`pyproject.toml, poetry.lock`**: Python dependencies.
- **`.env`**: Environment variables.

---

## ⚙️ Environment Variable Configuration

If needed, modify the `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ENV=Development
POSTGRES_USER=your-db-user
POSTGRES_PASSWORD=your-db-password
POSTGRES_DB=your-db-name
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## 🛠️ Development Commands

- **Create a superuser** (for admin panel access):
  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```

---

## 🔗 Important Links

- **Admin Panel**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

> **💡 Note**: Ensure the parser is properly configured to work with data sources.

