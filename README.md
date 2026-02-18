# CodeArena 🏆 
# made with ❤️ by CoderJaunt - @mit
## 20-Day Python & MySQL Learning System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://mysql.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive, hands-on learning system for mastering Python programming and MySQL database development through building a real-world **Developer Tournament System**.

---

## 📚 Course Overview

CodeArena is a structured 20-day learning journey that takes you from Python basics to building a complete tournament management system with database integration. Each day includes:

- **Examples**: Step-by-step concept demonstrations
- **Projects**: Practical implementations
- **Challenges**: Test your understanding

### 🎯 What You'll Build

A complete **CodeArena Tournament System** featuring:
- Player registration and profiles
- Tournament management
- Leaderboards and rankings
- XP and badge system
- Multi-threaded match processing
- Data export and reporting
- CLI interface

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the repository:**
   ```bash
   cd codearena
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup MySQL Database:**
   ```sql
   CREATE DATABASE codearena_db;
   USE codearena_db;
   ```

---

## 📅 Learning Path

### Week 1: Python Fundamentals

| Day | Topic | Project |
|-----|-------|---------|
| **Day 01** | Variables, Data Types, Strings | Database Setup & Table Creation |
| **Day 02** | Functions & Lambda | INSERT Operations |
| **Day 03** | Modules & Packages | Modular DB Structure |
| **Day 04** | OOP - Classes & Objects | Player Class |
| **Day 05** | OOP - Inheritance | Tournament Management |

### Week 2: Advanced Python

| Day | Topic | Project |
|-----|-------|---------|
| **Day 06** | Lambda Functions | Leaderboard Filtering |
| **Day 07** | Map, Filter, Reduce | XP Calculations |
| **Day 08** | Exception Handling | Safe DB Operations |
| **Day 09** | File Handling | Export Leaderboard |
| **Day 10** | Regular Expressions | Username/Email Validation |

### Week 3: Professional Python

| Day | Topic | Project |
|-----|-------|---------|
| **Day 11** | Generators | Level Progression |
| **Day 12** | Iterators | Badge Iterator |
| **Day 13** | Decorators | XP Boosters & Permissions |
| **Day 14** | Logging | System Event Tracker |
| **Day 15** | Virtual Environments | Environment Setup |

### Week 4: Advanced Topics & Integration

| Day | Topic | Project |
|-----|-------|---------|
| **Day 16** | Multithreading | Concurrent Matches |
| **Day 17** | SQL Aggregation & Reporting | Tournament Reports |
| **Day 18** | Performance Optimization | Leaderboard Optimization |
| **Day 19** | Clean Architecture | Full Integration |
| **Day 20** | CLI Development | CodeArena CLI |

---

## 📁 Project Structure

```
codearena/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── 00_COMPLETE_GUIDE.py         # Full course overview
├── README.py                    # Project documentation
│
├── day01/                       # Python Basics
│   ├── examples/                # Concept demonstrations
│   │   ├── ex01_variables.py
│   │   ├── ex02_arithmetic.py
│   │   ├── ex03_strings.py
│   │   └── ex04_input.py
│   └── project/                 # Practical implementation
│       ├── database_setup.py
│       └── challenge.py
│
├── day02/                       # Functions
│   ├── examples/
│   └── project/
│
├── day03/                       # Modules
├── day04/                       # OOP - Player
├── day05/                       # OOP - Tournament
├── day06/                       # Lambda
├── day07/                       # Map/Filter/Reduce
├── day08/                       # Exception Handling
├── day09/                       # File Handling
├── day10/                       # Regex
├── day11/                       # Generators
├── day12/                       # Iterators
├── day13/                       # Decorators
├── day14/                       # Logging
├── day15/                       # Virtual Environments
├── day16/                       # Multithreading
├── day17/                       # SQL Reporting
├── day18/                       # Optimization
├── day19/                       # Integration
├── day20/                       # CLI System
│
└── venv/                        # Virtual environment
```

---

## 🗄️ Database Schema

The project uses the following MySQL tables:

```sql
-- Players table
CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    xp INT DEFAULT 0,
    level INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tournaments table
CREATE TABLE tournaments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    status ENUM('upcoming', 'active', 'completed') DEFAULT 'upcoming'
);

-- Scores table
CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    tournament_id INT,
    points INT DEFAULT 0,
    match_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id)
);

-- Badges table
CREATE TABLE badges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    badge_name VARCHAR(50),
    unlocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(id)
);
```

---

## 🎓 How to Use This Course

### Daily Learning Flow

1. **Read the Examples** (`dayXX/examples/`)
   - Each example focuses on a specific concept
   - Run them individually to see how they work
   - Modify and experiment with the code

2. **Complete the Project** (`dayXX/project/`)
   - Apply what you learned in a practical scenario
   - Projects build on previous days
   - Integrate with the tournament system

3. **Try the Challenges** (`dayXX/project/challenge.py`)
   - Test your understanding
   - Build additional features
   - Practice problem-solving

### Running Examples

```bash
# Activate virtual environment
source venv/bin/activate

# Run a specific example
cd day01
python3 examples/ex01_variables.py

# Run a project
cd day04/project
python3 player_class_db.py
```

---

## 🛠️ Development Tools

### Code Formatting (Optional)
```bash
pip install black
black day01/ day02/  # Format specific directories
```

### Linting (Optional)
```bash
pip install flake8
flake8 day01/ --max-line-length=100
```

### Type Checking (Optional)
```bash
pip install mypy
mypy day04/project/
```

---

## 🧪 Testing

Run syntax validation across all files:
```bash
find . -path ./venv -prune -o -name "*.py" -type f -exec python3 -m py_compile {} \;
```

Run individual files:
```bash
python3 day01/examples/ex01_variables.py
python3 day06/examples/ex01_lambda_basics.py
```

---

## 📊 Progress Tracker

- [ ] Day 01: Python Basics ✓
- [ ] Day 02: Functions ✓
- [ ] Day 03: Modules ✓
- [ ] Day 04: OOP - Player Class ✓
- [ ] Day 05: OOP - Tournament Class ✓
- [ ] Day 06: Lambda Functions ✓
- [ ] Day 07: Map/Filter/Reduce ✓
- [ ] Day 08: Exception Handling ✓
- [ ] Day 09: File Handling ✓
- [ ] Day 10: Regular Expressions ✓
- [ ] Day 11: Generators ✓
- [ ] Day 12: Iterators ✓
- [ ] Day 13: Decorators ✓
- [ ] Day 14: Logging ✓
- [ ] Day 15: Virtual Environments ✓
- [ ] Day 16: Multithreading ✓
- [ ] Day 17: SQL Reporting ✓
- [ ] Day 18: Optimization ✓
- [ ] Day 19: Integration ✓
- [ ] Day 20: CLI System ✓

---

## 🤝 Contributing

This is a learning project, but improvements are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📖 Key Concepts Covered

### Python Fundamentals
- Variables, data types, operators
- Control flow (if/else, loops)
- Functions and scope
- String manipulation
- User input/output

### Object-Oriented Programming
- Classes and objects
- Inheritance and polymorphism
- Class attributes and methods
- Magic methods
- Multiple inheritance

### Advanced Python
- Lambda functions
- Map, filter, reduce
- List/dict comprehensions
- Generators and iterators
- Decorators
- Context managers

### Error Handling
- Try/except blocks
- Custom exceptions
- Database error handling
- Best practices

### File Operations
- Text file handling
- CSV operations
- JSON processing
- Context managers (with statement)

### Database Integration
- MySQL connection
- CRUD operations
- SQL queries
- Transaction management
- Connection pooling

### Concurrency
- Threading basics
- Thread safety
- Thread pools
- Thread communication

### Software Engineering
- Modular code structure
- Clean architecture
- Logging
- Virtual environments
- Package management
- CLI development

---

## 🐛 Troubleshooting

### Common Issues

**MySQL Connection Error:**
```bash
# Ensure MySQL is running
sudo systemctl start mysql  # Linux
brew services start mysql   # macOS

# Check connection
cd day01/project
python3 database_setup.py
```

**Import Errors:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Permission Errors:**
```bash
# Fix file permissions
chmod +x Day-20/project/codearena_cli.py
```

---

## 📈 Learning Outcomes

By completing this course, you will:

- ✅ Master Python programming fundamentals
- ✅ Understand object-oriented programming
- ✅ Work with MySQL databases
- ✅ Handle files and data formats
- ✅ Write clean, modular code
- ✅ Implement error handling
- ✅ Use advanced Python features
- ✅ Build concurrent applications
- ✅ Create CLI tools
- ✅ Develop a complete project

---

## 📞 Support

- 📧 Email: codersjaunt@proton.me
- 🐛 Issues: [GitHub Issues](https://github.com/SwagCode4U/codearena/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/SwagCode4U/codearena/discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Python Software Foundation
- MySQL Community
- All contributors and learners

---

## 🎉 Happy Coding!

Start your journey with `day01/examples/ex01_variables.py` and build your way to a complete tournament management system!

**"Code, Learn, Compete, Win!"** 🏆
**"CodersJaunt"**
