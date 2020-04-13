'''自定义有向图'''
class DirectedGraph(object):
    def __init__(self, d):      #传入字典（顶点：邻接点列表）
        if isinstance(d, dict):
            self.__graph = d
        else:
            self.__graph = dict()
            print('格式错误')

    def __generatePath(self, graph, path, end, results):
        '''深度优先遍历，添加不在之间的路径（作为参数传递，顺便完成了回溯）'''
        current = path[-1]
        if current == end:
            results.append(path)
        else:
            for n in graph[current]:
                if n not in path:
                    self.__generatePath(graph, path+[n], end, results)

    # 寻找两个顶点之间所有可达路径
    def searchPath(self, start, end):
        self.__results = []
        self.__generatePath(self.__graph, [start], end, self.__results)
        self.__results.sort(key=lambda x:len(x))
        print('The path from ', self.__results[0][0], ' to ', self.__results[0][-1], ' is ')
        for path in self.__results:
            print(path)

