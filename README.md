# 🎓 Student Management System

A  simple full-stack web application to manage students and their academic results with CSV upload support, dashboards, and automatic CGPA calculation.

---

## 🚀 Features

* 📂 Upload students via CSV
* 📊 Upload results via CSV
* 🎯 Automatic total, percentage & CGPA calculation
* 👨‍🎓 Student Dashboard
* 👩‍🏫 Teacher Dashboard
* 🔐 Authentication (JWT-based)
* 📁 MVC Architecture

---

## 🛠 Tech Stack

* **Backend:** Node.js, Express.js
* **Database:** MongoDB
* **Frontend:** EJS, CSS(Tailwind css)
* **Other:** Multer (file upload), CSV Parser

---

## 📂 Project Structure

```
server/
 ├── controller/
 ├── database/
 ├── middleware/
 ├── model/
 ├── routes/
views/
 ├── student/
 ├── teacher/
 ├── include/
Server.js
package.json
```

---

## ⚙️ How to Run This Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NandaniJS08/student-management-system.git
cd student-management-system
```

---

### 2️⃣ Install Dependencies

```bash
npm install
```

---

### 3️⃣ Create `.env` File

Create a `.env` file in the root directory and add:

```env
PORT=3000
MONGO_URI=mongodb://localhost:27017/student_mgm2
JWT_SECRET=your_secret_key
```

---

### 4️⃣ Start MongoDB

Make sure MongoDB is running on your system.

---

### 5️⃣ Run the Server

```bash
node Server.js
```

---

### 6️⃣ Open in Browser

```
http://localhost:3000
```

---

## 🧪 Sample Usage

1. Upload student data using CSV file given in repo
2. Upload result data using CSV file given in repo
3. View dashboards for analysis

---

## 📈 Future Improvements

* 📊 Add charts & analytics dashboard
* 🤖 AI-based performance insights
* 🌐 Deploy to cloud (Render / Vercel)
* 📱 Improve UI/UX

---

## 👩‍💻 Author

**Nandani J Solgama**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
