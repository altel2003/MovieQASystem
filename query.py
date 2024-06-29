from py2neo import Graph,Node,Relationship,NodeMatcher


class Query():
    def __init__(self):
        self.graph=Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

    # 问题类型0，查询电影得分
    def run(self,cql):
        result=[]
        find_rela = self.graph.run(cql)
        for i in find_rela:
            result.append(i.items()[0][1])
        return result