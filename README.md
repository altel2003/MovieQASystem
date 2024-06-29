# MovieQASystem
A simple movie knowledge graph project implemented with flask+neo4j+sklearn. It is academic garbage, just take a look.
---

# Instructions for Setting Up and Running the Project

## Step 1: Pre-configure Neo4j and the Python Environment
- **Neo4j Setup:** Ensure you have Neo4j installed and configured. Replace the default import folder in Neo4j with the provided import folder.
- **Python Environment:** Configure the Python environment according to the specifications in `requirements.txt`.

## Step 2: Configure and Run `Graph_create.py`
1. **Modify Database Connection:**
    - Open `Graph_create.py`.
    - Locate the following line:
        ```python
        # 创建Neo4j数据库连接
        graph = Graph("bolt://localhost:7687", user="neo4j", password="neo4jhan")  # 修改你的密码
        ```
    - Replace `"neo4jhan"` with your actual password.
2. **Run the Script:**
    - Ensure the Neo4j service is running.
    - Execute `Graph_create.py` to create the required Neo4j database for the project.
    - **Important:** The script will clear the existing database by default. If you want to keep your old database, comment out the line:
        ```python
        graph.delete_all()
        ```

## Step 3: Run the Application
- Execute `app.py`.
- Open your web browser and navigate to `127.0.0.1:5000` to start interacting with the application.

---

## 如何使用？

### 步骤1：预先配置Neo4j及Python环境
- **Neo4j设置：** 确保您已安装并配置好Neo4j，将Neo4j中的默认import文件夹替换为提供的import文件夹。
- **Python环境：** 根据`requirements.txt`中的要求配置Python环境。

### 步骤2：配置并运行`Graph_create.py`
1. **修改数据库连接：**
    - 打开`Graph_create.py`。
    - 找到以下代码：
        ```python
        # 创建Neo4j数据库连接
        graph = Graph("bolt://localhost:7687", user="neo4j", password="neo4jhan")  # 修改你的密码
        ```
    - 将`"neo4jhan"`替换为您的实际密码。
2. **运行脚本：**
    - 确保Neo4j服务已启动。
    - 执行`Graph_create.py`以创建项目所需的Neo4j数据库。
    - **注意：** 脚本默认会清空原有数据库。如果您希望保留旧数据库，请注释掉以下代码：
        ```python
        graph.delete_all()
        ```

### 步骤3：运行应用程序
- 执行`app.py`脚本。
- 在浏览器中打开`127.0.0.1:5000`进行交互。

---

Feel free to follow these steps to set up and run your project. Happy coding! 🚀
