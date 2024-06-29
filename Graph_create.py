# 单独运行的脚本。用于创建数据库

from py2neo import Graph

# 创建Neo4j数据库连接
graph = Graph("bolt://localhost:7687", user="neo4j", password="neo4jhan") ##修改你的密码

def run_query(query):
    tx = graph.begin()
    tx.run(query)
    graph.commit(tx)

# 导入电影类型节点
query1 = """
LOAD CSV WITH HEADERS FROM "file:///genre.csv" AS line
MERGE (p:Genre{gid:toInteger(line.gid),name:line.gname})
"""


# 导入演员信息节点
query2 = """
LOAD CSV WITH HEADERS FROM 'file:///person.csv' AS line
MERGE (p:Person { pid:toInteger(line.pid),birth:line.birth,
death:line.death,name:line.name,
biography:line.biography,
birthplace:line.birthplace})
"""


# 导入电影信息节点
query3 = """
LOAD CSV WITH HEADERS FROM "file:///movie.csv" AS line  
MERGE (p:Movie{mid:toInteger(line.mid),title:line.title,introduction:line.introduction,
rating:toFloat(line.rating),releasedate:line.releasedate})
"""


# 导入关系 actedin
query4 = """
LOAD CSV WITH HEADERS FROM "file:///person_to_movie.csv" AS line 
MATCH (from:Person{pid:toInteger(line.pid)}), (to:Movie{mid:toInteger(line.mid)})  
MERGE (from)-[r:actedin{pid:toInteger(line.pid),mid:toInteger(line.mid)}]->(to)
"""


# 导入关系 is
query5 = """
LOAD CSV WITH HEADERS FROM "file:///movie_to_genre.csv" AS line
MATCH (from:Movie{mid:toInteger(line.mid)}), (to:Genre{gid:toInteger(line.gid)})  
MERGE (from)-[r:is{mid:toInteger(line.mid),gid:toInteger(line.gid)}]->(to)
"""
if __name__ == '__main__':
    graph.delete_all()
    run_query(query1)
    run_query(query2)
    run_query(query3)
    run_query(query4)
    run_query(query5)