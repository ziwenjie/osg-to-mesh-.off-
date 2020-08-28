# _*_ coding: utf-8 -*-
# @Time      : 8/28/20 2:54 PM
# @Author    : title_z
# @Filename  : OSGTOOFF_L25.py

import os


def generaterawface(filename1, filename2):
    """
    生成rawface文件
    格式：
           0 1 2 3 4 5 6 7 8 9
           10 11 12 13 14 15 16 17 18 19
           20 21 22 23 24 25 26 27 28 29
    :param filename1:  原始的osg文件
    :param filename2:  生成的rawface文件
    :return: 无
    """
    # with open('Tile_+000_+000_L25_00000410_sub1.osg', 'r') as osg:
    with open(filename1, 'r') as osg:
        lines = osg.readlines()
        lines = str(lines)
        begin = lines.find('DrawElementsUInt TRIANGLES')
        end = lines.rfind('VertexArray UniqueID Vec3Array_3 Vec3Array')
        faces = lines[begin + 52:end - 41]
        faces = faces.split(',')
        i = 0
        # with open('face.txt', 'a') as f0:
        with open(filename2, 'a') as f0:
            f0.write(' ')
            for face in faces:

                if i < len(faces) - 1:
                    face = face.replace('\\n', '')
                    face = face.replace("'", '')
                    f0.write(face)
                    f0.write('\n')
                    i += 1
                else:
                    face = face.replace('\\n', '')
                    face = face.replace("'", '')
                    f0.write(face)
            f0.close()


def generaterawvertex(filename1, filename2):
    """
    生成rawvertex文件
    形状：
         -20.0933 -46.2571 -29.9932
         -20.0001 -46.2966 -29.8956
         -20.0278 -46.3562 -29.9925
         -18.8853 -45.6837 -31.7788
    :param filename1:   原始的osg文件
    :param filename2:   生成的vertex文件
    :return: 无
    """
    with open(filename1, 'r') as osg:
        # with open('Tile_+000_+000_L25_00000410_sub1.osg', 'r') as osg:
        lines = osg.readlines()
        lines = str(lines)
        begin = lines.find('VertexArray UniqueID Vec3Array_3 Vec3Array')
        end = lines.rfind('TexCoordArray 0 UniqueID Vec2Array_4 Vec2Array')
        vertexes = lines[begin + 65:end - 25]
        vertexes = vertexes.split(',')
        print(vertexes)
        i = 0
        # with open('vertex.txt', 'a') as f1:
        with open(filename2, 'a') as f1:
            f1.write(' ')
            for vertex in vertexes:

                if i < len(vertexes) - 1:
                    vertex = vertex.replace('\\n', '')
                    vertex = vertex.replace("'", '')
                    f1.write(vertex)
                    f1.write('\n')
                    i += 1
                else:
                    vertex = vertex.replace('\\n', '')
                    vertex = vertex.replace("'", '')
                    f1.write(vertex)
            f1.close()


def generatevertex(filename1, filename2):  # filename1是读取的文件, filename2
    """
    :param filename1: 原始的点的坐标
    :param filename2: 最终生成的数据
    :return:
    """
    vertexes = open(filename1).readlines()
    print(vertexes)
    f = open(filename2, 'a')
    for vertex in vertexes:
        f.write(vertex.replace('         ', ''))
    f.close()


def genneratefaces(filename1, filename2):
    """
    :param filename1:    是原始triface数据
    :param filename2:   生成一维的face数组   shape: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    :return:
    """
    faces = open(filename1).readlines()
    # faces = open('offeaxample.txt').readlines()
    # f = open('faces.txt', 'a')
    f = open(filename2, 'a')
    for face in faces:
        face = face.replace(',', '')
        face = face.replace('          ', '')
        face = face.replace('\n', ' ')
        f.write(face)
    f.close()


def genneratefaces(filename1, filename2):
    """
    :param filename1:    是原始triface数据
    :param filename2:   生成一维的face数组   shape: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    :return:
    """
    faces = open(filename1, 'r').readlines()
    # faces = open('offeaxample.txt').readlines()
    # f = open('faces.txt', 'a')
    f = open(filename2, 'a')
    for face in faces:
        face = face.replace(',', '')
        face = face.replace('           ', '')
        face = face.replace('\n', ' ')
        f.write(face)
    f.close()


def generatetrifaces(filename1, filename2):
    """
    :param filename1: 此处filename1与generatefaces的filename2相同
    :param filename2: 是生成中间文件，
            shape:0 1 2
                  3 4 5
                  6 7 8
                  9 10 11
    :return:
    """
    with open(filename1, 'r') as f1:
        # with open('faces.txt', 'a') as f1:
        for line in f1:
            str0 = line.split(' ')
            for j in range(len(str0)):
                with open(filename2, 'a') as trifaces:
                    # with open('trifaces.txt', 'a') as trifaces:
                    if (j + 1) % 3 == 0:
                        # result.append(str0[j])
                        # result.append('\n')
                        trifaces.write(str0[j])
                        trifaces.write('\n')
                    else:
                        # result.append((str0[j]))
                        trifaces.write(str0[j])
                        trifaces.write(' ')


def generateofftriface(filename1, filename2):
    """
    :param filename1: 与 generatetrifaces的filename2相同
    :param filename2:  生成off格式的数据形式
    shape: 3  0 1 2
           3  3 4 5
           3  6 7 8
    :return:
    """
    with open(filename1, 'r') as f1:
        # with open('trifaces.txt') as f:
        lines = f1.readlines()
        with open(filename2, 'a') as f2:
            # with open('add3.txt', 'a') as f2:
            for line in lines:
                f2.write('3  ')
                f2.write(line)
            f2.close()
        f1.close()


if __name__ == '__main__':
    path =   # 原始文件的地址
    destination =  # 目的地地址
    names = []
    i = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if os.path.splitext(file)[1] == '.osg' and 'L25' in str(os.path.splitext(file)[0]):
                names.append(os.path.join(dirpath, file))
                currentname = os.path.join(dirpath, file)  # 当前的处理的文件  即currentname是现在处理的文件 filename1
                # print(currentname)
                # rawface.txt
                rawfacename = 'rawface{0}.txt'.format(i)  # 当前生成的rawface.txt文件
                rawfaceaddr = os.path.join(destination, rawfacename)  # 当前生成的rawface.txt文件的路径
                generaterawface(currentname, rawfaceaddr)  # 生成rawface.txt文件

                # rawvertex.txt
                rawvertexname = 'rawvertex{0}.txt'.format(i)  # 当前生成的 rawvertex.txt 文件
                rawvertexaddr = os.path.join(destination, rawvertexname)  # 当前生成的 rawvertex.txt 文件的路径
                generaterawvertex(currentname, rawvertexaddr)  # 生成 rawvertex.txt

                # vertex.txt
                vertexname = 'vertex{0}.txt'.format(i)  # 当前生成的vertex.txt文件
                vertexaddr = os.path.join(destination, vertexname)  # 当前生成的vertex.txt文件的路径
                generatevertex(rawvertexaddr, vertexaddr)  # 当前生成vertex.txt文件

                # oneface.txt
                onedfacename = 'onedface{0}.txt'.format(i)  # 当前生成 onedface.txt文件
                onedfaceaddr = os.path.join(destination, onedfacename)
                genneratefaces(rawfaceaddr, onedfaceaddr)  # 生成了 oneface.txt

                # trifaces.txt
                trifacesname = 'triface{0}.txt'.format(i)  # 产生文件名
                trifacesaddr = os.path.join(destination, trifacesname)  # 产生文件地址
                generatetrifaces(onedfaceaddr, trifacesaddr)  # 生成文件

                # offtriface.txt文件
                offtrifacename = 'offtriface{0}.txt'.format(i)
                offtrifaceaddr = os.path.join(destination, offtrifacename)
                generateofftriface(trifacesaddr, offtrifaceaddr)

                """
                上方产生了所有的所需以及中间文件
                下面产生.off文件
                """
                with open(offtrifaceaddr) as f0:
                    line1 = f0.readlines()
                    var1 = str(len(line1))
                    f0.close()
                with open(vertexaddr) as f1:
                    line2 = f1.readlines()
                    var2 = str(len(line2))
                    f1.close()
                off = 'meshes{0}.off'.format(i)
                offaddr = os.path.join(destination, off)
                i += 1
                with open(offaddr, 'a') as offfile:
                    offfile.write('OFF')
                    offfile.write('\n')
                    offfile.write(var2 + ' ' + var1 + ' ' + '0')
                    offfile.write('\n')
                    with open(vertexaddr) as f1:
                        line2 = f1.readlines()
                        for line in line2:
                            offfile.write(line)
                        f1.close()
                    with open(offtrifaceaddr) as f0:
                        line1 = f0.readlines()
                        for line in line1:
                            offfile.write(line)
                        f0.close()
                    offfile.close()
