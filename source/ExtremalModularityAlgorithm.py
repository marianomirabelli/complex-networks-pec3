import glob, os, io
import stat

def execute(directory):

    os.chdir(directory)
    for file in glob.glob("*.net"):

        lol_file_name = file.split(".")[0] + ".lol"
        clu_file_name = file.split(".")[0] + ".clu"
        input_directory = os.path.join("../" + directory, file)
        '''
        lol_file_name = file.split(".")[0]+ ".lol"
        clu_file_name = file.split(".")[0]+ ".clu"
        input_directory = os.path.join("../" + directory,file)
        lol_exit_directory = os.path.join("../../results-extremal-m/", lol_file_name)
        clu_exit_direcotry = os.path.join("../../results-extremal-m/", clu_file_name)
        os.chdir("../../radatools/Communities_Detection/")
        st = os.stat("./Communities_Detection.exe")
        os.chmod("./Communities_Detection.exe", st.st_mode | stat.S_IEXEC)
        os.system("./Communities_Detection.exe V UN E 2 0 1.0 " + input_directory + " " + lol_exit_directory)
        os.chdir("../../radatools/Communities_Tools/")
        st = os.stat("./Convert_Lol_To_Clu.exe")
        os.chmod("./Convert_Lol_To_Clu.exe", st.st_mode | stat.S_IEXEC)
        os.system("./Convert_Lol_To_Clu.exe " + lol_exit_directory + " " + clu_exit_direcotry + " 2")

        os.chdir("../../radatools/Communities_Tools/")
        st = os.stat('./Compare_Partitions.exe')
        os.chmod("./Compare_Partitions.exe", st.st_mode | stat.S_IEXEC)
        if ("model" in directory) and ("rb125" in input_directory):
                index = 1
                while (index <= 3):
                    os.system("./Compare_Partitions.exe ../../results-extremal-m/" + clu_file_name + " ../" + directory
                              + "rb125-" + str(index) + ".clu" + " ../../results-extremal-m/" + clu_file_name + "-" + str(
                        index) + ".exit " + " V")
                    index += 1
        else:
            os.system("./Compare_Partitions.exe ../../results-extremal-m/" + clu_file_name + " ../" + directory
                      + clu_file_name + " ../../results-extremal-m/" + clu_file_name + ".exit " + " V")

        os.chdir("../" + directory)
        '''
        os.chdir("../../radatools/Communities_Tools/")
        st = os.stat('./Modularity_Calculation.exe')
        os.chmod("./Modularity_Calculation.exe", st.st_mode | stat.S_IEXEC)
        os.system("./Modularity_Calculation.exe " + input_directory + " ../../results-extremal-m/" + clu_file_name
                   + " 0 0 UN TC 2 >> " + " ../../results-extremal-m/" + clu_file_name + ".modularity")

    os.chdir("../../results-extremal-m/")
    os.system("rm *.log")
    os.system("rm *.lol")



def main():

    execute("../files/model/")
    execute("../files/toy/")
    execute("../files/real/")

main()
