import glob, os, io
import xlsxwriter as xlsx

def remove_items(array):
    array.remove("=")
    array.remove("-")
    array.remove("0.00000000")
    array.remove("=")

def write_modularity(modularity_array,worksheet,row_index):

    worksheet.write(row_index, 0, "Modularity")
    worksheet.write(row_index, 1, modularity_array[1])

def write_headers(worksheet,row_index):

    worksheet.write(row_index, 0, "Partition")
    worksheet.write(row_index, 1, "Modularity")
    worksheet.write(row_index, 2, "Nodes")

def write_modularity_detail(modularity_array,worksheet,row_index):

    worksheet.write(row_index, 0, modularity_array[0])
    worksheet.write(row_index, 1, modularity_array[1])
    worksheet.write(row_index, 2, modularity_array[3].split("(")[1])

def execute(directory,worksheet):
    os.chdir(directory)
    index = 0
    for file in glob.glob("*.modularity"):

        index+=3
        worksheet.write(index, 0, "Network " + file.split(".modularity")[0].split(".clu")[0])
        with open(file, "r") as ins:

           total_modularity = ins.readline()
           array = total_modularity.split()
           remove_items(array)
           index += 1
           write_modularity(array,worksheet,index)
           index += 1
           write_headers(worksheet,index)
           for line in ins:
              index += 1
              array = line.split()
              remove_items(array)
              write_modularity_detail(array,worksheet,index)



def main():
    workbook = xlsx.Workbook('../modularity/modularity_report.xlsx')
    execute("../results-extremal-m/", workbook.add_worksheet('extremal-modularity'))
    execute("../results-greeedy-m/", workbook.add_worksheet('greedy-modularity'))
    execute("../results-kclique/", workbook.add_worksheet('kclique-modularity'))
  # execute("../results-label-p/", workbook.add_worksheet('extremal-modularity'))
  #  execute("../results-spectral-m/", workbook.add_worksheet('extremal-modularity'))
    workbook.close()

main()