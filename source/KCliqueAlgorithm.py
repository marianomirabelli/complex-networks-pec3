import glob, os, io
import  networkx as nx
import stat
from networkx.algorithms import community


def exectueCliqueAlgorithm(directory):

    os.chdir(directory)
    for file in glob.glob("*.net"):

        file_name = file.split(".")[0]+ ".clu"

        '''
        multigraph = nx.read_pajek(file)
        modelGraph = nx.Graph(multigraph)
        file_name = file.split(".")[0]+ ".clu"
        file_directory = os.path.join("../../results-kclique/",file_name)
        f = open(file_directory, "w+")
        communities = community.k_clique_communities(modelGraph,3)

        lines = [None] * (len(modelGraph)+1)
        group_number = 1

        for group in communities:
            group_as_string = str(group_number)
            for node_value in group:
                id = modelGraph.nodes.get(node_value)['id']
                index = int(id)
                lines[index] = group_as_string
            group_number+=1

        lines[0] = "*Vertices " + str(len(modelGraph))
        for index, x in enumerate(lines):
            if x is None:
                lines[index] = str(group_number)
                group_number += 1
        f.writelines('\n'.join(lines))
        f.write("\n")
        f.close()
        os.chdir("../../radatools/Communities_Tools/")
        st = os.stat('./Compare_Partitions.exe')
        os.chmod("./Compare_Partitions.exe", st.st_mode | stat.S_IEXEC)
        if ("model" in directory) and ("rb125" in file_name):
                index = 1
                while(index<=3):
                    os.system("./Compare_Partitions.exe ../../results-kclique/" + file_name + " ../" + directory
                              + "rb125-"+str(index)+".clu" + " ../../results-kclique/" + file_name + "-"+str(index) + ".exit " + " V")
                    index+=1
        else:
            os.system("./Compare_Partitions.exe ../../results-kclique/" + file_name + " ../" + directory
                      + file_name + " ../../results-kclique/" + file_name + ".exit " + " V")

        os.chdir("../" + directory)
        '''
        os.chdir("../../radatools/Communities_Tools/")
        st = os.stat('./Modularity_Calculation.exe')
        os.chmod("./Modularity_Calculation.exe", st.st_mode | stat.S_IEXEC)
        os.system("./Modularity_Calculation.exe ../" + directory + file + " ../../results-kclique/" + file_name
                  + " 0 0 UN TC 2 >> " + " ../../results-kclique/" + file_name + ".modularity")
    os.chdir("../../source")


def main():

    exectueCliqueAlgorithm("../files/model/")
    exectueCliqueAlgorithm("../files/toy/")
    exectueCliqueAlgorithm("../files/real/")

main()

